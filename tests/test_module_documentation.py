import re
import runpy
from pathlib import Path


ROOT = Path(__file__).parents[1]


def test_module_catalog_is_canonical_entry_point():
    catalog = (ROOT / "docs" / "modules.md").read_text(encoding="utf-8")
    installer = (
        ROOT / "bootstrap" / "skills" / "installing-framework" / "SKILL.md"
    ).read_text(encoding="utf-8")
    readme = (ROOT / "README.md").read_text(encoding="utf-8")

    assert "../../../docs/modules.md" in installer
    assert "канонический каталог" in installer
    assert "docs/modules.md" in readme
    assert "## Выбираемые модули" in catalog


def test_module_catalog_matches_selectable_modules():
    catalog = (ROOT / "docs" / "modules.md").read_text(encoding="utf-8")
    selectable = runpy.run_path(
        str(ROOT / "bootstrap" / "hooks" / "session_start_load_project_baseline.py")
    )["KNOWN_MODULES"]
    documented = set(re.findall(r"^\| `([^`]+)` \|", catalog, re.MULTILINE))
    assert documented == selectable
