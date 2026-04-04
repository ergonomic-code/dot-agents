#!/usr/bin/env python3

import argparse
from functools import lru_cache
from pathlib import Path
import subprocess
import sys


FRAMEWORK_SRC_RELATIVE_FILES = [
    "roles.md",
    "project-baseline.md",
]
DEFAULT_FRAMEWORK_CHECKOUT_ROOT = ".agents/ergo"


@lru_cache(maxsize=1)
def repo_root() -> Path:
    return Path(
        subprocess.check_output(
            ["git", "rev-parse", "--show-toplevel"],
            text=True,
        ).strip()
    )


def resolve_agents_md_path(agents_md_path: str | None) -> Path:
    if not agents_md_path:
        return repo_root() / "AGENTS.md"

    path = Path(agents_md_path)
    if not path.is_absolute():
        path = repo_root() / path
    return path


def installed_framework_checkout_root(agents_md_path_arg: str | None) -> Path:
    agents_md_path = resolve_agents_md_path(agents_md_path_arg)
    if not agents_md_path.is_file():
        return Path(DEFAULT_FRAMEWORK_CHECKOUT_ROOT)

    for line in agents_md_path.read_text(encoding="utf-8").splitlines():
        prefix = "Framework checkout root: "
        if line.startswith(prefix):
            value = line[len(prefix):].strip().rstrip(".")
            return Path(value.strip("`"))

    return Path(DEFAULT_FRAMEWORK_CHECKOUT_ROOT)


def framework_src_root(agents_md_path_arg: str | None) -> Path:
    return repo_root() / installed_framework_checkout_root(agents_md_path_arg) / "src"


def normalize_repo_relative_path(path: Path) -> str:
    try:
        return path.resolve().relative_to(repo_root().resolve()).as_posix()
    except ValueError:
        return path.as_posix()


def load_framework_config(framework_config_path: str | None) -> str:
    if not framework_config_path:
        return ""

    config_path = Path(framework_config_path)
    if not config_path.is_absolute():
        config_path = repo_root() / config_path

    if not config_path.is_file():
        return ""

    yaml_text = config_path.read_text(encoding="utf-8").rstrip("\n")
    if not yaml_text.strip():
        return ""

    rel = normalize_repo_relative_path(config_path)
    return (
        "# Framework config\n\n"
        f"`{rel}`\n\n"
        "```yaml\n"
        f"{yaml_text}\n"
        "```\n"
    )


def load_files(
    framework_config_path: str | None,
    agents_md_path: str | None,
) -> str:
    root = framework_src_root(agents_md_path)
    chunks = []

    for relative_path in FRAMEWORK_SRC_RELATIVE_FILES:
        path = root / relative_path
        if not path.is_file():
            continue

        text = path.read_text(encoding="utf-8")
        if not text.strip():
            continue

        chunks.append(text.rstrip("\n"))

    config_chunk = load_framework_config(framework_config_path).rstrip("\n")
    if config_chunk:
        chunks.append(config_chunk)

    return "\n\n".join(chunks) + ("\n" if chunks else "")


def main() -> int:
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument("--agents-md-path")
    parser.add_argument("--framework-config-path")
    args, _unknown = parser.parse_known_args()

    text = load_files(args.framework_config_path, args.agents_md_path)
    if text:
        sys.stdout.write(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
