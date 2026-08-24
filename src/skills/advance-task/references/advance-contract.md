# Advance task stage contract

Select and execute one stage per `$advance-task` invocation.
Use current-session outcomes only when they identify the task directory, selected step, affected paths, and validation evidence unambiguously.
If evidence supports several stages or skips an unverified prerequisite, return `status: blocked` instead of guessing.

## Shared boundary

Keep every stage inside one selected task step.
For test-eligible behavior, keep the step inside one test-method-sized vertical increment.
Preserve later behavior and unrelated changes.
Do not create commits or use subagents.
Do not treat a stage as complete until its completion evidence has been independently checked against the current repository state.

## Stage order

### 1. Select increment

Select this stage when unfinished task work remains and no current step selection is proven.
Load and follow `framework_checkout_root/src/skills/select-next-increment/SKILL.md` without permitting writes.
Complete with `outcome: increment-selected`, `outcome: non-test-step-selected`, or `outcome: no-unimplemented-work` only when that skill's evidence contract is satisfied.

### 2. Execute non-test step

Select this stage when `non-test-step-selected` is proven and its result is not complete.
Follow `framework_checkout_root/src/references/non-test-task-step.md` directly.
Permit only the selected production or task-artifact write set and mechanically required adaptations of existing behavior tests.
Complete only with `outcome: non-test-step-complete` after verifying the selected result, commands, actual diff, and absence of new or changed coverage of the selected detail.

### 3. Complete non-test step

Select this stage when `non-test-step-complete` is proven and the matching task status is still pending.
Reverify the result and update only the matching `todo.md` item and any task artifact whose status would otherwise contradict it.
Return `status: blocked` when the matching status update is ambiguous.
Complete with `outcome: non-test-step-status-complete`, then stop before selecting another step.

### 4. Design case

Select this stage when one increment is selected and no matching complete verification case is proven.
Load and follow `framework_checkout_root/src/skills/design-test-case/SKILL.md` for exactly one test-method-sized case or one allowed complete parameterized set.
When a task directory resolves, use `<task-dir>/030-test-cases-new.md` as the explicit target test-case artifact and write the case before completing the stage.
Otherwise return the case in the stage result for reuse in the current session.
Accept a provisional `Feature` only for an explicitly planned new SUT and carry its missing technical reference into `$align-required-design`.
Complete only when the rendered case satisfies that skill's final checklist.

### 5. Align required design

Select this stage only when the designed case proves that a public contract, production type or signature, test API, fixture, preset, or configuration surface must be added or changed before the case can be coded, including when its `Feature` is provisional.
Load and follow `framework_checkout_root/src/skills/align-required-design/SKILL.md` with the selected case, task directory, and target artifact paths.
Complete only with that skill's `outcome: required-design-aligned` and an explicit result for every required surface.
Return `status: blocked` only for the unresolved product behavior, approved-artifact conflict, or scope widening reported by that skill.
Skip this stage when the existing design already covers the selected case.

### 6. Code and verify case

Select this stage when the case and required design are complete but the selected Kotlin test is absent or not aligned, or no current executed result proves its behavior state.
Do not select it while the selected `Feature` is provisional.
Resolve one explicit target test path and load and follow `framework_checkout_root/src/skills/code-test-case/SKILL.md`.
Permit only the selected test, required test infrastructure, and compile-only production surface allowed by that skill.
When the selected test is already aligned and only its behavior state is unproven, permit no file changes.
Complete with `outcome: expected-red` only when the test compiled, executed, and failed because the selected behavior is missing.
Complete with `outcome: already-green` only when the selected case passes.
Return `status: pending` only for incomplete execution evidence or a verified transient environmental failure that can be retried without file changes.
Return `status: blocked` for a compilation failure, fixture failure, unrelated assertion, or non-transient environmental failure; name the invalidated prerequisite and the earliest stage that must be repeated.

### 7. Plan production fix

Select this stage when `expected-red` is proven and no current production-fix plan resolves for the selected case.
Load and follow `framework_checkout_root/src/skills/plan-test-case-fixing/SKILL.md`.
Permit only brief updates explicitly allowed by that skill.
Complete with `outcome: production-fix-planned` only when the plan has no unresolved questions and includes the selected case, failure evidence, diagnosed cause, behavior boundary, selected fix, target production areas, and verification command.

### 8. Make green

Select this stage when `expected-red` and a current production-fix plan are proven.
Load and follow `framework_checkout_root/src/skills/fix-red-case/SKILL.md`, passing the verified plan explicitly.
Permit production-code changes only and preserve the selected test unchanged.
Complete with `outcome: selected-test-passes` only when the same selected test passes.

### 9. Refactor increment

Select this stage when the selected case is green after production changes and the bounded increment has not received a completed refactor review.
Resolve the current increment diff from changes attributed to its case, production fix, and required design without including unrelated worktree changes.
Return `status: blocked` when that boundary cannot be isolated.
Load and follow `framework_checkout_root/src/skills/refactor-case/SKILL.md` against only that current increment diff.
Honor its nested approval before any refactor edit.
Return `status: pending` while that approval or refactor verification is outstanding.
Complete with `outcome: refactored` or `outcome: no-op` only after the selected test passes.
Skip this stage for `already-green` when the increment has no production change to review.

### 10. Complete increment

Select this stage after `already-green`, or after the green and refactor stages are complete.
Rerun the selected test before changing task status.
Update only the matching `todo.md` item and any task artifact whose status would otherwise contradict it.
Mark only the selected increment complete.
When one todo item also covers later behavior, preserve that scope and add or update a narrower child item.
Return `status: blocked` when the matching status update is ambiguous.
Complete with `outcome: increment-complete`, then stop before selecting another increment.

## Repeated invocation

On the next invocation, verify state again from current evidence.
Do not rely on the previous stage's intended outcome when repository state or current execution contradicts it.
When prior conversational evidence is unavailable, repeat a safe read-only stage or verification rather than assuming it completed.
