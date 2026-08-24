# TDD stage contracts

Use these contracts only from `$implement-task-tdd`.

## Responsibility boundary

The invoked stage skill owns semantic correctness, evidence interpretation, and its `status` and `outcome` classification.
The coordinator owns protocol, state transitions, Git isolation, write-set enforcement, required-command observation, review gates, and commits.
The coordinator does not reproduce stage reasoning.

## Shared handoff

Give every stage subagent:

- `task_dir` and relevant task artifacts;
- verified `HEAD`, staged and unstaged paths, and unrelated changes to preserve;
- the preceding approved stage result;
- allowed write set and forbidden actions;
- required validation and output.

Require every stage subagent to return:

- `status`: `complete`, `pending`, or `blocked`;
- evidence used;
- files changed;
- commands run and observed results;
- `outcome` when complete;
- remaining blocker or uncertainty.

## Stages

### 1. Select increment

Invoke `$select-next-increment`.
Allow no file changes.
Accept `status: complete` only with `outcome: increment-selected` or `outcome: no-unimplemented-behavior`.

### 2. Design case

Invoke `$design-test-case` with the approved increment and `<task-dir>/030-test-cases-new.md` as its output path.
Allow changes only to that artifact.
Accept `status: complete` only with `outcome: case-designed`.

### 3. Align required design

Invoke `$align-required-design` with the selected case, task directory, and explicit target artifact paths.
Allow changes only to required task, target API, target test-case, solution, and implementation-design artifacts.
Accept `status: complete` only with `outcome: required-design-aligned`.

### 4. Code and prove red

Invoke `$code-test-case` with the selected case, required design, and explicit Kotlin test path.
Allow changes only to the selected test, required test infrastructure, and compile-only production surface allowed by that skill.
Require reported compilation and exact-test execution commands.
Accept `status: complete` only with `outcome: expected-red` or `outcome: already-green`.

### 5. Plan production fix

Invoke `$plan-test-case-fixing` with the approved red-stage result and task directory.
Allow changes only to `<task-dir>/010-task-brief.md`, `<task-dir>/030-solution-brief.md`, `<task-dir>/030-implementation-design.md`, and `<task-dir>/030-implementation-structure.yaml`.
Require the exact selected-test command, reusable production-fix plan, validated `structure-chart/v1` source, and its rendered Mermaid diagram.
Accept `status: complete` only with `outcome: fix-planned` and no unresolved questions or blockers.

### 6. Make green

Invoke `$fix-red-case` with the approved production-fix plan.
Allow production-code changes only.
Require the exact selected-test command.
Accept `status: complete` only with `outcome: selected-test-passes`.

### 7. Refactor increment

Invoke `$refactor-case` with the red and green boundary commits.
Use the net diff from the red commit's parent through the green commit.
Allow changes only within the coordinator-approved refactor write set and forbid `todo.md` changes.

When the skill returns `status: pending` with `pending_reason: refactor-plan-approval`, stop for approval and then resume the same subagent.
Require the exact selected-test command for a completed result.
Accept `status: complete` only with `outcome: refactored` or `outcome: no-op`.

## Mechanical verification

After every subagent:

- verify that `HEAD` did not change and inspect the latest commit;
- inspect staged and unstaged status and diffs;
- verify every path and hunk changed since the pre-stage snapshot is within the stage write set;
- verify earlier approved and unrelated changes remain preserved where practical;
- verify every required command was actually run;
- rerun the required compile or exact-test command for stages 4-7;
- compare only the observed command state with the reported outcome.

For `expected-red` and `fix-planned`, require successful compilation and an executed failing selected test.
For `fix-planned`, also require the plan-contract fields, successful structure-chart validation and rendering commands, and no unresolved questions or blockers.
For `already-green`, `selected-test-passes`, `refactored`, and `no-op`, require the selected test to pass.
Do not independently classify the failure cause or reassess selection, design, alignment, minimality, or remaining behavior.
Do not advance on report-only evidence or any mechanical mismatch.
