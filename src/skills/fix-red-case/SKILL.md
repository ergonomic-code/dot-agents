---
name: fix-red-case
description: Fix production code for one red Kotlin JUnit case created or aligned by `$code-test-case`; use after that skill when the test is failing and test edits are forbidden.
---

# Fix Red Case

Read `../../conventions/feature-workdir.md`.
Read `../../conventions/tests.md`.

Use this skill only after `$code-test-case` has created or aligned one Kotlin JUnit case and that case is red.
Fix production code only.
Do not edit tests, test fixtures, test data, assertions, display names, test annotations, or test build configuration.

## Workflow

1. Reproduce or inspect the failing selected test and identify the current failure cause.
2. Resolve the active feature directory via `feature-workdir.md`.
   If resolved, read `<active-feature-dir>/progress.md` when present and every `<active-feature-dir>/050*` artifact that exists.
   If not resolved or no `050*` artifact exists, continue from the failing test, current code, and loaded conventions.
3. Make only the smallest production-code change that addresses the currently observed failure cause and is consistent with the selected case, progress state, and feature design when they exist.
   Before editing production code, read `../../roles/developer.md` and follow it.
   Keep this skill's test-edit ban and selected-case scope as stricter constraints.
   Derive the selected behavior boundary from the failing test's entry point, endpoint, operation, scenario, and feature design when present.
   Keep investigation and edits inside that boundary, except for compile-only call-site propagation forced by the chosen change.
   If the next necessary step would inspect or change a sibling endpoint, operation, mode, or scenario to justify the fix, stop and report the boundary instead of widening the implementation.
   Do not implement predicted later design changes before rerunning the selected test.
   If the test contradicts the feature design, requires test edits, or cannot be fixed within production code, stop and report the blocker.
4. Rerun only the same selected test after each production-code change.
   If it passes, stop.
   If the failure changes, stop immediately and report the new failure.
   If the same failure remains after a production-code change, re-identify the current cause and continue only inside the same selected SUT boundary.
   Stop if the next fix requires changing a sibling endpoint, operation, mode, scenario, or a broader shared path not already inside that boundary.

## Constraints

- Preserve the red case as the contract; do not weaken, skip, rewrite, or delete it.
- Keep scope to the selected failing case and the nearest production change points.
- Do not refactor, redesign, or broaden behavior beyond what the case and feature design require.
- Do not change feature artifacts under this skill.

## Output

Report the failure cause, design context used or absent, production files changed, verification command, and whether the test passed or the failure changed.
