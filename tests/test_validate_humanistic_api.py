import importlib.util
from pathlib import Path

import pytest


def _load_validator_module():
    script_path = (
        Path(__file__).resolve().parents[1]
        / "src/artifacts/humanistic-api-v1/scripts/validate_humanistic_api.py"
    )
    spec = importlib.util.spec_from_file_location("validate_humanistic_api", script_path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


@pytest.mark.parametrize("fixture_name", ["valid.md", "valid.adoc"])
def test_accepts_humanistic_api_source_blocks(fixture_name: str):
    fixture = (
        Path(__file__).resolve().parent
        / "fixtures/artifacts/humanistic-api-v1"
        / fixture_name
    )

    errors = _load_validator_module().validate_document(fixture.read_text(encoding="utf-8"))

    assert errors == []


def test_ignores_surrounding_document_but_rejects_invalid_source_block():
    fixture = (
        Path(__file__).resolve().parent
        / "fixtures/artifacts/humanistic-api-v1/invalid.md"
    )

    errors = _load_validator_module().validate_document(fixture.read_text(encoding="utf-8"))

    assert errors == ["line 4: source block must start with Method, Model, or Enum"]


def test_rejects_unclosed_source_block():
    errors = _load_validator_module().validate_document("```text\nModel User =\n")

    assert errors == ["line 1: unclosed Markdown text fence"]
