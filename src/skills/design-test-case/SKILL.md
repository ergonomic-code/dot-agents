---
name: design-test-case
description: Design one `verification-check-format-v0.1` full-mode test case from a requirement, bug report, or desired behavior description.
---

# Design Test Case

Use this skill when the user gives a requirement, bug report, task brief, or desired behavior and needs one test case, but has not already provided one selected full-mode verification check.
Read `../write-verification-check/SKILL.md`.
Read `references/implementation-order.md`.

## Selection

Design exactly one materially distinct target behavior case.
For bugs, select the corrected target behavior; use the broken behavior only as evidence of the violated obligation.
For new behavior, select the stable desired behavior and apply `references/implementation-order.md` when several valid cases are implied.
If several independent obligations are implied and the target case is not selected, ask which one to design.

## Delegation

Map the selected obligation to `Feature`, `Rule`, optional named `Example`, `Given`, `When`, and `Then`.
Then render through `../write-verification-check/SKILL.md`.
Do not add sibling rules or examples unless the user explicitly asks for more than one case.

## Output

Return only one full-mode `verification-check-format-v0.1` case, or the missing selection issue.
If an output path is resolved, write only the case text to that file.
