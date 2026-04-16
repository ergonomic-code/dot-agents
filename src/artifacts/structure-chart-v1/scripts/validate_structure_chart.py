#!/usr/bin/env python3

from __future__ import annotations

import argparse
import json
from collections import Counter, defaultdict
from pathlib import Path
import sys

import yaml
from jsonschema import Draft202012Validator


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Validate structure-chart/v1 YAML against schema and semantic rules."
    )
    default_schema = (
        Path(__file__).resolve().parent.parent / "references" / "structure-chart-v1.schema.json"
    )
    parser.add_argument("document", help="Path to structure chart YAML or JSON.")
    parser.add_argument(
        "--schema",
        default=str(default_schema),
        help="Path to structure-chart/v1 JSON schema.",
    )
    return parser.parse_args()


def load_yaml_or_json(path: Path) -> object:
    with path.open("r", encoding="utf-8") as handle:
        if path.suffix.lower() == ".json":
            return json.load(handle)
        return yaml.safe_load(handle)


def make_path(path: list[object]) -> str:
    if not path:
        return "$"
    parts = ["$"]
    for part in path:
        if isinstance(part, int):
            parts.append(f"[{part}]")
        else:
            parts.append(f".{part}")
    return "".join(parts)


def flow_item_label(item: dict[str, object]) -> str:
    if "data" in item:
        return str(item["data"])
    if "module" in item:
        return str(item["module"])
    return str(item["lambda"])


def ensure_tree(module_parents: dict[str, str | None], errors: list[str]) -> None:
    state: dict[str, int] = {}

    def visit(module_id: str, trail: list[str]) -> None:
        status = state.get(module_id, 0)
        if status == 1:
            cycle = " -> ".join(trail + [module_id])
            errors.append(f"Module hierarchy contains a cycle: {cycle}")
            return
        if status == 2:
            return

        state[module_id] = 1
        parent_id = module_parents[module_id]
        if parent_id is not None:
            visit(parent_id, trail + [module_id])
        state[module_id] = 2

    for module_id in module_parents:
        visit(module_id, [])


def is_ancestor(
    descendant_id: str,
    candidate_ancestor_id: str,
    module_parents: dict[str, str | None],
) -> bool:
    current = module_parents.get(descendant_id)
    while current is not None:
        if current == candidate_ancestor_id:
            return True
        current = module_parents.get(current)
    return False


def validate_document(document: object, schema: object) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []

    validator = Draft202012Validator(schema)
    for error in sorted(validator.iter_errors(document), key=lambda item: list(item.absolute_path)):
        errors.append(f"{make_path(list(error.absolute_path))}: {error.message}")

    if not isinstance(document, dict):
        return errors, warnings

    modules = document.get("modules", [])
    lambdas = document.get("lambdas", [])
    calls = document.get("calls", [])

    if not isinstance(modules, list) or not isinstance(lambdas, list) or not isinstance(calls, list):
        return errors, warnings

    module_ids: list[str] = []
    lambda_ids: list[str] = []
    module_parents: dict[str, str | None] = {}

    for module in modules:
        if not isinstance(module, dict) or "id" not in module:
            continue
        module_id = str(module["id"])
        module_ids.append(module_id)
        module_parents[module_id] = module.get("parent")
        code_ref = module.get("code")
        if not isinstance(code_ref, dict) or "path" not in code_ref or "line" not in code_ref:
            warnings.append(f"Module {module_id} has no code.path/code.line reference.")

    for lambda_item in lambdas:
        if not isinstance(lambda_item, dict) or "id" not in lambda_item:
            continue
        lambda_id = str(lambda_item["id"])
        lambda_ids.append(lambda_id)
        code_ref = lambda_item.get("code")
        if not isinstance(code_ref, dict) or "path" not in code_ref or "line" not in code_ref:
            warnings.append(f"Lambda {lambda_id} has no code.path/code.line reference.")

    id_counts = Counter(module_ids + lambda_ids)
    for item_id, count in sorted(id_counts.items()):
        if count > 1:
            errors.append(f"Duplicate identifier in global namespace: {item_id}")

    module_id_set = set(module_ids)
    global_id_set = set(module_ids + lambda_ids)

    for module in modules:
        if not isinstance(module, dict) or "id" not in module:
            continue
        module_id = str(module["id"])
        parent_id = module.get("parent")
        if parent_id is None:
            continue
        if not isinstance(parent_id, str) or parent_id not in module_id_set:
            errors.append(f"Module {module_id} references missing parent module: {parent_id}")

    ensure_tree(module_parents, errors)

    for lambda_item in lambdas:
        if not isinstance(lambda_item, dict) or "id" not in lambda_item:
            continue
        lambda_id = str(lambda_item["id"])
        owner_id = lambda_item.get("owner")
        if not isinstance(owner_id, str) or owner_id not in module_id_set:
            errors.append(f"Lambda {lambda_id} references missing owner module: {owner_id}")

    call_pairs: Counter[tuple[str, str]] = Counter()
    incoming_counts: Counter[str] = Counter()
    outgoing_counts: Counter[str] = Counter()

    for index, call in enumerate(calls):
        if not isinstance(call, dict):
            continue

        from_id = call.get("from")
        to_id = call.get("to")
        if not isinstance(from_id, str) or from_id not in global_id_set:
            errors.append(f"Call #{index} has unknown 'from' reference: {from_id}")
            continue
        if not isinstance(to_id, str) or to_id not in global_id_set:
            errors.append(f"Call #{index} has unknown 'to' reference: {to_id}")
            continue

        call_pairs[(from_id, to_id)] += 1
        incoming_counts[to_id] += 1
        outgoing_counts[from_id] += 1

        for field in ("in", "out"):
            items = call.get(field, [])
            if not isinstance(items, list):
                continue
            labels = [flow_item_label(item) for item in items if isinstance(item, dict)]
            repeated = sorted(name for name, count in Counter(labels).items() if count > 1)
            if repeated:
                warnings.append(
                    f"Call {from_id} -> {to_id} repeats flow items in '{field}': {', '.join(repeated)}"
                )

            for item in items:
                if not isinstance(item, dict):
                    continue
                if "module" in item and item["module"] not in module_id_set:
                    errors.append(
                        f"Call {from_id} -> {to_id} references unknown module in '{field}': {item['module']}"
                    )
                if "lambda" in item and item["lambda"] not in lambda_ids:
                    errors.append(
                        f"Call {from_id} -> {to_id} references unknown lambda in '{field}': {item['lambda']}"
                    )

        if not call.get("in") and not call.get("out") and "if" not in call and "loop" not in call:
            warnings.append(f"Call {from_id} -> {to_id} has no if/loop/in/out details.")

        if from_id in module_id_set and to_id in module_id_set:
            if is_ancestor(from_id, to_id, module_parents) and not call.get("notes"):
                warnings.append(
                    f"Call {from_id} -> {to_id} goes from child to ancestor without notes."
                )

    for (from_id, to_id), count in sorted(call_pairs.items()):
        if count > 1:
            errors.append(f"Duplicate call pair: {from_id} -> {to_id}")

    root_modules = {module_id for module_id, parent_id in module_parents.items() if parent_id is None}
    for module_id in module_ids:
        if module_id in root_modules:
            continue
        if incoming_counts[module_id] == 0 and outgoing_counts[module_id] == 0:
            warnings.append(f"Module {module_id} is isolated and not a root module.")

    for lambda_id in lambda_ids:
        if incoming_counts[lambda_id] == 0:
            warnings.append(f"Lambda {lambda_id} has no incoming call edges.")

    return errors, warnings


def main() -> int:
    args = parse_args()
    document_path = Path(args.document).resolve()
    schema_path = Path(args.schema).resolve()

    document = load_yaml_or_json(document_path)
    schema = load_yaml_or_json(schema_path)

    errors, warnings = validate_document(document, schema)

    if errors:
        print("Validation failed.", file=sys.stderr)
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        for warning in warnings:
            print(f"WARNING: {warning}", file=sys.stderr)
        return 1

    print("Validation passed.")
    for warning in warnings:
        print(f"WARNING: {warning}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
