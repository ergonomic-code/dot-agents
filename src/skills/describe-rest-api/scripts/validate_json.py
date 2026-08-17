#!/usr/bin/env python3

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator
from jsonschema import exceptions as jsonschema_exceptions


META_KEYS = {"change", "diff"}
TOP_LEVEL_BLOCK_SECTIONS = ("models", "sumTypes", "enums")


class DuplicateKeyError(ValueError):
    pass


class _ParsedObject(dict):
    def __init__(self, *args: Any, duplicate_paths: list[str] | None = None, **kwargs: Any):
        super().__init__(*args, **kwargs)
        self.duplicate_paths = duplicate_paths or []


def _unwrap_value(value: Any) -> tuple[Any, list[str]]:
    if isinstance(value, _ParsedObject):
        plain: dict[str, Any] = dict(value)
        duplicates = list(value.duplicate_paths)
        for key, child in list(plain.items()):
            unwrapped, child_duplicates = _unwrap_value(child)
            plain[key] = unwrapped
            duplicates.extend(f".{key}{path}" for path in child_duplicates)
        return plain, duplicates

    if isinstance(value, list):
        plain_list: list[Any] = []
        duplicates: list[str] = []
        for i, item in enumerate(value):
            unwrapped, item_duplicates = _unwrap_value(item)
            plain_list.append(unwrapped)
            duplicates.extend(f"[{i}]{path}" for path in item_duplicates)
        return plain_list, duplicates

    return value, []


def _collect_duplicate_key_paths(pairs: list[tuple[str, Any]]) -> _ParsedObject:
    result: dict[str, Any] = {}
    duplicate_paths: list[str] = []
    for key, value in pairs:
        unwrapped, child_duplicates = _unwrap_value(value)
        duplicate_paths.extend(f".{key}{path}" for path in child_duplicates)
        if key in result:
            duplicate_paths.append(f".{key}")
        result[key] = unwrapped
    return _ParsedObject(result, duplicate_paths=duplicate_paths)


def load_json(path: Path) -> object:
    with path.open("r", encoding="utf-8") as f:
        parsed = json.load(f, object_pairs_hook=_collect_duplicate_key_paths)
    unwrapped, duplicate_paths = _unwrap_value(parsed)
    if duplicate_paths:
        raise DuplicateKeyError(f"Duplicate key at ${duplicate_paths[0]}")
    return unwrapped


def deep_merge(base: Any, overlay: Any) -> Any:
    if isinstance(base, dict) and isinstance(overlay, dict):
        result = dict(base)
        for key, value in overlay.items():
            if key in result:
                result[key] = deep_merge(result[key], value)
            else:
                result[key] = value
        return result
    return overlay


def project(node: Any, side: str, preserve_meta: bool = False) -> Any:
    if isinstance(node, list):
        out = []
        for item in node:
            item_view = project(item, side, preserve_meta=preserve_meta)
            if item_view is not None:
                out.append(item_view)
        return out

    if not isinstance(node, dict):
        return node

    change = node.get("change")
    if side == "before" and change == "added":
        return None
    if side == "after" and change == "removed":
        return None

    working = dict(node) if preserve_meta else {key: value for key, value in node.items() if key not in META_KEYS}
    overlay = (node.get("diff") or {}).get(side)
    if overlay is not None:
        working = deep_merge(working, overlay)

    result: dict[str, Any] = {}
    for key, value in working.items():
        if key == "diff":
            continue
        if not preserve_meta and key == "change":
            continue

        value_view = project(value, side, preserve_meta=preserve_meta)
        if value_view is not None:
            result[key] = value_view

    return result


def canonical_path(path: str) -> str:
    base_path = path.split("?", 1)[0]
    return re.sub(r"\{[^{}]*\}", "{}", base_path)


def endpoint_key(endpoint: dict[str, Any]) -> str:
    method = endpoint.get("method", "")
    path = endpoint.get("path", "")
    return f"{method} {canonical_path(path)}"


def _response_path_by_status(raw_endpoint: dict[str, Any], endpoint_index: int, status: int) -> str:
    for response_index, response in enumerate(raw_endpoint.get("responses", [])):
        if response.get("status") == status:
            return f"$.endpoints[{endpoint_index}].responses[{response_index}].body.type.refId"
    return f"$.endpoints[{endpoint_index}].responses[?status={status}].body.type.refId"


def _collect_declared_ref_ids(document: dict[str, Any]) -> set[str]:
    declared: set[str] = set()
    for section_name in ("models", "sumTypes", "enums"):
        section = document.get(section_name)
        if not isinstance(section, list):
            continue
        for item in section:
            if isinstance(item, dict):
                item_id = item.get("id")
                if isinstance(item_id, str) and item_id:
                    declared.add(item_id)
    return declared


def _walk_refs(node: Any) -> list[str]:
    ref_ids: list[str] = []

    def walk(value: Any) -> None:
        if isinstance(value, dict):
            if value.get("kind") == "ref":
                ref_id = value.get("refId")
                if isinstance(ref_id, str) and ref_id:
                    ref_ids.append(ref_id)
            for child in value.values():
                walk(child)
        elif isinstance(value, list):
            for child in value:
                walk(child)

    walk(node)
    return ref_ids


def _collect_top_level_blocks(
    document: dict[str, Any],
) -> tuple[dict[str, tuple[str, int, dict[str, Any]]], dict[str, str]]:
    blocks: dict[str, tuple[str, int, dict[str, Any]]] = {}
    paths: dict[str, str] = {}
    for section_name in TOP_LEVEL_BLOCK_SECTIONS:
        section = document.get(section_name)
        if not isinstance(section, list):
            continue
        for index, block in enumerate(section):
            if not isinstance(block, dict):
                continue
            block_id = block.get("id")
            if isinstance(block_id, str) and block_id:
                blocks[block_id] = (section_name, index, block)
                paths[block_id] = f"$.{section_name}[{index}].change"
    return blocks, paths


def _walk_added_only_refs(node: Any, path: str, inherited_added_only: bool = False) -> list[tuple[str, str]]:
    refs: list[tuple[str, str]] = []

    if isinstance(node, dict):
        node_added_only = inherited_added_only or node.get("change") == "added"

        if node.get("kind") == "ref":
            ref_id = node.get("refId")
            if node_added_only and isinstance(ref_id, str) and ref_id:
                refs.append((ref_id, path))

        for key, value in node.items():
            child_path = f"{path}.{key}"
            refs.extend(_walk_added_only_refs(value, child_path, node_added_only))
        return refs

    if isinstance(node, list):
        for index, item in enumerate(node):
            refs.extend(_walk_added_only_refs(item, f"{path}[{index}]", inherited_added_only))
        return refs

    return refs


def _collect_reachable_top_level_refs(block: dict[str, Any]) -> set[str]:
    reachable: set[str] = set()

    def walk(node: Any) -> None:
        if isinstance(node, dict):
            if node.get("kind") == "ref":
                ref_id = node.get("refId")
                if isinstance(ref_id, str) and ref_id:
                    reachable.add(ref_id)
            for value in node.values():
                walk(value)
        elif isinstance(node, list):
            for item in node:
                walk(item)

    walk(project(block, "after"))
    return reachable


def validate_marked_added_ref_targets(document: object) -> list[tuple[str, str]]:
    if not isinstance(document, dict) or document.get("changeMode") != "marked":
        return []

    blocks_by_id, change_paths_by_id = _collect_top_level_blocks(document)
    errors: list[tuple[str, str]] = []
    seen: set[str] = set()
    queue: list[str] = []

    for ref_id, _ in _walk_added_only_refs(document, "$"):
        queue.append(ref_id)

    while queue:
        block_id = queue.pop(0)
        if block_id in seen or block_id not in blocks_by_id:
            continue
        seen.add(block_id)

        section_name, index, block = blocks_by_id[block_id]
        if block.get("change") != "added":
            message = (
                "missing required change='added' for block referenced only from added content"
                if not errors
                else "missing required change='added' for block reachable only from added content"
            )
            errors.append((change_paths_by_id[block_id], message))

        for nested_ref_id in _collect_reachable_top_level_refs(block):
            if nested_ref_id in blocks_by_id and nested_ref_id not in seen:
                queue.append(nested_ref_id)

    return errors


def validate_resolved_ref_ids(document: object) -> list[tuple[str, str]]:
    if not isinstance(document, dict):
        return []

    declared_ref_ids = _collect_declared_ref_ids(document)
    errors: list[tuple[str, str]] = []

    def walk(node: Any, path: str) -> None:
        if isinstance(node, dict):
            if node.get("kind") == "ref" and "refId" in node:
                ref_id = node.get("refId")
                if isinstance(ref_id, str) and ref_id and ref_id not in declared_ref_ids:
                    ref_name = node.get("ref")
                    if isinstance(ref_name, str) and ref_name:
                        errors.append((f"{path}.refId", f"unresolved refId '{ref_id}' for ref '{ref_name}'"))
                    else:
                        errors.append((f"{path}.refId", f"unresolved refId '{ref_id}'"))
            for key, value in node.items():
                walk(value, f"{path}.{key}")
        elif isinstance(node, list):
            for index, item in enumerate(node):
                walk(item, f"{path}[{index}]")

    walk(document, "$")
    return errors


def validate_marked_ref_ids(document: object) -> list[tuple[str, str]]:
    if not isinstance(document, dict) or document.get("changeMode") != "marked":
        return []

    errors: list[tuple[str, str]] = []
    refs_by_key_slot: dict[tuple[str, str], set[str]] = {}
    missing_seen: set[tuple[str, str, str]] = set()

    endpoints = document.get("endpoints")
    if not isinstance(endpoints, list):
        return []

    for endpoint_index, raw_endpoint in enumerate(endpoints):
        if not isinstance(raw_endpoint, dict):
            continue

        for side in ("before", "after"):
            endpoint_view = project(raw_endpoint, side)
            if not isinstance(endpoint_view, dict):
                continue

            key = endpoint_key(endpoint_view)

            request = endpoint_view.get("request")
            if isinstance(request, dict):
                body = request.get("body")
                if isinstance(body, dict) and body.get("kind") == "type":
                    type_expr = body.get("type")
                    if isinstance(type_expr, dict) and type_expr.get("kind") == "ref":
                        ref_id = type_expr.get("refId")
                        path = f"$.endpoints[{endpoint_index}].request.body.type.refId"
                        if not isinstance(ref_id, str) or not ref_id:
                            if (key, "request", path) not in missing_seen:
                                missing_seen.add((key, "request", path))
                                errors.append((path, "missing required refId for marked-mode endpoint body (slot=request)"))
                        else:
                            refs_by_key_slot.setdefault((key, "request"), set()).add(ref_id)

            for response in endpoint_view.get("responses", []):
                if not isinstance(response, dict):
                    continue
                status = response.get("status")
                body = response.get("body")
                if not isinstance(status, int):
                    continue
                if isinstance(body, dict) and body.get("kind") == "type":
                    type_expr = body.get("type")
                    if isinstance(type_expr, dict) and type_expr.get("kind") == "ref":
                        ref_id = type_expr.get("refId")
                        slot = f"response:{status}"
                        path = _response_path_by_status(raw_endpoint, endpoint_index, status)
                        if not isinstance(ref_id, str) or not ref_id:
                            if (key, slot, path) not in missing_seen:
                                missing_seen.add((key, slot, path))
                                errors.append((path, f"missing required refId for marked-mode endpoint body (slot={slot})"))
                        else:
                            refs_by_key_slot.setdefault((key, slot), set()).add(ref_id)

    for (key, slot), ref_ids in sorted(refs_by_key_slot.items()):
        if len(ref_ids) > 1:
            errors.append(("$.endpoints", f"inconsistent refId for endpoint slot ({key}, {slot}): {sorted(ref_ids)}"))

    return errors


def validate_marked_block_changes(document: object) -> list[tuple[str, str]]:
    if not isinstance(document, dict) or document.get("changeMode") != "marked":
        return []

    errors: list[tuple[str, str]] = []
    blocks_by_id: dict[str, dict[str, Any]] = {}

    for section_name in TOP_LEVEL_BLOCK_SECTIONS:
        section = document.get(section_name)
        if not isinstance(section, list):
            continue
        for block_index, block in enumerate(section):
            if not isinstance(block, dict):
                continue

            block_id = block.get("id")
            if not isinstance(block_id, str) or not block_id:
                continue

            blocks_by_id[block_id] = {
                "section": section_name,
                "index": block_index,
                "block": block,
            }

    for info in blocks_by_id.values():
        section_name = info["section"]
        block_index = info["index"]
        block = info["block"]

        if block.get("change") in {"added", "removed", "changed"}:
            continue

        ref_ids = _walk_refs(block)
        if not ref_ids:
            continue

        referenced_blocks = [blocks_by_id[ref_id]["block"] for ref_id in ref_ids if ref_id in blocks_by_id]
        if not referenced_blocks:
            continue

        if all(ref_block.get("change") == "added" for ref_block in referenced_blocks):
            errors.append(
                (
                    f"$.{section_name}[{block_index}].change",
                    "missing required change='added' for marked-mode block composed only of added refs",
                )
            )
            continue

        if all(ref_block.get("change") == "removed" for ref_block in referenced_blocks):
            errors.append(
                (
                    f"$.{section_name}[{block_index}].change",
                    "missing required change='removed' for marked-mode block composed only of removed refs",
                )
            )

    return errors


def render_errors(errors: list[tuple[str, str]]) -> None:
    print(f"Invalid: {len(errors)} error(s)")
    for i, (path, message) in enumerate(errors, start=1):
        print(f"{i}. {path}: {message}")


def validate_custom_rules(document: object, mode: str) -> list[tuple[str, str]]:
    errors: list[tuple[str, str]] = []
    if mode == "strict":
        errors.extend(validate_resolved_ref_ids(document))
    errors.extend(validate_marked_ref_ids(document))
    errors.extend(validate_marked_block_changes(document))
    errors.extend(validate_marked_added_ref_targets(document))
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Validate JSON document against JSON Schema draft 2020-12.",
    )
    parser.add_argument(
        "--mode",
        choices=("strict", "nonstrict"),
        default="strict",
        help="strict rejects unresolved refId values; nonstrict allows unresolved model, enum, sum-type, or endpoint refs",
    )
    parser.add_argument("schema", type=Path, help="Path to JSON Schema file")
    parser.add_argument("document", type=Path, help="Path to JSON document file")
    args = parser.parse_args()

    try:
        schema = load_json(args.schema)
        document = load_json(args.document)

        Draft202012Validator.check_schema(schema)
        validator = Draft202012Validator(schema)

        schema_errors = sorted(validator.iter_errors(document), key=lambda e: list(e.absolute_path))
        if schema_errors:
            rendered = []
            for error in schema_errors:
                path = "$"
                if error.absolute_path:
                    path += "".join(
                        f"[{part}]" if isinstance(part, int) else f".{part}"
                        for part in error.absolute_path
                    )
                rendered.append((path, error.message))
            render_errors(rendered)
            return 1

        custom_errors = validate_custom_rules(document, args.mode)
        if custom_errors:
            render_errors(custom_errors)
            return 1

        print("Valid")
        return 0

    except FileNotFoundError as e:
        print(f"File not found: {e.filename}", file=sys.stderr)
        return 2
    except json.JSONDecodeError as e:
        print(f"Invalid JSON in {e.doc}: {e}", file=sys.stderr)
        return 2
    except DuplicateKeyError as e:
        print

if __name__ == "__main__":
    raise SystemExit(main())
