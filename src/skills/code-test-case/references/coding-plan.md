# Coding Plan

Use this read-only phase for one caller-selected verification check after input validation.
Treat its result as transient internal state of `$code-test-case`.
Do not write, edit, generate, or persist repository files or expose the plan as a separate capability or artifact.

Inspect only the repository evidence needed to make the selections below.

## Select the change

1. Select the SUT from the check's technical anchor, explicit target, supplied context, and existing code.
2. Select the governing production/API contract in this order:
   - a caller-supplied contract;
   - an existing contract that unambiguously governs the SUT;
   - compile-only surface mechanically determined by the check, supplied context, and repository conventions.
3. Select the required test APIs, fixtures, assertions, and other test support from existing repository patterns, or define the smallest convention-compliant additions.
4. Select the narrowest matching test container and its repository path.
5. Decide whether to match and conservatively update an existing case or add a new case.
6. Select the minimal compile-only production surface required for the test to compile without implementing the selected behavior.
7. Select the narrowest compile command and exact test selector that identify the selected case, plus the command that executes that selector.
8. List every file implementation may change and classify each as test case, test support, or compile-only production surface.
9. Verify that every selected change is inside the repository binding and authorized artifact kinds.

## Blockers

Report a blocker instead of selecting an implementation when:
- the SUT, governing contract, target container, case mapping, exact selector, or permitted write set is ambiguous;
- the selected check and supplied contract conflict;
- a new or changed public contract has several valid designs and the caller supplied none;
- compilation requires production behavior or production surface that is not mechanically determined;
- required test support cannot be designed from the check and applicable conventions;
- reliable compilation or exact-case execution cannot be selected within the repository binding.

Return the selections or the blocker to `$code-test-case` without changing repository state.
