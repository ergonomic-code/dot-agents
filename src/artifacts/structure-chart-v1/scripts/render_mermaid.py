#!/usr/bin/env python3

from __future__ import annotations

import argparse
import json
from collections import defaultdict
from pathlib import Path

import yaml


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Render Mermaid from structure-chart/v1 YAML.")
    parser.add_argument("document", help="Path to structure chart YAML or JSON.")
    return parser.parse_args()


def load_yaml_or_json(path: Path) -> dict[str, object]:
    with path.open("r", encoding="utf-8") as handle:
        if path.suffix.lower() == ".json":
            data = json.load(handle)
        else:
            data = yaml.safe_load(handle)
    if not isinstance(data, dict):
        raise TypeError("Structure chart document must be an object.")
    return data


def escape_label(value: str) -> str:
    return value.replace('"', "&quot;")


def flow_item_label(item: dict[str, object]) -> str:
    if "data" in item:
        return str(item["data"])
    if "module" in item:
        return str(item["module"])
    return str(item["lambda"])


def module_label(module: dict[str, object]) -> str:
    return str(module.get("title") or module["id"])


def lambda_label(lambda_item: dict[str, object]) -> str:
    parts = [f"λ {lambda_item.get('title') or lambda_item['id']}"]
    params = lambda_item.get("params") or []
    captures = lambda_item.get("captures") or []
    if params:
        parts.append(f"params: {', '.join(str(item) for item in params)}")
    if captures:
        parts.append(f"captures: {', '.join(str(item) for item in captures)}")
    return "<br/>".join(parts)


def edge_label(call: dict[str, object]) -> str:
    lines: list[str] = []
    if "if" in call and call["if"]:
        lines.append(f"if: {call['if']}")
    loop = call.get("loop")
    if isinstance(loop, dict) and loop.get("collection"):
        collection = str(loop["collection"])
        condition = loop.get("condition")
        if condition:
            lines.append(f"loop: {collection}, {condition}")
        else:
            lines.append(f"loop: {collection}")
    for field in ("in", "out"):
        items = call.get(field) or []
        if items:
            rendered = ", ".join(flow_item_label(item) for item in items if isinstance(item, dict))
            lines.append(f"{field}: {rendered}")
    return "<br/><br/>".join(lines)


def render_document(document: dict[str, object]) -> str:
    modules = document.get("modules") or []
    lambdas = document.get("lambdas") or []
    calls = document.get("calls") or []

    module_map = {
        str(module["id"]): module for module in modules if isinstance(module, dict) and "id" in module
    }
    module_order: list[str] = []
    module_parents: dict[str, str | None] = {}
    root_lambdas: dict[str, list[dict[str, object]]] = defaultdict(list)

    for module in modules:
        if not isinstance(module, dict) or "id" not in module:
            continue
        module_id = str(module["id"])
        module_order.append(module_id)
        parent_id = module.get("parent")
        module_parents[module_id] = parent_id if isinstance(parent_id, str) else None

    def top_ancestor(module_id: str) -> str:
        current = module_id
        while True:
            parent_id = module_parents.get(current)
            if parent_id is None:
                return current
            current = parent_id

    for lambda_item in lambdas:
        if not isinstance(lambda_item, dict) or "id" not in lambda_item or "owner" not in lambda_item:
            continue
        root_lambdas[top_ancestor(str(lambda_item["owner"]))].append(lambda_item)

    lines = [
        '%%{init: {"flowchart": {"nodeSpacing": 48, "rankSpacing": 72, "htmlLabels": true}, "themeCSS": ".edgeLabel rect, .edgeLabel .labelBkg { fill: transparent !important; stroke: transparent !important; } .edgeLabel p, .nodeLabel p, .label p { text-align: left !important; background: transparent !important; line-height: 1.35; }"}}%%',
        "flowchart LR",
    ]

    def emit_root(module_id: str, indent: str) -> None:
        module = module_map[module_id]
        lambda_items = root_lambdas.get(module_id, [])
        label = escape_label(module_label(module))

        if lambda_items:
            lines.append(f'{indent}subgraph {module_id}["{label}"]')
            for lambda_item in lambda_items:
                lambda_id = str(lambda_item["id"])
                lambda_text = escape_label(lambda_label(lambda_item))
                lines.append(f'{indent}    {lambda_id}["{lambda_text}"]')
            lines.append(f"{indent}end")
            return

        lines.append(f'{indent}{module_id}["{label}"]')

    for module_id in module_order:
        if module_parents.get(module_id) is None:
            emit_root(module_id, "    ")
            continue
        module = module_map[module_id]
        label = escape_label(module_label(module))
        lines.append(f'    {module_id}["{label}"]')

    if calls:
        lines.append("")

    for call in calls:
        if not isinstance(call, dict):
            continue
        from_id = str(call["from"])
        to_id = str(call["to"])
        label = edge_label(call)
        if label:
            lines.append(f'    {from_id} -->|"{escape_label(label)}"| {to_id}')
        else:
            lines.append(f"    {from_id} --> {to_id}")

    lambda_ids = [str(item["id"]) for item in lambdas if isinstance(item, dict) and "id" in item]
    if lambda_ids:
        lines.append("")
        lines.append("    classDef lambda fill:#f7f2ff,stroke:#8a63ff,stroke-width:1px;")
        lines.append(f"    class {','.join(lambda_ids)} lambda;")

    return "\n".join(lines) + "\n"


def main() -> int:
    args = parse_args()
    document = load_yaml_or_json(Path(args.document).resolve())
    print(render_document(document), end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
