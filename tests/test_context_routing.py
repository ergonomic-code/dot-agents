import re
from pathlib import Path

import yaml


CONTEXT_ROOT = Path(__file__).parents[1] / "src" / "context"
SRC_ROOT = CONTEXT_ROOT.parent


def front_matter(path: Path) -> dict:
    text = path.read_text()
    _start, yaml_text, _body = text.split("---", 2)
    return yaml.safe_load(yaml_text)


def test_topical_indexes_have_valid_module_metadata_and_unique_order():
    known_modules = {
        "core",
        "ergonomic-architecture",
        "ergonomic-testing",
        "database",
        "http-api",
        "kotlin",
        "spring",
        "junit",
        "kotest",
    }
    orders = []

    for path in CONTEXT_ROOT.glob("*.md"):
        if path.name == "index.md":
            continue
        metadata = front_matter(path)
        assert set(metadata) == {"requires_modules", "applies_when", "routing_order"}
        assert metadata["requires_modules"]
        assert set(metadata["requires_modules"]) <= known_modules
        assert metadata["applies_when"].strip()
        orders.append(metadata["routing_order"])

    assert len(orders) == len(set(orders))

def test_stack_matrix_is_expressed_by_index_text():
    database = (CONTEXT_ROOT / "relational-databses.md").read_text()
    http_api = (CONTEXT_ROOT / "http-api.md").read_text()
    kotlin = (CONTEXT_ROOT / "kotlin.md").read_text()
    spring = (CONTEXT_ROOT / "spring.md").read_text()

    kotlin_database = (CONTEXT_ROOT / "kotlin-database.md").read_text()
    spring_http = (CONTEXT_ROOT / "spring-http-api.md").read_text()
    spring_http_tests = (CONTEXT_ROOT / "spring-http-api-tests.md").read_text()
    spring_database = (CONTEXT_ROOT / "spring-database.md").read_text()
    spring_kotlin = (CONTEXT_ROOT / "spring-kotlin.md").read_text()
    kotlin_http = (CONTEXT_ROOT / "kotlin-http-api.md").read_text()

    assert "kotlin/persistence-models.md" not in kotlin
    assert "kotlin/persistence-models.md" in kotlin_database
    assert "http-api-versioning.md" not in kotlin
    assert "http-api-versioning.md" in kotlin_http
    assert "spring/" not in database
    assert "spring/" not in http_api
    assert "spring-jdbc.md" not in spring
    assert "kotlin-beans.md" not in spring
    assert "spring-http-json-api.md" not in spring
    assert "http-api-tests.md" not in spring
    assert "spring-http-json-api.md" in spring_http
    assert "http-api-tests.md" not in spring_http
    assert "http-api-tests.md" in spring_http_tests
    assert "spring-jdbc.md" in spring_database
    assert "kotlin-beans.md" in spring_kotlin


def referenced_convention_paths(text: str) -> list[Path]:
    return [
        SRC_ROOT / "conventions" / match
        for match in re.findall(r"`(?:\.\./|framework_checkout_root/src/)*conventions/([^`]+\.md)`", text)
    ]


def test_index_convention_references_exist_and_are_reachable():
    indexed = set()
    for index in CONTEXT_ROOT.glob("*.md"):
        for path in referenced_convention_paths(index.read_text()):
            assert path.is_file(), f"{index} references missing {path}"
            indexed.add(path)

    for convention in (SRC_ROOT / "conventions").rglob("*.md"):
        assert convention in indexed, (
            f"{convention} is not reachable from a context index"
        )


def test_all_relative_markdown_references_from_indexes_exist():
    for index in CONTEXT_ROOT.glob("*.md"):
        references = re.findall(r"`(\.\./[^`]+\.md)`", index.read_text())
        for reference in references:
            assert (index.parent / reference).resolve().is_file(), (
                f"{index} references missing {reference}"
            )


def test_all_convention_references_exist():
    documents = [*CONTEXT_ROOT.glob("*.md")]
    documents.extend((SRC_ROOT / "skills").rglob("*.md"))
    documents.extend((SRC_ROOT / "task-workdir" / "skills").rglob("*.md"))
    documents.extend((SRC_ROOT / "references").rglob("*.md"))

    for document in documents:
        for path in referenced_convention_paths(document.read_text()):
            assert path.is_file(), f"{document} references missing {path}"


def test_code_test_case_keeps_only_intrinsic_core_naming_dependencies():
    paths = referenced_convention_paths(
        (SRC_ROOT / "skills" / "code-test-case" / "SKILL.md").read_text()
    )
    assert SRC_ROOT / "conventions/core/test-naming.md" in paths
    assert all(path.parent.name == "core" for path in paths)


def test_skill_checks_modules_before_optional_module_dependencies():
    skill = SRC_ROOT / "skills" / "refactor-case" / "SKILL.md"
    metadata = front_matter(skill)
    text = skill.read_text()

    assert metadata["requires_modules"] == ["core", "ergonomic-architecture"]
    assert text.index("проверь наличие всех `requires_modules`") < text.index(
        "../../conventions/ergonomic-architecture/abstraction-level-boundaries.md"
    )


def test_generic_tdd_chain_has_no_routed_technology_contracts():
    documents = [
        SRC_ROOT / "skills/code-test-case/SKILL.md",
        SRC_ROOT / "skills/code-test-case/references/coding-plan.md",
        SRC_ROOT / "skills/code-test-case/agents/openai.yaml",
        SRC_ROOT / "skills/fix-red-case/SKILL.md",
        SRC_ROOT / "skills/fix-red-case/agents/openai.yaml",
        SRC_ROOT / "references/red-case-fix-selection.md",
    ]
    technology_markers = ("kotlin", "junit", "kotest", "spring")

    for document in documents:
        text = document.read_text().lower()
        assert all(marker not in text for marker in technology_markers), document


def test_general_conventions_have_no_spring_or_controller_leaks():
    general_http = "\n".join(
        path.read_text() for path in (SRC_ROOT / "conventions" / "http-api").glob("*.md")
    )
    database = "\n".join(
        path.read_text() for path in (SRC_ROOT / "conventions" / "database").glob("*.md")
    )

    assert "controller" not in general_http
    assert "WebTestClient" not in general_http
    assert "RestTestClient" not in general_http
    assert "@ReadingConverter" not in database
    assert "JdbcCustomConversions" not in database
