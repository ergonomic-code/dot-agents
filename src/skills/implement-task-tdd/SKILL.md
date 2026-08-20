---
name: implement-task-tdd
description: Coordinate a task directory through reviewed vertical TDD increments, delegating each stage to a separate sequential subagent and owning workflow state, Git isolation, and commit boundaries. Use when the user asks to implement a task, todo, or briefs end to end through TDD with review gates.
---

# Implement Task with TDD

Read `framework_checkout_root/src/roles/developer.md`.
Read `framework_checkout_root/src/conventions/process/tasks.md`.
Read `references/stage-contracts.md`.

## Input

Require one task directory resolved through `framework_checkout_root/src/conventions/process/tasks.md`.
Require `<task-dir>/010-task-brief.md`, `<task-dir>/030-solution-brief.md`, and `<task-dir>/todo.md`.
If any required file is missing, stop and name it.

Before the first stage and immediately before every later stage:

- read the current task artifacts needed for the handoff;
- inspect `HEAD`, Git history, staged and unstaged changes;
- identify and preserve unrelated changes;
- record the verified state and allowed write set.

Record non-overlapping human-approved commits since the last verified state and include them in the later refactor range.
Stop on unauthorized drift or when unrelated changes overlap the next stage.
Do not clean, restore, stash, stage, or commit unrelated changes.

## Coordination

The coordinator owns workflow state, review gates, Git isolation, write sets, and commits.
Each stage skill owns the semantic correctness of its result.
Do not repeat its selection, design, failure-cause, minimality, alignment, or completion reasoning.

Run stages strictly through this state machine:

1. `$select-next-increment`
2. `$design-test-case`
3. `$align-required-design`
4. `$code-test-case`
5. `$fix-red-case`
6. `$refactor-case`

Run stages sequentially and never in parallel.
Run each stage in a new separate subagent, except when resuming an approved refactor plan.
If separate subagents are unavailable, stop.
Do not let subagents commit.

Give each subagent the fresh handoff, write set, stop conditions, and required output from `references/stage-contracts.md`.
After it returns, apply only the mechanical verification defined there.
Advance only when the stage reports `status: complete` and mechanical verification passes.

After each completed stage, report the result and stop for explicit human approval, except for the green-to-refactor transition.
Approval authorizes only the transition and commit defined by this skill.
On `pending` or `blocked`, keep the same stage active and stop.
Rerun a continued stage in a new subagent after fresh state verification, except that approval of a refactor plan resumes the same subagent.

## Commits

The coordinator owns every commit.
Immediately before each commit, reload and follow project-local Git conventions.
Stage only verified increment-owned paths or hunks.
Never use broad staging commands.

After approval at a review gate, commit only the changes approved at that gate before starting the next stage.
If the completed stage made no file changes, do not create an empty commit.

After approval of `case-designed`, commit only the case artifact.
After approval of `required-design-aligned`, commit only the changed design artifacts.
After approval of `expected-red`, commit together:

- the selected test;
- required test infrastructure;
- minimal compile-only production surface.

After a mechanically verified green stage, create a separate commit containing only the production change and compile-required production call-site propagation.
Then immediately start refactoring without another review gate.

After final approval of the refactor result, update the matching `todo.md` item and create a separate commit containing only the refactoring and task-status update.
Mark only the selected increment complete.
If its todo item covers later behavior, preserve that scope in a narrower pending child item.
Stop if the status update is ambiguous.
For a no-op refactor, commit only the task-status update.
Do not create an empty commit.

Before and after every commit, verify `HEAD`, status, staged diff, resulting commit diff, and preservation of unrelated changes.

## Already-green case

After approval of `already-green`, update the matching `todo.md` item and create one explicitly non-red commit containing only the approved test, test infrastructure, compile-only production surface, and task-status update.
Skip green and refactor, then return to selection.
Do not create an empty commit.

## Refactor review

Treat green-to-refactor as a continuous transition.
Apply the refactor stage's nested pre-edit plan approval from `references/stage-contracts.md`.
After refactoring completes, apply the normal review gate before updating `todo.md` or committing.

## Stop conditions

Stop with the current stage active when:

- the stage reports `pending` or `blocked`;
- mechanical verification fails, with workflow status `blocked`;
- unauthorized drift appears, with workflow status `blocked`;
- unrelated changes overlap the stage write set, with workflow status `blocked`;
- the subagent does not finish, with workflow status `pending`.

Preserve verified commits when stopping.
Report completed stages, active stage and status, worktree state, and exact blocker.

Finish when `$select-next-increment` reports `outcome: no-unimplemented-behavior` and mechanical verification passes.

## Output

At every review gate, report the task directory, increment, stage, status, outcome or pending reason, verified Git state, changed files, mechanical verification, and approval needed.
For green-to-refactor, report the same state as a progress update without requesting approval.
At completion, report created commits, completed increments, final verification, and remaining unrelated changes.
