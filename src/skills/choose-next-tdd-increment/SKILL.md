---
name: choose-next-tdd-increment
description: Choose the next small TDD increment from a feature brief, code anchors, principle-level solution, branch changes, and progress state. Use when the user asks to choose, propose, or add the next increment, iteration, TDD slice, red/green slice, or progress item for an active feature/devlog branch.
---

# Choose Next TDD Increment

Read `framework_checkout_root/src/conventions/feature-workdir.md`.

## Inputs

Resolve the active feature directory and optional implementation stage through `feature-workdir.md`.
Use an explicitly named `progress.md`.
Otherwise use the single relevant `progress.md` from the active stage or feature directory.
If zero or several progress files remain possible, stop and ask for the target file.

Discover required context near the active feature/stage:
- feature brief;
- code anchors;
- principle-level solution or blueprint;
- current feature branch changes;
- current progress.

If any required context cannot be found, stop and name what is missing.

## Selection

Read the progress file before choosing options.
Treat it as the authoritative queue.
Use feature artifacts and branch changes to avoid duplicates, stale work, and already-implemented slices.
Prefer the smallest increment that can move through one red step and one green step.
Keep each option inside one behavior, API surface, refactor boundary, or testable integration seam.
Do not mix unrelated obligations only because they touch the same files.

Return 2-4 short numbered options and wait for the user to choose.
If no meaningful next increment remains, return the explicit option `Судя по всему фича реализована полностью` and explain the evidence in one short line.
For each increment option include only:
- scope;
- why now;
- red+green;
- files;
- risk.

Do not edit files before the user chooses an option.
If the progress file already contains the chosen increment, report the existing item and do not add a duplicate.

## Progress Update

After the user chooses an option, update only the selected `progress.md`.
If the user chooses `Судя по всему фича реализована полностью`, do not edit files.
Do not create or edit code, tests, test-case artifacts, brief files, design docs, or other progress files.
The user's choice authorizes the write; do not ask for a second confirmation.

Insert the item into the matching implementation queue, stage, or `Feature` group.
If the insertion point is ambiguous, stop and ask where to place it.
Preserve existing indentation and checklist style.

Use exactly this shape:

```markdown
- [ ] <short increment title>
  - [ ] Красный тест
  - [ ] Зелёный тест
```

After writing, report the updated progress path and the added increment title.
