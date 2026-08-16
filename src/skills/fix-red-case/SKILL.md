---
name: fix-red-case
description: Fix production code for one red Kotlin JUnit case created or aligned by `$code-test-case`; use after that skill when the test is failing and test edits are forbidden.
---

# Fix Red Case

Read `framework_checkout_root/src/references/red-case-fix-planning.md`.
Read `framework_checkout_root/src/conventions/process/tasks.md`.

Use this skill only after `$code-test-case` has created or aligned one Kotlin JUnit case and that case is red.
Fix production code only.
Do not edit tests, test fixtures, test data, assertions, display names, test annotations, or test build configuration.

## Input

Resolve an optional task directory through `framework_checkout_root/src/conventions/process/tasks.md`.
Use a production-fix plan explicitly included in the current request as the existing plan.
Otherwise, when a task directory resolves, inspect its briefs and relevant task artifacts for plans whose request, artifact, or containing section identifies the selected case.
If exactly one such plan exists, use it as the existing plan.
If selecting among task plans is ambiguous, ask the user instead of choosing one.

## Workflow

1. Establish the current failure through `Current failure` in `framework_checkout_root/src/references/red-case-fix-planning.md`.
2. If an existing plan resolves, follow only `Reuse an existing plan`; otherwise follow `Create a plan` in the same reference.
3. If the selected branch reports an unresolved question or blocker, stop without changing production code.
4. Implement the selected production fix inside its behavior boundary while preserving the planning result and constraints.
   Apply the loaded ergonomic, boundary, and code implementation conventions before editing production code.
   Keep this skill's test-edit ban and selected-case scope as stricter constraints.
5. Rerun only the same selected test after production-code changes.
   If it still fails, re-establish the current failure and follow `Create a plan` for that failure.
   Stop if it reports an unresolved question or blocker, or if the selected fix requires changing a sibling endpoint, operation, mode, scenario, or a broader shared path outside the selected behavior boundary.
   Otherwise implement the next selected fix and repeat the same test.

## Output

Report the plan source (`prompt`, task directory, or new planning), failure causes addressed, design context used or absent, production files changed, verification command, and whether the selected test passed or the work was blocked.
