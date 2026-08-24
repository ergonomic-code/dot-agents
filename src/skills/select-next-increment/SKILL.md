---
name: select-next-increment
description: Select and classify the next minimal unfinished task step from a prepared task directory without changing files. Use when a user or coordinating skill needs a read-only selection before test-driven or non-test implementation.
---

# Select Next Increment

Read `framework_checkout_root/src/roles/developer.md`.
Read `framework_checkout_root/src/conventions/process/tasks.md`.
Read `framework_checkout_root/src/conventions/test-design.md`.
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
Exclude a non-test step when its implementation and required verification are both proven complete.
Treat commits, completed todo items, and task artifacts as supporting evidence.
Return `status: blocked` when these sources disagree or the next increment remains ambiguous.
Apply `framework_checkout_root/src/references/test-case-implementation-order.md`.

Classify each unfinished candidate before selecting it:

- `test-eligible behavior` requires an observable behavior or contract from the current explicit user request or `010-task-brief.md`;
- `non-test step` covers an implementation detail, solution choice, implementation or verification instruction that has no independent observable obligation at the delivered capability boundary;
- a current explicit user request for a specific implementation-detail test, or an earlier such request unambiguously recorded in `010-task-brief.md`, makes that detail test-eligible;
- `todo.md`, solution briefs, implementation designs, commits, and existing tests may support or order work but do not independently create a test obligation.

Do not reinterpret an implementation detail as observable behavior merely because it can be exposed or inspected.

## Output

Always report the evidence used, files changed as `none`, and commands run with their results.
Return `status: complete` with `outcome: increment-selected` and:

- the requirement or explicit-test basis that makes the increment test-eligible;
- obligation and observable outcome;
- external entry point and final effect;
- minimal data and variant set, and smallest sufficient production behavior;
- excluded later behavior;
- expected test level and likely red cause;
- evidence that its behavior remains unimplemented, the slice spans its external boundary and observable effect, and no contract-valid degenerate happy path requiring less production behavior remains.

Return `status: complete` with `outcome: non-test-step-selected` and:

- the matching unfinished task item;
- the intended implementation or verification result;
- evidence that it is not a test-eligible behavior;
- the smallest production or task-artifact write set and any mechanical existing-test adaptation required to preserve current behavior checks;
- verification using existing checks or transient diagnostics;
- the prohibition on new tests, new or changed coverage of the selected detail, test-case artifacts, and production surfaces created only for verification.

Return `status: complete` with `outcome: no-unimplemented-work` when neither test-eligible behavior nor non-test work remains.
Return `status: blocked` with the remaining ambiguity, conflict, or missing evidence.
