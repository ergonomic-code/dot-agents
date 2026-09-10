---
name: design-test-case
description: Design one test-method-sized `verification-check-format-v0.1` full-mode check from a requirement, bug report, or desired behavior description.
---

# Design Test Case

Use this skill when the user gives requirements, a bug report, or desired behavior and needs one test-method-sized check, but has not already provided one selected full-mode verification check.

Read `../write-verification-check/SKILL.md`.
Read `framework_checkout_root/src/conventions/ergonomic-approach-rules.md`.
Read `framework_checkout_root/src/conventions/test-design.md`.
Read `framework_checkout_root/src/conventions/test-case-selection.md`.
Read `framework_checkout_root/src/references/test-case-implementation-order.md`.

## Eligibility

Before designing, verify that the selected obligation is test-eligible under `framework_checkout_root/src/conventions/test-design.md`.
Accept an implementation detail only when the user explicitly requests that specific test or supplied requirements unambiguously record an earlier explicit request for it.
Do not treat progress, design context, an implementation step, or a verification instruction as a test obligation without an eligible requirement source.
Return `status: blocked` with `reason: not-test-eligible` when this condition is not met.

Design exactly one test-method-sized target behavior check.
For bugs, select the corrected target behavior; use the broken behavior only as evidence of the violated obligation.
For new behavior, select the stable desired behavior and apply `framework_checkout_root/src/references/test-case-implementation-order.md` when several valid cases are implied.
If several independent obligations are implied and the target case is not selected, ask which one to design.

## Design

1. Identify the selected observable obligation without fixing its technical SUT.
2. Discover the available test levels and select the test kind, evidence-backed SUT, and optional polymorphic variant through the design-time rules in `test-case-selection.md`.
3. Resolve the verified object for `Feature` from the selected SUT, explicit user input, existing artifacts, code, or supplied design.
4. Inspect existing and sibling tests and select the target disposition, examples, and test form together through `test-case-selection.md`, including the exact existing target anchor when applicable.
5. Map the selected obligation to `Feature` and `Rule`, then render the selected concrete example, concrete parameter set, or generated example class with `Given`, `When`, and `Then`.

If no candidate SUT can be resolved from the behavior and repository evidence, ask for the missing target instead of inventing one.
If no verified object can be resolved after selecting the SUT, ask for the missing object instead of inventing one.
When the verified object is an explicitly planned new SUT whose technical reference is not designed yet, stop and ask for that reference instead of writing a provisional `Feature`.
Otherwise ask only when unresolved observable product behavior prevents stating the selected `Rule` or `Example`.
Then render through `../write-verification-check/SKILL.md`.
Do not add sibling rules or examples outside that selected obligation.

## Scope Boundary

This skill is design-only.
Do not create, modify, plan, or announce test code or production code.
After returning or writing the verification case stop.

## Output

Accompany the check with concise coding decisions outside the verification-check block: selected kind, form, and whether to create, strengthen, or extend a parameterized case.
For an existing case, identify its repository-relative file, exact container, and source-level method; for a new case, leave the path to coding.
Pass these decisions to the caller along with the selected check; in an artifact, place them immediately before its block and identify the selected `Rule` and `Example` headers, or the sole unnamed example, and the selected assertion change for `strengthen`.

When invoked by another skill with an explicit resolved output path, write the rendered case before returning it to that caller.
When invoked by another skill without a resolved output path, return the rendered case without writing files.
When the caller identifies the output as an existing cases artifact, update it instead of returning the case inline.
In that artifact, write only the selected target check under the caller-selected cases section.
Merge into a block for the same `Feature` only when its kind, form, disposition, and target agree and the accompanying decisions still identify the exact selected verification and examples; otherwise add a separate block.
Within a compatible block, merge into the matching `Rule`, or insert the selected `Rule` when none matches.
Use the artifact's existing source-block format.
When merging, add only missing examples or strengthen only the selected verification; preserve existing examples and obligations, naming an unnamed example if it gains a sibling.
Preserve all other sections and cases.
If the resolved output path is not a cases artifact, write the check and accompanying coding decisions to that file.
If no output path is resolved, return one full-mode check with its coding decisions, or the missing selection issue.

When invoked by another skill, return `status: complete` with `outcome: case-designed` only after writing the valid rendered case to the requested artifact.
Return `status: blocked` with the exact missing selection, behavior, or artifact issue otherwise.

## Before Finishing

Read `../../artifacts/verification-check-format-v0.1/references/requirements-coverage-checklist.md` and apply it within the selected obligation.
