---
name: advance-task
description: Advance a prepared Lightweight SDD task by identifying and executing exactly one next verified TDD increment stage, then stop. Use when the user asks to continue, advance, or take the next task step without delegating the whole task to `$implement-task-tdd`.
---

# Advance Task

Read `framework_checkout_root/src/roles/developer.md`.
Read `framework_checkout_root/src/conventions/process/tasks.md`.
Read `references/advance-contract.md`.

## Input

Require one task directory.
Resolve it through `framework_checkout_root/src/conventions/process/tasks.md`.
Require `<task-dir>/010-task-brief.md`, `<task-dir>/030-solution-brief.md`, and `<task-dir>/todo.md`.
If any required file is missing, return `status: blocked` and name it.

## State verification

Read the current task artifacts, material current-session results, relevant implementation and tests, `git status`, staged and unstaged diffs, current `HEAD`, and relevant Git history.
Treat only observed files, diffs, command results, and explicit current-session outcomes as stage evidence.
Do not infer a completed stage solely from a todo marker, commit message, file presence, or expected test state.
Identify unrelated user changes and preserve them.
Stop when unrelated changes overlap the files, hunks, symbols, generated artifacts, or behavior boundary required by the next stage.
Do not clean, restore, stash, stage, or commit changes.

## Advance

Use `references/advance-contract.md` to select the earliest incomplete stage whose prerequisites are proven.
Execute exactly that stage and do not begin another stage in the same invocation.
Invocation of this skill authorizes execution of the selected stage, but not a nested approval required by a named stage skill.
When the selected stage names a skill, load and follow it as its caller, passing the task directory, selected increment, prior verified outcomes, explicit target paths, and allowed write boundary.
Apply that skill's stricter input, write, stop, validation, and output rules.
Otherwise execute the stage contract directly.

After execution, verify the actual files, diffs, `HEAD`, unrelated changes, and the stage-specific completion condition.
Return `status: pending` when the selected stage remains active but can continue within its approved boundary.
Return `status: blocked` when its prerequisites conflict, its boundary must widen, or its completion cannot be verified.
Do not select or execute the following stage for a `pending` or `blocked` result.

## Output

Report:

- task directory;
- selected increment or `unresolved`;
- selected stage;
- `status`: `complete`, `pending`, or `blocked`;
- evidence used to select the stage;
- stage outcome or exact blocker;
- changed files;
- commands run and verification results;
- current `HEAD`, staged and unstaged paths, and unrelated changes preserved;
- next stage when it is already determined, without starting it.

When no unimplemented behavior remains, return `status: complete` with `outcome: task-complete` and make no changes.
