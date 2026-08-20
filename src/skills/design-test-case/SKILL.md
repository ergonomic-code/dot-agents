---
name: design-test-case
description: Design one test-method-sized `verification-check-format-v0.1` full-mode check from a requirement, bug report, or desired behavior description.
---

# Design Test Case

Use this skill when the user gives a requirement, bug report, task brief, or desired behavior and needs one test-method-sized check, but has not already provided one selected full-mode verification check.

Read `../write-verification-check/SKILL.md`.
Read `framework_checkout_root/src/references/test-case-implementation-order.md`.

## Task artifact bindings

- human-readable artifact title: `Изменения тест-кейсов`

## Selection

Design exactly one test-method-sized target behavior check.
For bugs, select the corrected target behavior; use the broken behavior only as evidence of the violated obligation.
For new behavior, select the stable desired behavior and apply `framework_checkout_root/src/references/test-case-implementation-order.md` when several valid cases are implied.
If several independent obligations are implied and the target case is not selected, ask which one to design.
When one obligation maps a finite set of mutually exclusive input or context states to expected outcomes, design the complete set as named `Example`s under that one `Rule` unless the user explicitly selects a subset.

## Delegation

Before mapping `Feature`, resolve the verified object from explicit user input, an existing artifact `Feature`, a named endpoint, API surface, component, operation, or explicitly planned target surface.
If no verified object can be resolved, ask for the target surface instead of inventing a component-like SUT.
For new behavior, prefer the stable existing boundary or explicitly planned boundary over an inferred internal component.
When the verified object is an explicitly planned new SUT whose technical reference is not designed yet, write a provisional `Feature` without the parenthesized reference and leave its materialization to `$align-required-design`.
Do not ask the user for the missing technical reference during behavior design.
Carry technical and architecture choices into `$align-required-design`.
Ask only when unresolved observable product behavior prevents stating the selected `Rule` or `Example`.
Map the selected obligation to `Feature` and `Rule`, then to one `Example` or, when the finite-set rule applies, the complete set of named `Example`s, each with `Given`, `When`, and `Then`.
Then render through `../write-verification-check/SKILL.md`.
Do not add sibling rules or examples outside that selected obligation.

## Scope Boundary

This skill is design-only.
Do not create, modify, plan, or announce test code or production code.
After returning or writing the verification case stop.

## Output

When invoked by another skill with an explicit resolved output path, write the rendered case before returning it to that caller.
When invoked by another skill without a resolved output path, return the rendered case without writing files.
If the resolved output path is `030-test-cases-new.*`, update that cases artifact instead of returning the case inline.
In an existing cases artifact, add only the new case under the added-cases section.
If that section already contains a source block for the same `Feature`, insert only the new `Rule` into that block.
Otherwise add one source block in the artifact's existing container format.
Preserve all other sections and cases.
If the resolved output path is not a cases artifact, write only the case text to that file.
If no output path is resolved, return only one full-mode `verification-check-format-v0.1` case, or the missing selection issue.

When invoked by another skill, return `status: complete` with `outcome: case-designed` only after writing the valid rendered case to the requested artifact.
Return `status: blocked` with the exact missing selection, behavior, or artifact issue otherwise.

## Before Finishing

Read `../../artifacts/verification-check-format-v0.1/references/requirements-coverage-checklist.md` and apply it within the selected obligation.
