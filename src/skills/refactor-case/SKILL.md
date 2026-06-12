---
name: refactor-case
description: Review and refactor code after `$code-test-case` and `$fix-red-case` have made a selected case green; use when the user asks to refactor a commit or uncommitted changes before broadening scope.
---

# Refactor Case

Read `../../conventions/code-implementation.md`.
Read `../../conventions/ergonomic-approach-rules.md`.
Read `../../conventions/task-boundaries.md`.
Read `../../conventions/abstraction-level-boundaries.md`.

Use this skill only after the selected case is green.
Accept either one commit or current uncommitted changes as the refactor target.

## Workflow

1. Inspect the target diff and the selected case context when available.
2. Find refactor-only problems inside the target boundary:
   - duplication after the second occurrence;
   - mixed abstraction levels per `abstraction-level-boundaries.md`;
   - misplaced mechanics that belong behind an adapter, helper, mapper, value type, or collaborator.
3. Propose a short refactor plan and wait for explicit approval before editing.
4. After approval, change structure only.
   Preserve observable behavior, public contracts, persistence shape, API responses, test intent, and progress state.
5. Rerun the selected test.
   If shared APIs or broad call sites changed, also run the smallest relevant compile or module test.

## Constraints

- Do not add behavior, cases, assertions, migrations, endpoint contracts, config, retries, defaults, or compatibility branches.
- Do not weaken, rewrite, skip, or delete tests.
- Do not broaden beyond the commit or uncommitted diff except for compile-required call-site propagation.
- Prefer moving, extracting, renaming, or introducing a narrow helper over new framework abstractions.
- Stop if a desired cleanup requires behavior clarification or wider redesign.

## Output

Before edits, report the target, findings, proposed refactor steps, and validation plan.
After edits, report files changed and validation result.
