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
    assert "## Автоматические пересечения" in catalog


def test_module_catalog_covers_selectable_modules_and_intersections():
    catalog = (ROOT / "docs" / "modules.md").read_text(encoding="utf-8")
    selectable = {
        "core",
        "ergonomic-architecture",
        "ergonomic-testing",
        "tdd",
        "database",
        "http-api",
        "spring",
        "junit",
        "kotest",
    }
    intersections = {
        "spring-http-api",
        "spring-http-api-tests",
    }

    for module in selectable | intersections:
        assert f"`{module}`" in catalog
