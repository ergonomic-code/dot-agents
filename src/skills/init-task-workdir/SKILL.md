---
name: init-task-workdir
description: Create a new task workdir under `devlog/NNN-slug` with `010-task-brief.md`, `030-solution-brief.md` and `todo.md` from framework templates. Use when the user asks to create, initialize, or bootstrap a task directory, task workdir, or devlog entry and provides, or must be asked for, a three-digit task id and slug.
---

# Init Task Workdir

Read `framework_checkout_root/src/references/task-brief-template.md`.
Read `framework_checkout_root/src/references/solution-brief-template.md`.
Read `framework_checkout_root/src/references/todo-template.md`.

## Workflow

- Resolve only an explicit user argument in form `NNN-slug`, `NNN slug`, or `devlog/NNN-slug`.
- Require `<task-id>` as exactly three digits and `<task-slug>` as one user-provided path segment.
- Do not derive the slug from a title or requirements text.
- If id or slug is missing, ask only for the missing part and stop.
- If the slug contains a path separator or escapes `./devlog`, ask for a corrected slug and stop.
- Use target directory `./devlog/<task-id>-<task-slug>`.
- If the target directory already exists, stop and report that no files were changed.
- Create only the target directory, `010-task-brief.md`, `030-solution-brief.md`. and `todo.md`.
- Copy the file templates from the loaded references.
- Create a flat task directory by default.
- Keep placeholders unless the user explicitly provided exact values.
- Do not inspect product code, infer requirements, or create extra files.
- Verify that the directory and all files exist.

## Output

Report the created directory and files.
If stopped, report the blocking reason and exact missing or conflicting input.
