#!/usr/bin/env python3

import argparse
from collections.abc import Callable, Mapping
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile

import yaml


NO_TASK = "n/a"
TASK_ID = r"[^\W_]+(?:-[^\W_]+)*"
TASK_DIRECTORY = re.compile(r"^(?P<id>[^\W_]+)(?:-.+)?$")
STANDALONE_ID = re.compile(
    rf"(?m)(?:^|\\n)[ \t]*(?P<id>{TASK_ID})[ \t]*(?=$|\\n)"
)
SKILL_ID = re.compile(
    r"(?:"
    r"`?\$[A-Za-z0-9][A-Za-z0-9_-]*`?"
    r"|"
    r"`?(?:[^\s`]+/)?skills/[^\s`]+/SKILL\.md`?"
    rf")\s+(?P<id>{TASK_ID})(?![\w-])"
)

SemanticResolver = Callable[[str, Mapping[str, Path]], str]


def directory_task_id(path: Path) -> str | None:
    brief = path / "010-task-brief.md"
    try:
        lines = brief.read_text(encoding="utf-8").splitlines() if brief.is_file() else []
        if lines and lines[0] == "---":
            end = lines.index("---", 1)
            metadata = yaml.safe_load("\n".join(lines[1:end]))
            if not isinstance(metadata, dict):
                return None
            if "task_id" in metadata:
                task_id = metadata["task_id"]
                if not isinstance(task_id, str) or not re.fullmatch(TASK_ID, task_id):
                    return None
                if path.name == task_id or (
                    path.name.startswith(task_id + "-")
                    and len(path.name) > len(task_id) + 1
                ):
                    return task_id
                return None
    except (OSError, UnicodeError, ValueError, yaml.YAMLError):
        return None

    match = TASK_DIRECTORY.fullmatch(path.name)
    return match.group("id") if match else None


def active_tasks(repo_root: Path) -> dict[str, Path]:
    devlog = repo_root / "devlog"
    if not devlog.is_dir():
        return {}

    tasks: dict[str, Path] = {}
    duplicate_ids: set[str] = set()
    for path in devlog.iterdir():
        if not path.is_dir() or path.name in {"done", "on-hold"}:
            continue
        task_id = directory_task_id(path)
        if task_id is None:
            continue
        if task_id in tasks:
            duplicate_ids.add(task_id)
        else:
            tasks[task_id] = path

    for task_id in duplicate_ids:
        del tasks[task_id]
    return tasks


def referenced_task_ids(prompt: str, active_ids: set[str]) -> list[str]:
    references = {
        match.group("id")
        for pattern in (STANDALONE_ID, SKILL_ID)
        for match in pattern.finditer(prompt)
        if match.group("id") in active_ids
    }
    return sorted(references)


def build_resolver_prompt(prompt: str, candidates: Mapping[str, Path]) -> str:
    sections = [
        "Выбери одну задачу из кандидатов, которая однозначно соответствует запросу.",
        f"Верни ровно один идентификатор кандидата или {NO_TASK}.",
        "Не используй инструменты.",
        "",
        "Исходный запрос:",
        prompt,
    ]
    for task_id, task_dir in candidates.items():
        brief = task_dir / "010-task-brief.md"
        content = brief.read_text(encoding="utf-8") if brief.is_file() else ""
        sections.extend(["", f"Кандидат {task_id}:", content])
    return "\n".join(sections)


def invoke_codex(prompt: str, candidates: Mapping[str, Path]) -> str:
    codex = shutil.which("codex") or "/opt/codex/bin/codex"
    with tempfile.TemporaryDirectory() as temp_dir:
        output_path = Path(temp_dir) / "response.txt"
        command = [
            codex,
            "exec",
            "--ephemeral",
            "--ignore-user-config",
            "--ignore-rules",
            "--skip-git-repo-check",
            "--sandbox",
            "read-only",
            "--disable",
            "shell_tool",
            "--disable",
            "unified_exec",
            "--disable",
            "code_mode",
            "--disable",
            "apps",
            "--disable",
            "browser_use",
            "--disable",
            "computer_use",
            "--disable",
            "image_generation",
            "--disable",
            "multi_agent",
            "--disable",
            "goals",
            "-c",
            "mcp_servers={}",
            "-c",
            "enabled_tools=[]",
            "--output-last-message",
            str(output_path),
            "-",
        ]
        subprocess.run(
            command,
            input=build_resolver_prompt(prompt, candidates),
            text=True,
            cwd=temp_dir,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            check=True,
        )
        return output_path.read_text(encoding="utf-8").strip()


def resolve_task(
    prompt: str,
    repo_root: Path,
    semantic_resolver: SemanticResolver = invoke_codex,
) -> Path | None:
    tasks = active_tasks(repo_root)
    candidate_ids = referenced_task_ids(prompt, set(tasks))
    if not candidate_ids:
        return None
    if len(candidate_ids) == 1:
        return tasks[candidate_ids[0]]

    candidates = {task_id: tasks[task_id] for task_id in candidate_ids}
    try:
        selected = semantic_resolver(prompt, candidates).strip()
    except (OSError, subprocess.SubprocessError):
        return None
    if selected not in candidates:
        return None
    return candidates[selected]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo-root", type=Path, default=Path.cwd())
    args = parser.parse_args()
    prompt = sys.stdin.read()
    resolved = resolve_task(prompt, args.repo_root.resolve())
    if resolved is None:
        print(NO_TASK)
    else:
        print(resolved.relative_to(args.repo_root.resolve()).as_posix())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
