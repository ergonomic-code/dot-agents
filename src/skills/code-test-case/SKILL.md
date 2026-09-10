---
name: code-test-case
description: Transform one caller-selected verification check into one repository change containing a compilable Kotlin JUnit test case, then prove it expected red, already green, or blocked.
---

# Code Test Case

## Purpose

Transform one caller-selected verification check into one repository change containing one compilable Kotlin JUnit test case.
Keep the case strict and verify its current behavior state.

Read `framework_checkout_root/src/conventions/test-case-selection.md`.
Read `framework_checkout_root/src/conventions/test-naming.md`.

## Input

Accept:
- one caller-selected verification check;
- accompanying design decisions: selected test kind, form, target disposition (`new`, `strengthen`, or `extend-parameterized`), and the exact repository file, container, and method for an existing target;
- a repository binding, including the authorized output destination and artifact kinds;
- an optional existing production/API contract or caller-supplied design/API contract.

The invocation context may supply the repository binding and output authorization.
Validate the check against `framework_checkout_root/src/artifacts/verification-check-format-v0.1/ARTIFACT.md` and its applicable `full`-mode references before planning.

## Output

Return exactly one outcome:
- `expected-red` when the exact selected test compiles, executes, and fails because its required behavior is absent;
- `already-green` when the exact selected test compiles, executes, and passes;
- `blocked` for invalid or ambiguous input, unresolved design, unauthorized changes, unreliable verification, or a failure that is not the selected missing behavior.

Report changed files, the compilation command, the execution command, the exact test selector, the observed result, and the evidence connecting the result to the outcome.
For `blocked`, report the blocker and any completed evidence without claiming a behavior state.

## Workflow

1. Validate that the selected check is one unambiguous full-mode case with a technical SUT anchor and observable obligation.
2. Validate the accompanying design decisions: the SUT must match the selected kind, the examples must match the selected form, and an existing target must resolve exactly.
   In a merged artifact block, use only the verification and examples explicitly selected by those decisions; return `blocked` if their scope is ambiguous.
   Return `blocked` for missing or conflicting decisions; do not select them again or require them as fields in the verification-check format.
3. Produce the internal read-only plan through `references/coding-plan.md`.
4. If planning reports a blocker, return `blocked` without materializing changes.
5. Materialize only the planned test case, test support, and compile-only production surface using the context routed for the planned write set.
6. For `strengthen` or `extend-parameterized`, update only the recorded existing case.
   For `new`, create or use only the mechanically derived container at the authorized path.
   Preserve unrelated declarations and do not delete unrelated tests.
7. Apply the routed final checks, compile the exact selected test, and then execute that exact test.
8. Return `expected-red`, `already-green`, or `blocked` according to the observed evidence.

## Boundaries

- Treat the recorded target disposition as immutable design input, not an internal planning decision.
- The skill may select test-support APIs, fixtures, and assertions; for `new`, derive the container, path, and method name through `test-naming.md`, and for an existing target preserve its recorded location and identifier.
  Implement the case shape recorded by the test form.
- Use an existing production/API contract or materialize a caller-supplied contract.
- Derive compile-only production surface only when its shape is mechanically determined by the check, supplied design context, and repository conventions.
- If a new or changed public contract has several valid designs and none is supplied, return `blocked`; do not invoke an API-design skill implicitly.
- Production changes are limited to planned symbols, signatures, types, constructors, fields, and compile-only call-site propagation.
- Do not implement production behavior or add persistence, integrations, migrations, configuration, generated documentation, or other behavior-bearing production changes.
- Return `blocked` for compilation failures outside the planned compile-only surface, fixture or test-support failures, unrelated assertion failures, environmental failures preventing reliable verification, or required writes outside the authorization.
- Do not weaken, rewrite, skip, or delete the selected check to manufacture expected red.
- Do not resolve tasks, task directories, progress, commits, or workflow state.
