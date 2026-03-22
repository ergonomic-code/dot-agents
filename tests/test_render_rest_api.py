import importlib.util
import json
from pathlib import Path

import pytest


def _load_renderer_module():
    script_path = Path(__file__).resolve().parents[1] / "src/skills/describing-rest-api/scripts/render_rest_api.py"
    spec = importlib.util.spec_from_file_location("render_rest_api", script_path)
    module = importlib.util.module_from_spec(spec)
    assert spec is not None and spec.loader is not None
    spec.loader.exec_module(module)
    return module


@pytest.mark.parametrize(
    ("input_fixture", "expected_fixture"),
    [
        ("marked-model-block-gutter.json", "marked-model-block-gutter.expected.md"),
    ],
    ids=[
        "рендерер должен рендерить маркер изменения блока внутри text-блока в diff mode",
    ],
)
def test_render_rest_api_marked_diff(input_fixture: str, expected_fixture: str):
    fixtures_dir = Path(__file__).resolve().parents[1] / "tests/fixtures/skills/describing-rest-api"
    fixture_path = fixtures_dir / input_fixture
    doc = json.loads(fixture_path.read_text(encoding="utf-8"))
    expected = (fixtures_dir / expected_fixture).read_text(encoding="utf-8")

    renderer = _load_renderer_module()
    rendered = renderer.render_document(doc, diff_format="marked")

    assert rendered == expected


@pytest.mark.parametrize(
    ("input_fixture", "expected_fixture"),
    [
        ("pair-before-removed.json", "pair-before-removed.expected.md"),
        ("pair-multipart-request.json", "pair-multipart-request.expected.md"),
    ],
    ids=[
        "рендерер должен рендерить маркеры изменения блока в diff mode, даже если в исходном IR поле явно не помечено как removed",
        "рендерер должен рендерить multipart body в paired diff mode",
    ],
)
def test_render_rest_api_paired_diff(input_fixture: str, expected_fixture: str):
    fixtures_dir = Path(__file__).resolve().parents[1] / "tests/fixtures/skills/describing-rest-api"
    fixture_path = fixtures_dir / input_fixture
    doc = json.loads(fixture_path.read_text(encoding="utf-8"))
    expected = (fixtures_dir / expected_fixture).read_text(encoding="utf-8")

    renderer = _load_renderer_module()
    rendered = renderer.render_document(doc, diff_format="paired")

    assert rendered == expected
