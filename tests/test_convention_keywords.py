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


def test_modular_convention_paths_have_no_legacy_files():
    modules = {
        "core",
        "ergonomic-architecture",
        "database",
        "http-api",
        "kotlin",
        "spring",
        "junit",
        "kotest",
    }
    assert modules <= {path.name for path in CONVENTIONS_ROOT.iterdir() if path.is_dir()}
    assert not [path for path in CONVENTIONS_ROOT.glob("*.md")]
