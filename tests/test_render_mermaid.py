import importlib.util
from pathlib import Path


def _load_renderer_module():
    script_path = (
        Path(__file__).resolve().parents[1]
        / "src/artifacts/structure-chart-v1/scripts/render_mermaid.py"
    )
    spec = importlib.util.spec_from_file_location("render_mermaid", script_path)
    module = importlib.util.module_from_spec(spec)
    assert spec is not None and spec.loader is not None
    spec.loader.exec_module(module)
    return module


def test_render_document_nests_modules_and_lambda_in_their_direct_owners():
    renderer = _load_renderer_module()
    document = {
        "modules": [
            {"id": "root", "title": "Root"},
            {"id": "child", "title": "Child", "parent": "root"},
            {"id": "leaf", "title": "Leaf", "parent": "child"},
        ],
        "lambdas": [
            {"id": "child_lambda", "title": "Child lambda", "owner": "child"},
        ],
        "calls": [],
    }

    rendered = renderer.render_document(document)

    assert rendered.splitlines()[1:] == [
        "flowchart LR",
        '    subgraph root["Root"]',
        '        subgraph child["Child"]',
        '            leaf["Leaf"]',
        '            child_lambda["λ Child lambda"]',
        "        end",
        "    end",
        "",
        "    classDef lambda fill:#f7f2ff,stroke:#8a63ff,stroke-width:1px;",
        "    class child_lambda lambda;",
    ]
