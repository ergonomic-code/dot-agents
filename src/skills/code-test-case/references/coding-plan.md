# Coding Plan

Use this read-only phase for one caller-selected verification check after input validation.
Treat its result as transient internal state of `$code-test-case`.
Do not write, edit, generate, or persist repository files or expose the plan as a separate capability or artifact.

Inspect only the repository evidence needed to make the selections below.

## Select the change

1. Use the check's SUT and the validated accompanying design decisions without selecting alternatives.
2. Apply the coding-time mapping in `test-case-selection.md`.
3. Select the governing production/API contract in this order:
   - a caller-supplied contract;
   - an existing contract that unambiguously governs the SUT;
   - compile-only surface mechanically determined by the check, supplied context, and repository conventions.
4. Select the required test APIs, fixtures, assertions, and other test support from existing repository patterns, or define the smallest convention-compliant additions.
5. For `new`, derive the test container and repository path from the recorded kind and SUT, and derive the case shape from the recorded form and `test-naming.md`.
6. For `strengthen` or `extend-parameterized`, resolve the recorded file, container, and case exactly; do not search for a different target.
7. Select the minimal compile-only production surface required for the test to compile without implementing the selected behavior.
8. Select the narrowest compile command and exact test selector that identify the selected case, plus the command that executes that selector.
9. List every file implementation may change and classify each as test case, test support, or compile-only production surface.
10. Verify that every selected change is inside the repository binding and authorized artifact kinds.

## Blockers

Report a blocker instead of selecting an implementation when:
- the SUT, governing contract, target container, case mapping, exact selector, or permitted write set is ambiguous;
- the selected check and supplied contract conflict;
- a new or changed public contract has several valid designs and the caller supplied none;
- compilation requires production behavior or production surface that is not mechanically determined;
- required test support cannot be designed from the check and applicable conventions;
- reliable compilation or exact-case execution cannot be selected within the repository binding.

Return the selections or the blocker to `$code-test-case` without changing repository state.
