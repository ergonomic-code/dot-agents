#!/usr/bin/env python
"""Create a Git evidence snapshot for a session-backlog entry."""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from datetime import UTC, datetime
from pathlib import Path


def run_git(repo_root: Path, *args: str) -> str:
    result = subprocess.run(
        ["git", "-C", str(repo_root), *args],
        check=True,
        capture_output=True,
        text=True,
    )
    return result.stdout


def unique_bundle_path(backlog_dir: Path, label: str) -> Path:
    entry_date = datetime.now(UTC).date().isoformat()
    slug = re.sub(r"[^a-z0-9]+", "-", label.lower()).strip("-")[:48] or "session"
    entry_pattern = re.compile(rf"^{re.escape(entry_date)}-(\d+)-")
    entry_numbers = [
        int(match.group(1))
        for child in backlog_dir.iterdir()
        if (match := entry_pattern.match(child.name))
    ]
    return backlog_dir / f"{entry_date}-{max(entry_numbers, default=0) + 1:02d}-{slug}"


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Create a Git evidence bundle for a session backlog entry."
    )
    parser.add_argument("--repo-root", required=True, type=Path)
    parser.add_argument("--backlog-dir", required=True, type=Path)
    parser.add_argument("--current-directory", required=True, type=Path)
    parser.add_argument("--label", default="session-evidence")
    args = parser.parse_args()

    repo_root = args.repo_root.resolve()
    if not (repo_root / ".git").exists():
        parser.error(f"--repo-root is not a Git worktree: {repo_root}")

    try:
        head = run_git(repo_root, "rev-parse", "HEAD").strip()
        branch = run_git(repo_root, "branch", "--show-current").strip()
        commit = run_git(repo_root, "show", "--no-ext-diff", "--no-patch", "--format=fuller", "HEAD")
        status = run_git(repo_root, "status", "--short", "--untracked-files=all")
        diff = run_git(repo_root, "diff", "--no-ext-diff", "--binary", "HEAD")
        diff_stat = run_git(repo_root, "diff", "--no-ext-diff", "--stat", "HEAD")
    except (OSError, subprocess.CalledProcessError) as error:
        print(f"Could not collect Git evidence: {error}", file=sys.stderr)
        return 1

    backlog_dir = args.backlog_dir.resolve()
    backlog_dir.mkdir(parents=True, exist_ok=True)
    bundle_dir = unique_bundle_path(backlog_dir, args.label)
    git_dir = bundle_dir / "git"
    git_dir.mkdir(parents=True)

    (git_dir / "head.txt").write_text(f"{head}\n", encoding="utf-8")
    (git_dir / "branch.txt").write_text(f"{branch or '(detached HEAD)'}\n", encoding="utf-8")
    (git_dir / "commit.txt").write_text(commit, encoding="utf-8")
    (git_dir / "status-short.txt").write_text(status, encoding="utf-8")
    (git_dir / "diff.patch").write_text(diff, encoding="utf-8")
    (git_dir / "diff-stat.txt").write_text(diff_stat, encoding="utf-8")
    metadata = {
        "schema_version": 1,
        "captured_at_utc": datetime.now(UTC).isoformat(),
        "current_directory": str(args.current_directory.resolve()),
        "repository_root": str(repo_root),
        "head": head,
        "branch": branch or None,
        "diff_base": "HEAD",
        "commands": {
            "commit": "git show --no-ext-diff --no-patch --format=fuller HEAD",
            "status": "git status --short --untracked-files=all",
            "diff": "git diff --no-ext-diff --binary HEAD",
            "diff_stat": "git diff --no-ext-diff --stat HEAD",
        },
    }
    (bundle_dir / "metadata.json").write_text(
        json.dumps(metadata, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(bundle_dir)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
