# TDD stage contracts

Use these contracts only from `$implement-task-tdd`.

## Shared handoff

Give every stage subagent a handoff containing:

- `task_dir`;
- task brief, solution brief, `todo.md`, and relevant task artifacts;
- verified `HEAD`, staged paths, unstaged paths, and unrelated changes to preserve;
- selected increment, external boundary, final observable effect, and exclusions when available;
- preceding stage result and unresolved findings when available;
- allowed write set and forbidden actions;
- required validation and output.

Require the subagent to return:

- `status`: `complete`, `pending`, or `blocked`;
- evidence used;
- files changed;
- commands run and their results;
- `outcome`: the stage-specific result when `status` is `complete`;
- remaining blocker or uncertainty.

Subagent output is evidence to verify, not proof of completion.

## 1. Select increment

Allow no file changes.
Invoke `$select-next-increment` with the task directory and shared handoff.
Before independent verification, read `framework_checkout_root/src/skills/select-next-increment/SKILL.md` and its referenced selection policy.
Verify the returned result against that contract and the actual task evidence.
Return the full result unchanged.

## 2. Design case

Allow no code changes.
Invoke `$design-test-case` with the approved increment and relevant artifacts.
Treat the approved increment as selected and do not add sibling obligations.
Return `status: complete` with `outcome: case-designed` and exactly one full-mode test-method-sized case or one allowed complete parameterized set.
Return the rendered case to the coordinator without writing files.

## 3. Design required APIs

Allow changes only to task, target API, target test-case, and solution artifacts.
Write the approved case into the corresponding target test-case artifact.
Inspect the public contract, production types and signatures, and test-side `*HttpApi`, `*TestApi`, fixtures, and presets required by that case.
Design only missing or changed surfaces required to compile and execute the selected case.
When the case requires a new or changed JSON-over-HTTP public contract, invoke `$describe-rest-api` and use its validated IR and rendered target artifact.
Limit that contract change to the selected case.
Update the corresponding task, API, and solution artifacts with those surfaces.
Create a new convention-compliant `030-*` artifact only when no current target artifact can own the required design.
Do not change requirements to make the selected case easier.
Return `status: blocked` when a required surface is unsupported by or conflicts with the briefs.

Do not write production code, test code, build configuration, migrations, schemas, or generated code.
Do not add APIs for later increments.
Return `status: complete` with `outcome: api-surfaces-aligned`, changed artifacts, and an explicit no-change result for each surface category already covered by existing design.

## 4. Code and prove red

Resolve the target Kotlin test file and invoke `$code-test-case` with its explicit path, the approved case, and API design.
For a new file, require its workflow-invoked generate mode to write the generated code to that path.
Allow changes only to the selected test, required test infrastructure, and minimal compile-only production surface permitted by that skill.
Do not change production behavior.
Require `$code-test-case` to compile and execute the exact selected test and classify its behavior state.
Do not accept compilation failure, fixture failure, environmental failure, or an unrelated assertion as red.
Do not weaken the test to manufacture the expected failure.

Return `status: complete` with exactly one outcome:

- `outcome: expected-red`, with the observed failure and its connection to the selected behavior;
- `outcome: already-green`, with the passing command and evidence.

Return `status: pending` only when execution evidence is incomplete or a verified transient environmental failure can be retried without file changes.
Return `status: blocked` for a compilation failure, fixture failure, unrelated assertion, non-transient environmental failure, or when the case or API design must change.

## 5. Make green

Invoke `$fix-red-case` only for a proven and approved red case.
Allow production-code changes only.
Preserve the selected test and its intent unchanged.
Make the smallest coherent production change for the approved vertical slice, including a contract-complete constant implementation when sufficient.
Do not implement later variants or obligations.

Run the selected test.
Return `status: complete` with `outcome: selected-test-passes` only when the same selected test passes.
Return `status: pending` only when implementation or verification is interrupted while further work remains inside the same boundary.
Return `status: blocked` if green requires widening the increment or changing the test.

## 6. Refactor increment

Invoke `$refactor-case` with the red and green boundary commits as one bounded TDD increment.
Use the net diff from the red commit's parent through the green commit so the range includes the red commit and every intervening commit.
Allow no behavior or test-intent changes.
When editing, keep its one-mode-per-iteration rule.

If there is no useful narrow refactoring, make no edits, run the selected test, and return `status: complete` with `outcome: no-op`.
Otherwise, before edits, return `status: pending` with `pending_reason: refactor-plan-approval` and the required refactor plan.
After approval, resume the same subagent.
Run the selected test after edits.
Do not update `todo.md`; the coordinator updates it only after final human review.
Return `status: complete` with `outcome: refactored` or `outcome: no-op` only after the required verification passes.
Return `status: pending` when verification is incomplete, or `status: blocked` when refactoring would violate this boundary.

## Independent verification

After every subagent, compare actual state with the pre-stage handoff:

- verify `HEAD` and inspect the latest commit to detect unauthorized commits;
- inspect staged and unstaged status and diffs;
- attribute every changed hunk to the approved write set;
- confirm unrelated user changes are byte-for-byte preserved where practical;
- rerun the narrowest required compile or test command;
- compare the observed result with the stage-specific completion condition.

Do not advance on report-only evidence.
