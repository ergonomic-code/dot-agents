---
name: refactor-case
description: Review and refactor code after `$code-test-case` and `$fix-red-case` have made a selected case green; use when the user asks to refactor one commit, current uncommitted changes, or one bounded red-plus-green TDD increment before broadening scope.
---

# Refactor Case

Read `../../conventions/code-implementation.md`.
Read `../../conventions/ergonomic-approach-rules.md`.
Read `../../conventions/ergonomic-architecture.md`.
Follow its projection-specific loading rules.
Read `../../conventions/abstraction-level-boundaries.md`.
Read `../../conventions/test-fixture-architecture.md`.
Read `../../conventions/http-api-test-rules.md`.
Read `./references/api-alignment.md`.

Use this skill only after the selected case is green.
Accept one commit, current uncommitted changes, or one coordinator-supplied bounded TDD increment identified by its red and green boundary commits.

## Workflow

1. Inspect the target diff and the selected case context when available.
   For a bounded TDD increment, inspect the full net diff from the red commit's parent through the green commit, including every intervening commit, and treat that range as the target boundary.
2. Inspect production changes inside the target boundary for:
   - duplication per `../../conventions/ergonomic-approach-rules.md`, including matches between changed and sibling code;
   - mixed abstraction levels per `abstraction-level-boundaries.md`;
   - misplaced mechanics that belong behind an adapter, helper, mapper, value type, or collaborator;
   - violations of loaded EA conventions, especially unclear operation/resource boundaries, peer horizontal dependencies, mixed orchestration and infrastructure concerns, or hidden direct dependencies that should stay explicit.
3. Inspect test changes inside the target boundary for:
   - violations of `test-fixture-architecture.md`, especially `*TestApi` scope leaks, cross-scope orchestration inside `*TestApi`, or setup that belongs in `*FixturePresets`;
   - violations of other loaded test conventions when they materially apply, especially `http-api-test-rules.md` for HTTP boundary tests and `*HttpApi` helpers.
4. If there is no useful narrow refactoring inside the target boundary, make no edits, rerun the selected test, and return a verified `no-op` without selecting a mode or requesting edit approval.
5. Otherwise classify the selected refactoring as exactly one mode:
   - `production` when the intended structural change is in production code;
   - `test` when the intended structural change is in test code;
   - stop if the iteration needs both, except for the minimal test updates required by `references/api-alignment.md`.
6. Load and apply exactly one matching rule file:
   - in `production` mode, read `../../conventions/process/production-code-refactoring.md`;
   - in `test` mode, read `../../conventions/process/tests-refactoring.md`.
7. For duplication, propose the narrowest shared implementation that owns the complete repeated responsibility while preserving behavior.
8. Propose a short refactor plan and wait for explicit approval before editing.
9. After approval, change structure only.
   Preserve observable behavior, public contracts, persistence shape, API responses, test intent.
10. Rerun the selected test.
   If shared APIs or broad call sites changed, also run the smallest relevant compile or module test.

## Constraints

- Do not add behavior, cases, assertions, migrations, endpoint contracts, config, retries, defaults, or compatibility branches.
- Do not weaken, rewrite, skip, or delete tests.
- In one iteration, refactor either production code or test code, not both.
- In `production` mode, do not change test structure except for the minimal updates required by `references/api-alignment.md`.
- In `test` mode, do not change production code.
- Do not broaden beyond the commit, uncommitted diff, or bounded TDD increment except for compile-required call-site propagation.
- Prefer moving, extracting, renaming, or introducing a narrow helper over new framework abstractions.
- Stop if a desired cleanup requires behavior clarification or wider redesign.

## Output

Before edits, report the target, chosen refactor mode, findings, proposed refactor steps, and validation plan.
For a no-op, report the target, absence of a useful narrow refactoring, and validation result.
After edits, report files changed and validation result.
