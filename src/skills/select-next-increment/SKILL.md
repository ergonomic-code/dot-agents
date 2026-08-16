---
name: select-next-increment
description: Select the next minimal unimplemented behavior increment from a prepared task directory without changing files. Use when a user or coordinating skill needs a read-only selection before test design or implementation.
---

# Select Next Increment

Read `framework_checkout_root/src/roles/developer.md`.
Read `framework_checkout_root/src/conventions/process/tasks.md`.
Read `framework_checkout_root/src/references/test-case-implementation-order.md`.

## Input

Require one task directory.
Resolve it through `framework_checkout_root/src/conventions/process/tasks.md`.
Require `<task-dir>/010-task-brief.md`, `<task-dir>/030-solution-brief.md`, and `<task-dir>/todo.md`.
If any required file is missing, return `status: blocked` and name it.

## Selection

Make no file changes.
Read the briefs, `todo.md`, current task artifacts, relevant implementation, tests, verified behavior, working tree, and relevant Git history.
Exclude behavior only when the current implementation or verified behavior proves it implemented.
Treat commits, completed todo items, and task artifacts as supporting evidence.
Return `status: blocked` when these sources disagree or the next increment remains ambiguous.
Apply `framework_checkout_root/src/references/test-case-implementation-order.md`.

## Output

Always report the evidence used, files changed as `none`, and commands run with their results.
Return `status: complete` with `outcome: increment-selected` and:

- obligation and observable outcome;
- external entry point and final effect;
- minimal data and variant set, and smallest sufficient production behavior;
- excluded later behavior;
- expected test level and likely red cause;
- evidence that its behavior remains unimplemented, the slice spans its external boundary and observable effect, and no contract-valid degenerate happy path requiring less production behavior remains.

Return `status: complete` with `outcome: no-unimplemented-behavior` when no unimplemented behavior remains.
Return `status: blocked` with the remaining ambiguity, conflict, or missing evidence.
