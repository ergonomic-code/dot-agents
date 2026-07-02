---
name: refactor-case
description: Review and refactor code after `$code-test-case` and `$fix-red-case` have made a selected case green; use when the user asks to refactor a commit or uncommitted changes before broadening scope.
---

# Refactor Case

Read `../../conventions/code-implementation.md`.
Read `../../conventions/ergonomic-approach-rules.md`.
Read `../../conventions/ergonomic-architecture.md`.
Follow its projection-specific loading rules.
Read `../../conventions/task-boundaries.md`.
Read `../../conventions/abstraction-level-boundaries.md`.
Read `../../conventions/test-fixture-architecture.md`.
Read `../../conventions/http-api-test-rules.md`.
Read `./references/api-alignment.md`.

Use this skill only after the selected case is green.
Accept either one commit or current uncommitted changes as the refactor target.

## Workflow

1. Inspect the target diff and the selected case context when available.
2. Classify the iteration as exactly one refactor mode:
   - `production` when the intended structural change is in production code;
   - `test` when the intended structural change is in test code;
   - stop if the iteration needs both, except for the minimal test updates required by `references/api-alignment.md`.
3. In `production` mode, find refactor-only problems inside the target boundary:
   - duplication after the second occurrence, including sibling code that repeats the same responsibility with different expressions;
   - mixed abstraction levels per `abstraction-level-boundaries.md`;
   - misplaced mechanics that belong behind an adapter, helper, mapper, value type, or collaborator;
   - violations of loaded EA conventions, especially unclear operation/resource boundaries, peer horizontal dependencies, mixed orchestration and infrastructure concerns, or hidden direct dependencies that should stay explicit.
4. In `test` mode, find refactor-only problems inside the target boundary:
   - violations of `test-fixture-architecture.md`, especially `*TestApi` scope leaks, cross-scope orchestration inside `*TestApi`, or setup that belongs in `*FixturePresets`;
   - violations of other loaded test conventions when they materially apply, especially `http-api-test-rules.md` for HTTP boundary tests and `*HttpApi` helpers.
5. For duplication, propose one format and a narrow helper when behavior stays equivalent.
6. Propose a short refactor plan and wait for explicit approval before editing.
7. After approval, change structure only.
   Preserve observable behavior, public contracts, persistence shape, API responses, test intent.
8. Rerun the selected test.
   If shared APIs or broad call sites changed, also run the smallest relevant compile or module test.

## Constraints

- Do not add behavior, cases, assertions, migrations, endpoint contracts, config, retries, defaults, or compatibility branches.
- Do not weaken, rewrite, skip, or delete tests.
- In one iteration, refactor either production code or test code, not both.
- In `production` mode, do not change test structure except for the minimal updates required by `references/api-alignment.md`.
- In `test` mode, do not change production code.
- Do not broaden beyond the commit or uncommitted diff except for compile-required call-site propagation.
- Prefer moving, extracting, renaming, or introducing a narrow helper over new framework abstractions.
- Stop if a desired cleanup requires behavior clarification or wider redesign.

## Output

Before edits, report the target, chosen refactor mode, findings, proposed refactor steps, and validation plan.
After edits, report files changed and validation result.
