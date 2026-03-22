#!/usr/bin/env python3

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


CHANGE_MARKERS = {
    "added": "+",
    "changed": "*",
    "removed": "x",
}

BEFORE_TITLE = "Before"
AFTER_TITLE = "After"
META_KEYS = {"change", "diff"}
EMPTY_GUTTER = " "


def change_prefix(change: str | None) -> str:
    return f"{CHANGE_MARKERS[change]} " if change in CHANGE_MARKERS else ""


def gutter_marker(change: str | None) -> str:
    return CHANGE_MARKERS.get(change, EMPTY_GUTTER)


def merge_markers(primary: str, fallback: str) -> str:
    return primary if primary != EMPTY_GUTTER else fallback


def load_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def leading_ws(s: str) -> str:
    return s[: len(s) - len(s.lstrip(" "))]


def render_comment(text: str | None) -> str:
    return f" // {text}" if text else ""


def indent_lines(lines: list[str], indent: str) -> list[str]:
    return [indent + line if line else "" for line in lines]


def attach_prefix(prefix: str, lines: list[str], comment: str | None = None, suffix: str = "") -> list[str]:
    if not lines:
        return [prefix.rstrip() + suffix + render_comment(comment)]

    if len(lines) == 1:
        return [prefix + lines[0] + suffix + render_comment(comment)]

    base_indent = leading_ws(prefix)
    out = [prefix + lines[0]]
    out.extend(base_indent + line for line in lines[1:-1])
    out.append(base_indent + lines[-1] + suffix + render_comment(comment))
    return out


def attach_gutter_prefix(
    prefix: str,
    lines: list[tuple[str, str]],
    marker: str = EMPTY_GUTTER,
    comment: str | None = None,
    suffix: str = "",
) -> list[tuple[str, str]]:
    if not lines:
        return [(marker, prefix.rstrip() + suffix + render_comment(comment))]

    if len(lines) == 1:
        child_marker, child_text = lines[0]
        return [(merge_markers(marker, child_marker), prefix + child_text + suffix + render_comment(comment))]

    base_indent = leading_ws(prefix)
    out: list[tuple[str, str]] = []

    first_marker, first_text = lines[0]
    out.append((merge_markers(marker, first_marker), prefix + first_text))

    for child_marker, child_text in lines[1:-1]:
        out.append((child_marker, base_indent + child_text if child_text else ""))

    last_marker, last_text = lines[-1]
    out.append((merge_markers(marker, last_marker), base_indent + last_text + suffix + render_comment(comment)))
    return out


def format_gutter_lines(lines: list[tuple[str, str]]) -> list[str]:
    out: list[str] = []
    for marker, text in lines:
        if text:
            out.append(f"{marker} {text}")
        else:
            out.append("")
    return out


def indent_gutter_lines(lines: list[tuple[str, str]], indent: str) -> list[tuple[str, str]]:
    return [(marker, indent + text if text else "") for marker, text in lines]


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


def has_changes(node: Any) -> bool:
    if isinstance(node, dict):
        if node.get("change") in CHANGE_MARKERS:
            return True
        return any(has_changes(value) for value in node.values())
    if isinstance(node, list):
        return any(has_changes(item) for item in node)
    return False


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


def render_sum_variant_compact(type_expr: dict[str, Any]) -> str:
    kind = type_expr["kind"]
    if kind == "ref":
        return type_expr["ref"]
    return render_type_compact(type_expr)


def render_type_compact(type_expr: dict[str, Any]) -> str:
    kind = type_expr["kind"]
    nullable = "?" if type_expr.get("nullable") else ""

    if kind == "primitive":
        return f'{type_expr["name"]}{nullable}'
    if kind == "ref":
        return f'<{type_expr["ref"]}>{nullable}'
    if kind == "enum":
        return f'Enum<{"|".join(type_expr["items"])}>{nullable}'
    if kind == "array":
        item = render_type_compact(type_expr["items"])
        return f'[{item}]{nullable}'
    if kind == "sum":
        variants = "|".join(render_sum_variant_compact(variant) for variant in type_expr["variants"])
        return f'<{variants}>{nullable}'

    return f"Object{nullable}"


def is_compact_type(type_expr: dict[str, Any]) -> bool:
    kind = type_expr["kind"]
    if kind in {"primitive", "ref", "enum"}:
        return True
    if kind == "array":
        return is_compact_type(type_expr["items"])
    if kind == "sum":
        return all(is_compact_type(variant) for variant in type_expr["variants"])
    return False


def render_field_lines(field: dict[str, Any], indent: str, is_last: bool) -> list[str]:
    prefix = f'{indent}{change_prefix(field.get("change"))}"{field["name"]}": '
    type_lines = render_type_lines(field["type"])
    suffix = "" if is_last else ","
    return attach_prefix(prefix=prefix, lines=type_lines, comment=field.get("description"), suffix=suffix)


def render_field_gutter_lines(field: dict[str, Any], indent: str, is_last: bool) -> list[tuple[str, str]]:
    prefix = f'{indent}"{field["name"]}": '
    type_lines = render_type_gutter_lines(field["type"])
    suffix = "" if is_last else ","
    return attach_gutter_prefix(
        prefix=prefix,
        lines=type_lines,
        marker=gutter_marker(field.get("change")),
        comment=field.get("description"),
        suffix=suffix,
    )


def render_type_lines(type_expr: dict[str, Any]) -> list[str]:
    kind = type_expr["kind"]
    nullable = "?" if type_expr.get("nullable") else ""

    if kind in {"primitive", "ref", "enum"}:
        return [render_type_compact(type_expr)]

    if kind == "array":
        items = type_expr["items"]
        if is_compact_type(items):
            return [render_type_compact(type_expr)]
        inner = render_type_lines(items)
        lines = ["["]
        lines.extend(indent_lines(inner, "  "))
        lines.append(f"]{nullable}")
        return lines

    if kind == "object":
        fields = type_expr.get("fields", [])
        lines = ["{"]
        for i, field in enumerate(fields):
            lines.extend(render_field_lines(field, "  ", is_last=i == len(fields) - 1))
        lines.append(f'}}{nullable}')
        return lines

    if kind == "sum":
        if is_compact_type(type_expr):
            return [render_type_compact(type_expr)]
        lines = ["<"]
        for i, variant in enumerate(type_expr["variants"]):
            lines.extend(indent_lines(render_type_lines(variant), "  "))
            if i < len(type_expr["variants"]) - 1:
                lines.append("  |")
        lines.append(f">{nullable}")
        return lines

    raise ValueError(f"Unsupported type kind: {kind}")


def render_type_gutter_lines(type_expr: dict[str, Any]) -> list[tuple[str, str]]:
    kind = type_expr["kind"]
    nullable = "?" if type_expr.get("nullable") else ""
    marker = gutter_marker(type_expr.get("change"))

    if kind in {"primitive", "ref", "enum"}:
        return [(marker, render_type_compact(type_expr))]

    if kind == "array":
        items = type_expr["items"]
        if is_compact_type(items):
            return [(marker, render_type_compact(type_expr))]
        inner = render_type_gutter_lines(items)
        lines = [(marker, "[")]
        lines.extend(indent_gutter_lines(inner, "  "))
        lines.append((marker, f"]{nullable}"))
        return lines

    if kind == "object":
        fields = type_expr.get("fields", [])
        lines: list[tuple[str, str]] = [(marker, "{")]
        for i, field in enumerate(fields):
            lines.extend(render_field_gutter_lines(field, "  ", is_last=i == len(fields) - 1))
        lines.append((marker, f'}}{nullable}'))
        return lines

    if kind == "sum":
        if is_compact_type(type_expr):
            return [(marker, render_type_compact(type_expr))]
        lines: list[tuple[str, str]] = [(marker, "<")]
        for i, variant in enumerate(type_expr["variants"]):
            lines.extend(indent_gutter_lines(render_type_gutter_lines(variant), "  "))
            if i < len(type_expr["variants"]) - 1:
                lines.append((marker, "  |"))
        lines.append((marker, f">{nullable}"))
        return lines

    raise ValueError(f"Unsupported type kind: {kind}")


def render_body_lines(body: dict[str, Any]) -> list[str]:
    if body["kind"] == "none":
        return ["none"]
    if body["kind"] == "type":
        return render_type_lines(body["type"])
    if body["kind"] == "multipart":
        lines = [body.get("contentType", "multipart/form-data")]
        for part in body["parts"]:
            part_lines = attach_prefix(
                prefix=f'{change_prefix(part.get("change"))}{part["name"]}: ',
                lines=render_type_lines(part["type"]),
                comment=part.get("description"),
            )
            lines.extend(indent_lines(part_lines, "  "))
        return lines
    raise ValueError(f'Unsupported body kind: {body["kind"]}')


def render_body_gutter_lines(body: dict[str, Any]) -> list[tuple[str, str]]:
    if body["kind"] == "none":
        return [(gutter_marker(body.get("change")), "none")]
    if body["kind"] == "type":
        return render_type_gutter_lines(body["type"])
    if body["kind"] == "multipart":
        lines: list[tuple[str, str]] = [(gutter_marker(body.get("change")), body.get("contentType", "multipart/form-data"))]
        for part in body["parts"]:
            part_lines = attach_gutter_prefix(
                prefix=f'{part["name"]}: ',
                lines=render_type_gutter_lines(part["type"]),
                marker=gutter_marker(part.get("change")),
                comment=part.get("description"),
            )
            lines.extend(indent_gutter_lines(part_lines, "  "))
        return lines
    raise ValueError(f'Unsupported body kind: {body["kind"]}')


def render_header_line(header: dict[str, Any], indent: str) -> str:
    return f'{indent}{change_prefix(header.get("change"))}{header["name"]}: {render_type_compact(header["type"])}{render_comment(header.get("description"))}'


def render_header_gutter_line(header: dict[str, Any], indent: str) -> tuple[str, str]:
    return gutter_marker(header.get("change")), f'{indent}{header["name"]}: {render_type_compact(header["type"])}{render_comment(header.get("description"))}'


def render_request_block(request: dict[str, Any]) -> list[str]:
    lines = [">"]
    has_headers = bool(request.get("headers"))
    has_body = "body" in request

    if has_headers:
        lines.append("  Headers:")
        for header in request["headers"]:
            lines.append(render_header_line(header, "    "))

    if has_headers and has_body:
        lines.append("")

    if has_body:
        lines.append("  Body:")
        lines.extend(indent_lines(render_body_lines(request["body"]), "    "))

    if not has_headers and not has_body:
        lines.append("  Body:")
        lines.append("    none")

    return lines


def render_request_gutter_block(request: dict[str, Any]) -> list[tuple[str, str]]:
    lines: list[tuple[str, str]] = [(gutter_marker(request.get("change")), ">")]
    has_headers = bool(request.get("headers"))
    has_body = "body" in request

    if has_headers:
        lines.append((EMPTY_GUTTER, "  Headers:"))
        for header in request["headers"]:
            lines.append(render_header_gutter_line(header, "    "))

    if has_headers and has_body:
        lines.append((EMPTY_GUTTER, ""))

    if has_body:
        lines.append((EMPTY_GUTTER, "  Body:"))
        lines.extend(indent_gutter_lines(render_body_gutter_lines(request["body"]), "    "))

    if not has_headers and not has_body:
        lines.append((EMPTY_GUTTER, "  Body:"))
        lines.append((EMPTY_GUTTER, "    none"))

    return lines


def render_status_line(response: dict[str, Any]) -> str:
    return f'  {change_prefix(response.get("change"))}{response["status"]}{render_comment(response.get("description"))}'


def render_status_gutter_line(response: dict[str, Any]) -> tuple[str, str]:
    return gutter_marker(response.get("change")), f'  {response["status"]}{render_comment(response.get("description"))}'


def render_response_block(responses: list[dict[str, Any]]) -> list[str]:
    lines = ["<"]
    for i, response in enumerate(responses):
        if i > 0:
            lines.append("")
        lines.append(render_status_line(response))
        headers = response.get("headers") or []
        body = response["body"]
        if headers:
            lines.append("    Headers:")
            for header in headers:
                lines.append(render_header_line(header, "      "))
            lines.append("")
            lines.append("    Body:")
            lines.extend(indent_lines(render_body_lines(body), "      "))
        else:
            lines.extend(indent_lines(render_body_lines(body), "    "))
    return lines


def render_response_gutter_block(responses: list[dict[str, Any]]) -> list[tuple[str, str]]:
    lines: list[tuple[str, str]] = [(EMPTY_GUTTER, "<")]
    for i, response in enumerate(responses):
        if i > 0:
            lines.append((EMPTY_GUTTER, ""))
        lines.append(render_status_gutter_line(response))
        headers = response.get("headers") or []
        body = response["body"]
        if headers:
            lines.append((EMPTY_GUTTER, "    Headers:"))
            for header in headers:
                lines.append(render_header_gutter_line(header, "      "))
            lines.append((EMPTY_GUTTER, ""))
            lines.append((EMPTY_GUTTER, "    Body:"))
            lines.extend(indent_gutter_lines(render_body_gutter_lines(body), "      "))
        else:
            lines.extend(indent_gutter_lines(render_body_gutter_lines(body), "    "))
    return lines


def render_rules_block(rules: list[dict[str, Any]]) -> list[str]:
    lines = ["Rules:"]
    for rule in rules:
        lines.append(f'  - {change_prefix(rule.get("change"))}{rule["text"]}')
    return lines


def render_rules_gutter_block(rules: list[dict[str, Any]]) -> list[tuple[str, str]]:
    lines: list[tuple[str, str]] = [(EMPTY_GUTTER, "Rules:")]
    for rule in rules:
        lines.append((gutter_marker(rule.get("change")), f'  - {rule["text"]}'))
    return lines


def render_typed_path(path: str, path_params: list[dict[str, Any]]) -> str:
    result = path
    for param in path_params:
        name = param["name"]
        marker = CHANGE_MARKERS[param["change"]] if param.get("change") in CHANGE_MARKERS else ""
        type_repr = render_type_compact(param["type"])
        replacement = "{" + f"{marker}{name}={type_repr}" + "}"
        result = result.replace("{" + name + "}", replacement)
    return result


def render_typed_path_gutter(path: str, path_params: list[dict[str, Any]]) -> str:
    result = path
    for param in path_params:
        name = param["name"]
        type_repr = render_type_compact(param["type"])
        replacement = "{" + f"{name}={type_repr}" + "}"
        result = result.replace("{" + name + "}", replacement)
    return result


def render_query_param_line(param: dict[str, Any], is_last: bool) -> str:
    suffix = "" if is_last else "&"
    content = f'{param["name"]}={{{render_type_compact(param["type"])}}}{suffix}{render_comment(param.get("description"))}'
    if param.get("change") in CHANGE_MARKERS:
        return f'  {CHANGE_MARKERS[param["change"]]} {content}'
    return f'    {content}'


def render_query_param_gutter_line(param: dict[str, Any], is_last: bool) -> tuple[str, str]:
    suffix = "" if is_last else "&"
    return gutter_marker(param.get("change")), f'    {param["name"]}={{{render_type_compact(param["type"])}}}{suffix}{render_comment(param.get("description"))}'


def render_endpoint_code_block(endpoint: dict[str, Any]) -> list[str]:
    path = render_typed_path(endpoint["path"], endpoint.get("pathParams", []))
    query_params = endpoint.get("queryParams", [])
    method_line = f'{change_prefix(endpoint.get("change"))}Method {endpoint["method"]} {path}{"?" if query_params else ""}'
    lines = [method_line]
    for i, param in enumerate(query_params):
        lines.append(render_query_param_line(param, is_last=i == len(query_params) - 1))
    if endpoint.get("request"):
        lines.append("")
        lines.extend(render_request_block(endpoint["request"]))
    lines.append("")
    lines.extend(render_response_block(endpoint["responses"]))
    if endpoint.get("rules"):
        lines.append("")
        lines.extend(render_rules_block(endpoint["rules"]))
    return lines


def render_endpoint_gutter_code_block(endpoint: dict[str, Any]) -> list[str]:
    path_params = endpoint.get("pathParams", [])
    path = render_typed_path_gutter(endpoint["path"], path_params)
    query_params = endpoint.get("queryParams", [])
    method_marker = gutter_marker(endpoint.get("change"))
    if method_marker == EMPTY_GUTTER and any(param.get("change") in CHANGE_MARKERS for param in path_params):
        method_marker = CHANGE_MARKERS["changed"]
    lines: list[tuple[str, str]] = [(method_marker, f'Method {endpoint["method"]} {path}{"?" if query_params else ""}')]
    for i, param in enumerate(query_params):
        lines.append(render_query_param_gutter_line(param, is_last=i == len(query_params) - 1))
    if endpoint.get("request"):
        lines.append((EMPTY_GUTTER, ""))
        lines.extend(render_request_gutter_block(endpoint["request"]))
    lines.append((EMPTY_GUTTER, ""))
    lines.extend(render_response_gutter_block(endpoint["responses"]))
    if endpoint.get("rules"):
        lines.append((EMPTY_GUTTER, ""))
        lines.extend(render_rules_gutter_block(endpoint["rules"]))
    return format_gutter_lines(lines)


def render_model_code_block(model: dict[str, Any]) -> list[str]:
    return [f'Model {model["name"]} =', "", *render_type_lines({"kind": "object", "fields": model["fields"]})]


def render_model_gutter_code_block(model: dict[str, Any]) -> list[str]:
    return format_gutter_lines([
        (gutter_marker(model.get("change")), f'Model {model["name"]} ='),
        (EMPTY_GUTTER, ""),
        *render_type_gutter_lines({"kind": "object", "fields": model["fields"]}),
    ])


def render_sum_type_lines(sum_type: dict[str, Any]) -> list[str]:
    variants = [render_sum_variant_compact(variant) for variant in sum_type["variants"]]
    lines = [f'Model {sum_type["name"]} =', ""]
    for i, variant in enumerate(variants):
        suffix = " |" if i < len(variants) - 1 else ""
        lines.append(f'  {variant}{suffix}')
    return lines


def render_sum_type_gutter_lines(sum_type: dict[str, Any]) -> list[str]:
    variants = [render_sum_variant_compact(variant) for variant in sum_type["variants"]]
    lines: list[tuple[str, str]] = [
        (gutter_marker(sum_type.get("change")), f'Model {sum_type["name"]} ='),
        (EMPTY_GUTTER, ""),
    ]
    for i, variant in enumerate(variants):
        suffix = " |" if i < len(variants) - 1 else ""
        lines.append((EMPTY_GUTTER, f'  {variant}{suffix}'))
    return format_gutter_lines(lines)


def render_enum_code_block(enum_block: dict[str, Any]) -> list[str]:
    lines = [f'Enum {enum_block["name"]}']
    for item in enum_block["items"]:
        line = f'  {change_prefix(item.get("change"))}{item["name"]}'
        if item.get("description"):
            line += render_comment(item["description"])
        lines.append(line)
    return lines


def render_enum_gutter_code_block(enum_block: dict[str, Any]) -> list[str]:
    lines: list[tuple[str, str]] = [(gutter_marker(enum_block.get("change")), f'Enum {enum_block["name"]}')]
    for item in enum_block["items"]:
        line = f'  {item["name"]}'
        if item.get("description"):
            line += render_comment(item["description"])
        lines.append((gutter_marker(item.get("change")), line))
    return format_gutter_lines(lines)


def render_shared_notes_code_block(notes: list[dict[str, Any]]) -> list[str]:
    return [f'{change_prefix(note.get("change"))}{note["text"]}' for note in notes] or ["none"]


def render_shared_notes_gutter_code_block(notes: list[dict[str, Any]]) -> list[str]:
    if not notes:
        return ["none"]
    return format_gutter_lines([(gutter_marker(note.get("change")), note["text"]) for note in notes])


def fenced_block(lines: list[str]) -> list[str]:
    return ["```text", *(lines or ["none"]), "```"]


def paired_block(title: str, before_lines: list[str], after_lines: list[str]) -> str:
    return "\n".join([
        title,
        "",
        f"### {BEFORE_TITLE}",
        "",
        *fenced_block(before_lines),
        "",
        f"### {AFTER_TITLE}",
        "",
        *fenced_block(after_lines),
    ])




def annotate_with_change(node: Any, change: str) -> Any:
    if isinstance(node, dict):
        out = {key: annotate_with_change(value, change) for key, value in node.items()}
        out["change"] = change
        return out
    if isinstance(node, list):
        return [annotate_with_change(item, change) for item in node]
    return node


def item_identity(item: Any) -> str | None:
    if not isinstance(item, dict):
        return None
    for key in ("id", "name", "text"):
        value = item.get(key)
        if isinstance(value, str) and value:
            return f"{key}:{value}"
    method = item.get("method")
    path = item.get("path")
    if isinstance(method, str) and method and isinstance(path, str) and path:
        return f"endpoint:{method} {path}"
    return None


def annotate_list_pair(before: list[Any], after: list[Any]) -> tuple[list[Any], list[Any]]:
    before_by_key: dict[str, Any] = {}
    after_by_key: dict[str, Any] = {}
    before_order: list[str | tuple[str, int]] = []
    after_order: list[str | tuple[str, int]] = []

    for index, item in enumerate(before):
        key = item_identity(item) or ("index", index)
        before_by_key[key] = item
        before_order.append(key)
    for index, item in enumerate(after):
        key = item_identity(item) or ("index", index)
        after_by_key[key] = item
        after_order.append(key)

    ordered_keys: list[Any] = []
    seen: set[Any] = set()
    for key in [*before_order, *after_order]:
        if key not in seen:
            seen.add(key)
            ordered_keys.append(key)

    before_out: list[Any] = []
    after_out: list[Any] = []
    for key in ordered_keys:
        has_before = key in before_by_key
        has_after = key in after_by_key
        if has_before and has_after:
            b, a = annotate_pair(before_by_key[key], after_by_key[key])
            if (
                isinstance(key, tuple)
                and key[:1] == ("index",)
                and isinstance(b, dict)
                and isinstance(a, dict)
                and b.get("change") == "not-changed"
                and a.get("change") == "not-changed"
            ):
                b = dict(b)
                a = dict(a)
                b["change"] = "changed"
                a["change"] = "changed"
            before_out.append(b)
            after_out.append(a)
        elif has_before:
            before_out.append(annotate_with_change(before_by_key[key], "removed"))
        else:
            after_out.append(annotate_with_change(after_by_key[key], "added"))
    return before_out, after_out


def annotate_pair(before: Any, after: Any) -> tuple[Any, Any]:
    if isinstance(before, dict) and isinstance(after, dict):
        keys = set(before) | set(after)
        before_out: dict[str, Any] = {}
        after_out: dict[str, Any] = {}
        changed = False
        for key in keys:
            if key == "change":
                continue
            if key in before and key in after:
                b, a = annotate_pair(before[key], after[key])
                before_out[key] = b
                after_out[key] = a
                if isinstance(b, dict) and b.get("change") != "not-changed":
                    changed = True
                elif isinstance(a, dict) and a.get("change") != "not-changed":
                    changed = True
                elif b != a:
                    changed = True
            elif key in before:
                before_out[key] = annotate_with_change(before[key], "removed")
                changed = True
            else:
                after_out[key] = annotate_with_change(after[key], "added")
                changed = True
        change = "changed" if changed else "not-changed"
        before_out["change"] = change
        after_out["change"] = change
        return before_out, after_out

    if isinstance(before, list) and isinstance(after, list):
        return annotate_list_pair(before, after)

    if before == after:
        return before, after

    return annotate_with_change(before, "changed"), annotate_with_change(after, "changed")


def ordered_definitions(doc: dict[str, Any] | None) -> list[tuple[str, dict[str, Any]]]:
    if not doc:
        return []
    definitions: list[tuple[str, dict[str, Any]]] = []
    definitions.extend(("model", item) for item in doc.get("models", []))
    definitions.extend(("sumType", item) for item in doc.get("sumTypes", []))
    definitions.extend(("enum", item) for item in doc.get("enums", []))
    return definitions


def definition_pair_key(kind: str, definition: dict[str, Any]) -> tuple[str, str]:
    return kind, str(definition.get("id") or definition.get("name") or "")


def normalize_pair_document(doc: dict[str, Any]) -> tuple[dict[str, Any], dict[str, Any]]:
    before = project(doc, "before", preserve_meta=False)
    after = project(doc, "after", preserve_meta=False)
    return annotate_pair(before, after)


def render_paired_document(doc: dict[str, Any]) -> str:
    before_doc, after_doc = normalize_pair_document(doc)
    parts: list[str] = [f'# {after_doc.get("title", doc.get("title", "API"))}']

    before_endpoints = before_doc.get("endpoints", [])
    after_endpoints = after_doc.get("endpoints", [])
    for index, endpoint in enumerate(after_endpoints):
        before_endpoint = before_endpoints[index] if index < len(before_endpoints) else None
        parts.append(render_endpoint_block(endpoint, paired=True, before_endpoint=before_endpoint))

    before_defs = {definition_pair_key(kind, definition): definition for kind, definition in ordered_definitions(before_doc)}
    for kind, definition in ordered_definitions(after_doc):
        before_definition = before_defs.get(definition_pair_key(kind, definition))
        if kind == "model":
            parts.append(render_model_block(definition, paired=True, before_model=before_definition))
        elif kind == "sumType":
            parts.append(render_sum_type_block(definition, paired=True, before_sum_type=before_definition))
        else:
            parts.append(render_enum_block(definition, paired=True, before_enum=before_definition))

    shared_notes = render_shared_notes(
        after_doc.get("sharedNotes", []),
        paired=True,
        before_notes=before_doc.get("sharedNotes", []),
    )
    if shared_notes:
        parts.append(shared_notes)
    return "\n\n".join(parts) + "\n"

def render_model_block(
    model: dict[str, Any],
    paired: bool,
    marked: bool = False,
    before_model: dict[str, Any] | None = None,
) -> str:
    title = f'## Model {model["name"]}'
    if paired:
        before_lines = render_model_gutter_code_block(before_model) if before_model else ["none"]
        after_lines = render_model_gutter_code_block(model) if model else ["none"]
        return paired_block(title, before_lines, after_lines)
    code_block = render_model_gutter_code_block(model) if marked else render_model_code_block(model)
    return "\n".join([title, "", *fenced_block(code_block)])


def render_sum_type_block(
    sum_type: dict[str, Any],
    paired: bool,
    marked: bool = False,
    before_sum_type: dict[str, Any] | None = None,
) -> str:
    title = f'## Model {sum_type["name"]}'
    if paired:
        before_lines = render_sum_type_gutter_lines(before_sum_type) if before_sum_type else ["none"]
        after_lines = render_sum_type_gutter_lines(sum_type) if sum_type else ["none"]
        return paired_block(title, before_lines, after_lines)
    code_block = render_sum_type_gutter_lines(sum_type) if marked else render_sum_type_lines(sum_type)
    return "\n".join([title, "", *fenced_block(code_block)])


def render_enum_block(
    enum_block: dict[str, Any],
    paired: bool,
    marked: bool = False,
    before_enum: dict[str, Any] | None = None,
) -> str:
    title = f'## Enum {enum_block["name"]}'
    if paired:
        before_lines = render_enum_gutter_code_block(before_enum) if before_enum else ["none"]
        after_lines = render_enum_gutter_code_block(enum_block) if enum_block else ["none"]
        return paired_block(title, before_lines, after_lines)
    code_block = render_enum_gutter_code_block(enum_block) if marked else render_enum_code_block(enum_block)
    return "\n".join([title, "", *fenced_block(code_block)])


def render_shared_notes(
    notes: list[dict[str, Any]],
    paired: bool,
    marked: bool = False,
    before_notes: list[dict[str, Any]] | None = None,
) -> str:
    if not notes:
        return ""
    if paired:
        before_lines = render_shared_notes_gutter_code_block(before_notes or []) if before_notes is not None else ["none"]
        after_lines = render_shared_notes_gutter_code_block(notes) if notes else ["none"]
        return paired_block("## Shared Notes", before_lines, after_lines)
    code_block = render_shared_notes_gutter_code_block(notes) if marked else render_shared_notes_code_block(notes)
    return "\n".join(["## Shared Notes", "", *fenced_block(code_block)])


def render_endpoint_block(
    endpoint: dict[str, Any],
    paired: bool,
    marked: bool = False,
    before_endpoint: dict[str, Any] | None = None,
) -> str:
    title = f'## Method {endpoint["method"]} {endpoint["path"]}'
    if paired:
        before_lines = render_endpoint_gutter_code_block(before_endpoint) if before_endpoint else ["none"]
        after_lines = render_endpoint_gutter_code_block(endpoint) if endpoint else ["none"]
        return paired_block(title, before_lines, after_lines)
    code_block = render_endpoint_gutter_code_block(endpoint) if marked else render_endpoint_code_block(endpoint)
    return "\n".join([title, "", *fenced_block(code_block)])


def render_plain_document(doc: dict[str, Any], paired: bool, marked: bool = False) -> str:
    parts: list[str] = [f'# {doc.get("title", "API")}']
    for endpoint in doc.get("endpoints", []):
        parts.append(render_endpoint_block(endpoint, paired=paired, marked=marked))
    for model in doc.get("models", []):
        parts.append(render_model_block(model, paired=paired, marked=marked))
    for sum_type in doc.get("sumTypes", []):
        parts.append(render_sum_type_block(sum_type, paired=paired, marked=marked))
    for enum_block in doc.get("enums", []):
        parts.append(render_enum_block(enum_block, paired=paired, marked=marked))
    shared_notes = render_shared_notes(doc.get("sharedNotes", []), paired=paired, marked=marked)
    if shared_notes:
        parts.append(shared_notes)
    return "\n\n".join(parts) + "\n"


def resolve_render_mode(doc: dict[str, Any], diff_format: str) -> str:
    if diff_format != "auto":
        return diff_format
    if doc.get("changeMode") == "none":
        return "none"
    return "marked"


def render_document(doc: dict[str, Any], diff_format: str) -> str:
    mode = resolve_render_mode(doc, diff_format)
    if mode == "paired":
        return render_paired_document(doc)
    if mode == "none":
        return render_plain_document(project(doc, "after", preserve_meta=False), paired=False, marked=False)
    return render_plain_document(doc, paired=False, marked=True)


def main() -> int:
    parser = argparse.ArgumentParser(description="Render REST API IR JSON to Markdown.")
    parser.add_argument("input", type=Path, help="Path to IR JSON file")
    parser.add_argument("output", type=Path, nargs="?", help="Output Markdown path. Defaults to stdout.")
    parser.add_argument(
        "--diff-format",
        choices=["auto", "none", "marked", "paired"],
        default="auto",
        help="How to render changes. 'auto' uses document.changeMode.",
    )
    args = parser.parse_args()
    doc = load_json(args.input)
    markdown = render_document(doc, diff_format=args.diff_format)
    if args.output:
        args.output.write_text(markdown, encoding="utf-8")
    else:
        print(markdown, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
