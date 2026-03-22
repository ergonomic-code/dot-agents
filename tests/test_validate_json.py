import importlib.util
import json
from pathlib import Path

import pytest
from jsonschema import Draft202012Validator


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


def _fixture_path(name: str) -> Path:
    fixtures_dir = Path(__file__).resolve().parents[1] / "tests/fixtures/skills/describing-rest-api"
    return fixtures_dir / name


@pytest.mark.parametrize(
    ("fixture_name", "expected_errors"),
    [
        (
            "marked-invalid-missing-refid.json",
            [
                (
                    "$.endpoints[0].request.body.type.refId",
                    "missing required refId for marked-mode endpoint body (slot=request)",
                ),
            ],
        ),
        (
            "marked-invalid-slot-mismatch.json",
            [
                (
                    "$.endpoints",
                    "inconsistent refId for endpoint slot (POST /users/{}, request): ['A', 'B']",
                ),
            ],
        ),
    ],
    ids=[
        "валидатор отклоняет отсутствие request.body.type.refId",
        "валидатор отклоняет несовпадение refId в одном endpoint slot",
    ],
)
def test_validate_marked_ref_ids_invalid_cases(fixture_name: str, expected_errors: list[tuple[str, str]]):
    validator = _load_validator_module()
    document = _load_fixture(fixture_name)

    errors = validator.validate_marked_ref_ids(document)

    assert errors == expected_errors


def test_validate_marked_ref_ids_allows_rename_with_stable_refid():
    validator = _load_validator_module()
    document = _load_fixture("marked-valid-rename.json")

    errors = validator.validate_marked_ref_ids(document)

    assert errors == []


def test_validate_marked_block_changes_rejects_added_sum_type_without_change_marker():
    validator = _load_validator_module()
    document = _load_fixture("marked-invalid-added-sum-type-without-change.json")

    errors = validator.validate_marked_block_changes(document)

    assert errors == [
        (
            "$.sumTypes[0].change",
            "missing required change='added' for marked-mode block composed only of added refs",
        ),
    ]