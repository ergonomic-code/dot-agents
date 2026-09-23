import re
from pathlib import Path


CONTEXT_ROOT = Path(__file__).parents[1] / "src" / "context"
SRC_ROOT = CONTEXT_ROOT.parent


def test_root_context_orders_independent_module_indexes():
    index = (CONTEXT_ROOT / "index.md").read_text()
    expected = [
        "markup.md",
        "production-code.md",
        "tests.md",
        "database.md",
        "http-api.md",
        "architecture.md",
        "kotlin.md",
        "spring.md",
        "junit.md",
        "kotest.md",
    ]
    positions = [index.index(f"`{item}`") for item in expected]
    assert positions == sorted(positions)


def test_technology_indexes_keep_routing_independent():
    kotlin = (CONTEXT_ROOT / "kotlin.md").read_text()
    junit = (CONTEXT_ROOT / "junit.md").read_text()
    kotest = (CONTEXT_ROOT / "kotest.md").read_text()

    assert "independently" in kotlin
    assert "Do not load Kotlin production process for a test-only Kotlin change." in kotlin
    assert "does not imply Spring or Kotest" in junit
    assert "does not imply Spring or JUnit" in kotest


def test_stack_matrix_is_expressed_by_index_text():
    database = (CONTEXT_ROOT / "database.md").read_text()
    http_api = (CONTEXT_ROOT / "http-api.md").read_text()
    kotlin = (CONTEXT_ROOT / "kotlin.md").read_text()
    spring = (CONTEXT_ROOT / "spring.md").read_text()

    assert "kotlin/persistence-models.md" in kotlin
    assert "also touches persistence" in kotlin
    assert "spring/" not in database
    assert "spring/" not in http_api
    assert "Spring HTTP test clients" in spring


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
