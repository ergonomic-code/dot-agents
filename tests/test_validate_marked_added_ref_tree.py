import importlib.util
import json
from pathlib import Path


def _load_validator_module():
    script_path = Path(__file__).resolve().parents[1] / "src/skills/describing-rest-api/scripts/validate_json.py"
    spec = importlib.util.spec_from_file_location("validate_json", script_path)
    module = importlib.util.module_from_spec(spec)
    assert spec is not None and spec.loader is not None
    spec.loader.exec_module(module)
    return module


def _load_fixture(name: str) -> object:
    fixtures_dir = Path(__file__).resolve().parents[1] / "tests/fixtures/skills/describing-rest-api"
    return json.loads((fixtures_dir / name).read_text(encoding="utf-8"))


def test_validate_marked_added_ref_tree_requires_added_markers():
    validator = _load_validator_module()
    document = _load_fixture("marked-invalid-added-ref-tree-without-change.json")

    errors = validator.validate_marked_added_ref_targets(document)

    assert errors == [
        (
            "$.sumTypes[0].change",
            "missing required change='added' for block referenced only from added content",
        ),
        (
            "$.models[1].change",
            "missing required change='added' for block reachable only from added content",
        ),
        (
            "$.models[2].change",
            "missing required change='added' for block reachable only from added content",
        ),
    ]