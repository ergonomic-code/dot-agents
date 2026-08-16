---
name: plan-test-case-fixing
description: Plan how to fix production code for one red Kotlin JUnit case using the planning phase shared with `$fix-red-case` without changing test or production code; when a task directory resolves, synchronize its task and solution briefs with user-confirmed requirement or implementation changes discovered during planning.
---

# Plan Test Case Fixing

Read `framework_checkout_root/src/references/red-case-fix-planning.md`.
Read `framework_checkout_root/src/conventions/process/tasks.md`.

## Input

Require exactly one selected Kotlin JUnit case.
Require the case to be red by reproducing it or inspecting concrete failing evidence.
Resolve an optional task directory through `framework_checkout_root/src/conventions/process/tasks.md`.
When a task directory resolves, require `<task-dir>/010-task-brief.md` and `<task-dir>/030-solution-brief.md`.
If either brief is missing, report it and stop instead of inventing task context.

## Boundary

Follow `Current failure` and `Create a plan` from the shared red-case fix planning reference, then stop before implementing the selected production fix.
Do not require or attempt to activate Codex Plan mode.
Do not modify tests, production code, fixtures, configuration, or other implementation files.
The only permitted writes after the shared planning phase are the task-brief updates defined below.

## Workflow

1. Follow `Current failure` and `Create a plan` from `framework_checkout_root/src/references/red-case-fix-planning.md`, using the resolved briefs as task design when present.
2. If the case conflicts with task design or planning exposes an ambiguous requirement or implementation choice, ask the user instead of resolving it from the test or current code.
3. When a task directory resolves and the user clarifies or changes task requirements or the implementation approach, update the corresponding briefs before finalizing the plan:
   - update `010-task-brief.md` for changed target behavior, scope, terms, scenarios, or requirements;
   - update `030-solution-brief.md` for changed implementation constraints, selected approach, open questions, or rejected alternatives;
   - update both when the decision changes both the task contract and the solution direction.
4. Otherwise, leave resolved briefs unchanged; when no task directory resolves, record any user decision in the plan output without creating task artifacts.
5. Keep brief edits minimal, preserve unrelated content, and do not change requirements merely to make the selected case easier to fix.
6. After any clarification or brief change, repeat `Create a plan` using the user's decision and the current briefs, then repeat from step 2 until no unresolved questions remain.
7. Stop before implementing the selected production fix.

## Output

Report:

- the reusable production-fix plan returned by the shared phase, including the selected case, failure evidence, diagnosed cause, behavior boundary, selected fix, target production areas, and verification command;
- the resolved task directory or `none`;
- user decisions made during planning and resulting brief changes, or `none`;
- unresolved questions or blockers;
- changed files, limited to the permitted briefs, or `none`.
