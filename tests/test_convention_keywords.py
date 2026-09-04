import re
from pathlib import Path


CONVENTIONS_ROOT = Path(__file__).parents[1] / "src" / "conventions"
KEYWORD_PATTERN = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*")


def convention_keywords(path: Path) -> list[str]:
    lines = path.read_text().splitlines()
    assert lines and lines[0] == "---", f"{path} has no YAML front matter"
    assert "---" in lines[1:], f"{path} has unclosed YAML front matter"
    end = lines.index("---", 1)
    metadata = lines[1:end]
    assert metadata and metadata[0] == "keywords:", f"{path} has no keywords list"
    assert all(line.startswith("  - ") for line in metadata[1:]), (
        f"{path} has unsupported keyword metadata"
    )
    return [line.removeprefix("  - ") for line in metadata[1:]]


def test_every_convention_declares_keywords_and_at_least_two_rules():
    conventions = sorted(CONVENTIONS_ROOT.rglob("*.md"))
    assert conventions

    for convention in conventions:
        keywords = convention_keywords(convention)
        assert keywords, f"{convention} must declare at least one keyword"
        assert len(keywords) == len(set(keywords)), (
            f"{convention} has duplicate keywords"
        )
        assert all(KEYWORD_PATTERN.fullmatch(keyword) for keyword in keywords), (
            f"{convention} keywords must use lowercase kebab-case"
        )
        lines = convention.read_text().splitlines()
        front_matter_end = lines.index("---", 1)
        rules = [line for line in lines[front_matter_end + 1 :] if line.startswith("- ")]
        assert len(rules) >= 2, f"{convention} must contain at least two rules"
