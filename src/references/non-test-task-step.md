# Non-test task step

Use this contract only for a step classified by `$select-next-increment` as `non-test-step-selected`.

## Execution

- Execute under the developer role with the selected step, current task artifacts, verified Git state, unrelated changes, allowed write set, and required verification.
- Implement or verify only the selected technical result.
- Keep the smallest production or task-artifact change that satisfies the selected step.
- Do not promote the selected detail into a requirement or test case to make it test-eligible.
- Do not create tests, test-case artifacts, assertions, or other persistent coverage for the selected detail.
- Change existing tests or test helpers only when mechanically required to keep existing behavior checks compiling and passing; add no new observation or assertion.
- Do not create a production surface used only for verification.
- Verify with applicable existing tests, compilation, static checks, or transient diagnostics.
- Keep transient diagnostic code and data outside tracked project files.
- If durable proof requires a new test, return `status: blocked` unless the user explicitly requested that specific test in the current conversation or an earlier explicit user request for it is unambiguously recorded in the task brief.
- Do not update `todo.md` or create commits during execution.

## Output

Return `status: complete` with `outcome: non-test-step-complete` only after the selected result and its verification are observed.
Report the intended result, changed files, commands and observed results, remaining uncertainty, and preserved unrelated changes.
Return `status: pending` for incomplete execution evidence that can continue without widening scope.
Return `status: blocked` when the result, write boundary, or verification cannot be completed under this contract.

## Completion

The caller verifies the actual diff, commands, absence of new or changed coverage of the selected detail, and preservation of unrelated changes.
Only after execution approval or an authorized later completion stage, the caller updates the matching `todo.md` item.
When the caller owns commits, it commits the verified implementation before creating a separate status commit.
When the caller owns commits and the step is verification-only, create only the status commit.
Do not mark broader or later work complete.
