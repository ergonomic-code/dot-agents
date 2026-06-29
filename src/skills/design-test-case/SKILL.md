---
name: design-test-case
description: Design one `verification-check-format-v0.1` full-mode test case from a requirement, bug report, or desired behavior description.
---

# Design Test Case

Use this skill when the user gives a requirement, bug report, task brief, or desired behavior and needs one test case, but has not already provided one selected full-mode verification check.
Read `framework_checkout_root/src/conventions/feature-workdir.md`.
Read `framework_checkout_root/src/conventions/feature-stage-skill.md`.
Read `framework_checkout_root/src/conventions/feature-artifact-phases.md`.
Read `../write-verification-check/SKILL.md`.
Read `framework_checkout_root/src/references/test-case-implementation-order.md`.

## Feature artifact bindings

- artifact phase code: `030`
- default feature-dir output path: `<feature-dir>/030-test-cases-new.adoc`
- human-readable artifact title: `Изменения тест-кейсов`

## Selection

Design exactly one materially distinct target behavior case.
For bugs, select the corrected target behavior; use the broken behavior only as evidence of the violated obligation.
For new behavior, select the stable desired behavior and apply `framework_checkout_root/src/references/test-case-implementation-order.md` when several valid cases are implied.
If several independent obligations are implied and the target case is not selected, ask which one to design.

## Delegation

Map the selected obligation to `Feature`, `Rule`, optional named `Example`, `Given`, `When`, and `Then`.
Then render through `../write-verification-check/SKILL.md`.
Do not add sibling rules or examples unless the user explicitly asks for more than one case.

## Scope Boundary

This skill is design-only.
Do not create, modify, plan, or announce test code or production code.
After returning or writing the verification case and allowed progress checklist updates, stop.

## Output

When invoked by another skill as an internal step, return the rendered case to that caller and do not write files.
If the resolved output path is `030-test-cases-new.*`, update that cases artifact instead of returning the case inline.
In an existing cases artifact, add only the new case under the added-cases section.
If that section already contains a source block for the same `Feature`, insert only the new `Rule` into that block.
Otherwise add one source block in the artifact's existing container format.
Preserve all other sections and cases.
After updating a cases artifact, update the active feature `progress.md` when it exists.
Add the case under `## Реализация` or the matching `### Этап <feature-code>/<stage-code>: <название>` heading when an active stage is resolved.
Create only missing headings and TDD checklist entries.
Add one unchecked parent item named by the tested behavior.
Under it, add unchecked child items `красный кейс` and `зелёный кейс`.
If the resolved output path is not a cases artifact, write only the case text to that file.
If no output path is resolved, return only one full-mode `verification-check-format-v0.1` case, or the missing selection issue.
