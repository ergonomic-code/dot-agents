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


def test_every_convention_declares_one_to_three_keywords():
    conventions = sorted(CONVENTIONS_ROOT.rglob("*.md"))
    assert conventions

    for convention in conventions:
        keywords = convention_keywords(convention)
        assert 1 <= len(keywords) <= 3, (
            f"{convention} must declare one to three keywords"
        )
        assert len(keywords) == len(set(keywords)), (
            f"{convention} has duplicate keywords"
        )
        assert all(KEYWORD_PATTERN.fullmatch(keyword) for keyword in keywords), (
            f"{convention} keywords must use lowercase kebab-case"
        )
