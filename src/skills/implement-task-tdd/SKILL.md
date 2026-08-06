---
name: implement-task-tdd
description: Coordinate implementation of a task directory through minimal reviewed vertical TDD increments, with every selection, test design, API design, red, green, and refactor stage delegated to a separate sequential subagent and committed at the defined boundaries. Use when the user asks to implement a task, todo, or briefs end to end through TDD with human approval after every stage.
---

# Implement Task with TDD

Read `framework_checkout_root/src/roles/developer.md`.
Read `framework_checkout_root/src/conventions/process/tasks.md`.
Read `framework_checkout_root/src/references/test-case-implementation-order.md`.
Read `references/stage-contracts.md`.

## Input

Require one task directory.
Resolve it through `framework_checkout_root/src/conventions/process/tasks.md`.
Require `<task-dir>/010-task-brief.md`, `<task-dir>/030-solution-brief.md`, and `<task-dir>/todo.md`.
If any required file is missing, stop and name it.

Before selecting an increment:

- read every current task artifact needed to understand the briefs and implementation status;
- read `todo.md`;
- inspect `git status`, staged and unstaged diffs, current `HEAD`, and relevant Git history;
- identify unrelated user changes and preserve them;
- record the verified Git state for the next subagent.

Stop if unrelated changes overlap the files, hunks, symbols, migrations, generated artifacts, or behavior boundary required by the next increment.
Do not clean, restore, stash, stage, or commit unrelated changes.

## Coordination

Repeat the cycle while the briefs and `todo.md` identify unimplemented behavior.
Run every stage in a new separate subagent.
Run stages strictly in order and never in parallel.
Do not let subagents commit.
If separate subagents are unavailable, stop instead of running a stage in the coordinator.

Immediately before starting every stage subagent, reverify current task artifacts, `HEAD`, staged and unstaged diffs, and unrelated changes against the last approved state.
Record non-overlapping human-approved commits since the last approved state and continue; include them in the later refactor range.
Stop on unauthorized drift or when unrelated changes overlap the increment.
Give every subagent the fresh shared handoff, write set, stop conditions, and required output from `references/stage-contracts.md`.

After every subagent returns, apply the independent verification from `references/stage-contracts.md`.
Only a result that satisfies its stage-specific completion condition completes the stage.
After independently verifying a completed stage, report its result and stop for explicit human approval.
Do not start the next stage before that approval.
Approval of a stage authorizes only the transition and commit defined by this skill.
For `pending` or `blocked`, stop with the same stage active; human approval cannot waive its completion condition.
After the human resolves a blocker or requests continuation of a pending stage, rerun that stage in a new subagent with freshly verified state.
The pre-edit refactor plan is not a completed stage; after its approval, resume the same refactor subagent as defined below.

## Cycle

1. Delegate selection of the next minimal increment.
2. Delegate one test-method-sized design through `$design-test-case`.
3. Delegate design and artifact alignment for only the API surfaces required by the selected case.
4. Delegate coding of the selected case through `$code-test-case` and prove its executed red state.
5. Delegate greening through `$fix-red-case`.
6. Delegate refactoring of the bounded red-plus-green increment through `$refactor-case`.

Apply the detailed contract and outputs for each stage from `references/stage-contracts.md`.

## Commits

The coordinator owns every commit.
Immediately before each commit, reload and follow project-local Git conventions.
Stage only verified increment-owned paths or hunks.
Never use a broad staging command that can include unrelated changes.

After approval of a proven red stage, commit together:

- the selected test;
- required test infrastructure;
- minimal compile-only production surface;
- approved task, case, API, and solution artifacts.

After approval of the green stage, create a separate commit containing only the coherent production change and compile-required production call-site propagation.

After final approval of the refactor result, update the matching `todo.md` item and create a separate commit containing only the refactoring and task-status update.
Mark only the selected increment complete.
When its todo item also covers later behavior, preserve that pending scope and record completion at a narrower child item.
Stop if the matching status update is ambiguous.
When refactoring is a no-op, commit the task-status update alone.
Do not create an empty commit.

Before and after every commit, verify `HEAD`, status, staged diff, resulting commit diff, and preservation of unrelated changes.

## Already-green case

If the selected test compiles and already passes, do not weaken it, create an artificial failure, or label any commit as red.
Stop for the normal stage review.
After approval, update the matching `todo.md` item and create one explicitly non-red commit for the approved test, test infrastructure, minimal compile-only production surface, design artifacts, and task-status update.
Skip green and refactor for that increment, then return to selection.
Do not create the commit when it would be empty.

## Refactor review

Apply the refactor stage's nested pre-edit plan approval from `references/stage-contracts.md`.
After the refactor result is complete, apply the normal final stage review before updating `todo.md` or committing.

## Stop conditions

Stop and leave the current stage active with `status: pending` or `status: blocked`, as defined by its contract, when:

- the increment is ambiguous;
- the briefs, `todo.md`, artifacts, code, or verified behavior conflict;
- the vertical slice must be widened beyond the approved increment;
- an unrelated change overlaps the increment;
- expected red cannot be proven;
- green requires changing the selected test or its intent;
- a subagent does not finish, in which case leave the stage active with `status: pending`;
- a subagent's result cannot be independently verified.

Preserve already verified commits when stopping.
Report the verified completed stages, current active stage and status, worktree state, and exact blocker.

Finish only when the briefs and `todo.md` contain no remaining unimplemented behavior.

## Output

At every review gate, report the task directory, increment, current stage, status, outcome or pending reason, verified Git state, changed files, verification result, and the approval needed.
At completion, report the commits created, completed increments, final verification, remaining unrelated changes, and why no unimplemented behavior remains.
