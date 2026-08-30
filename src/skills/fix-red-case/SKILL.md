---
name: fix-red-case
description: Fix production code for one red Kotlin JUnit case created or aligned by `$code-test-case`; use after that skill when the test is failing and test edits are forbidden.
---

# Fix Red Case

Read `framework_checkout_root/src/references/red-case-fix-selection.md`.

Use this skill only after `$code-test-case` has created or aligned one Kotlin JUnit case and that case is red.
Fix production code only.
Do not edit tests, test fixtures, test data, assertions, display names, test annotations, or test build configuration.

## Input

Accept the selected red case, current failure evidence, and optional design context.

## Workflow

1. Establish the current failure and select a fix through `framework_checkout_root/src/references/red-case-fix-selection.md`.
2. If selection reports an unresolved question or blocker, stop without changing production code.
3. Implement the selected production fix inside its behavior boundary while preserving the selection constraints.
   Apply the loaded ergonomic, boundary, and code implementation conventions before editing production code.
   Keep this skill's test-edit ban and selected-case scope as stricter constraints.
4. Rerun only the same selected test after production-code changes.
   If it still fails, re-establish the current failure and select the next fix for that failure.
   Stop if it reports an unresolved question or blocker, or if the selected fix requires changing a sibling endpoint, operation, mode, scenario, or a broader shared path outside the selected behavior boundary.
   Otherwise implement the next selected fix and repeat the same test.

## Output

Report failure causes addressed, design context used or absent, production files changed, verification command, and whether the selected test passed or the work was blocked.
When invoked by another skill, return `status: complete` with `outcome: selected-test-passes` only when the same selected test passes.
Return `status: pending` only when implementation or verification is interrupted while work remains inside the selected behavior boundary.
Return `status: blocked` when fix selection has an unresolved question or blocker, or green requires changing the selected test or widening the behavior boundary.
