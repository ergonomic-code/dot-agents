---
name: code-test-case
description: Transform one caller-selected verification check into one repository change containing a compilable Kotlin JUnit test case, then prove it expected red, already green, or blocked.
---

# Code Test Case

## Purpose

Transform one caller-selected verification check into one repository change containing one compilable Kotlin JUnit test case.
Keep the case strict and verify its current behavior state.

## Input

Accept:
- one caller-selected verification check;
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

1. Validate that the selected check is one unambiguous full-mode case with a technical SUT anchor and an observable obligation.
2. Produce the internal read-only plan through `references/coding-plan.md`.
3. If planning reports a blocker, return `blocked` without materializing changes.
4. Read `framework_checkout_root/src/conventions/tests.md` and materialize only the planned test case, test support, and compile-only production surface.
   Load production implementation conventions only when the plan includes production-surface changes.
5. When the target test container exists, match the selected case before adding it, preserve unrelated declarations, stop on ambiguous mapping, and do not delete unrelated tests.
   Otherwise create the planned container at the authorized path.
6. Apply the final checks loaded through the test convention index, compile the exact selected test, and then execute that exact test.
7. Return `expected-red`, `already-green`, or `blocked` according to the observed evidence.

## Boundaries

- Treat creation versus in-place update as an internal planning decision, not a public mode.
- The skill may select and design test-support APIs, fixtures, assertions, and the test container.
- Use an existing production/API contract or materialize a caller-supplied contract.
- Derive compile-only production surface only when its shape is mechanically determined by the check, supplied design context, and repository conventions.
- If a new or changed public contract has several valid designs and none is supplied, return `blocked`; do not invoke an API-design skill implicitly.
- Production changes are limited to planned symbols, signatures, types, constructors, fields, and compile-only call-site propagation.
- Do not implement production behavior or add persistence, integrations, migrations, configuration, generated documentation, or other behavior-bearing production changes.
- Return `blocked` for compilation failures outside the planned compile-only surface, fixture or test-support failures, unrelated assertion failures, environmental failures preventing reliable verification, or required writes outside the authorization.
- Do not weaken, rewrite, skip, or delete the selected check to manufacture expected red.
- Do not resolve tasks, task directories, roles, progress, commits, or workflow state.
