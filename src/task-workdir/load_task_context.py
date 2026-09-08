#!/usr/bin/env python3

import argparse
from collections.abc import Callable
from pathlib import Path
import sys

from resolve_task import resolve_task


NO_TASK_CONTEXT = "# Active task context\n\nActive task: none\n"
TaskResolver = Callable[[str, Path], Path | None]


def has_useful_work_state(content: str) -> bool:
    return any(
        line.strip() and not line.lstrip().startswith("#")
        for line in content.splitlines()
    )


def load_task_context(
    prompt: str,
    repo_root: Path,
    task_resolver: TaskResolver = resolve_task,
    task_workdir_context: Path | None = None,
) -> str:
    try:
        repo_root = repo_root.resolve()
        context_path = task_workdir_context or Path(__file__).with_name("context.md")
        task_dir = task_resolver(prompt, repo_root)
        if task_dir is None:
            return NO_TASK_CONTEXT
        if not isinstance(task_dir, Path):
            return NO_TASK_CONTEXT

        task_dir = task_dir.resolve()
        task_path = task_dir.relative_to(repo_root).as_posix()
        if not task_dir.is_dir():
            return NO_TASK_CONTEXT

        brief_path = task_dir / "010-task-brief.md"
        if not brief_path.is_file() or not context_path.is_file():
            return NO_TASK_CONTEXT

        rules = context_path.read_text(encoding="utf-8")
        brief = brief_path.read_text(encoding="utf-8")
        work_state_path = task_dir / "work-state.md"
        work_state = (
            work_state_path.read_text(encoding="utf-8")
            if work_state_path.is_file()
            else ""
        )
    except Exception:
        return NO_TASK_CONTEXT

    rules_separator = "" if rules.endswith("\n") else "\n"
    brief_separator = "" if brief.endswith("\n") else "\n"
    output = (
        "# Active task context\n\n"
        f"Active task: `{task_path}`\n\n"
        "## Task-workdir rules\n\n"
        f"{rules}{rules_separator}\n"
        "## Task brief\n\n"
        f"Source: `{task_path}/010-task-brief.md`\n\n"
        f"{brief}{brief_separator}"
    )
    if has_useful_work_state(work_state):
        work_state_separator = "" if work_state.endswith("\n") else "\n"
        output += (
            "\n## Work state\n\n"
            f"Source: `{task_path}/work-state.md`\n\n"
            f"{work_state}{work_state_separator}"
        )
    return output


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo-root", type=Path, default=Path.cwd())
    args = parser.parse_args()
    print(load_task_context(sys.stdin.read(), args.repo_root), end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
