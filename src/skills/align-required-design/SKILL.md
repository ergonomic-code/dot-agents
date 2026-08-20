---
name: align-required-design
description: Design and record only the production and test-side interfaces, boundary data, and configuration required to code one selected verification check, then materialize any provisional Feature SUT reference. Use before test coding when a selected case requires a new or changed contract, helper surface, or configuration.
---

# Align Required Design

Read `framework_checkout_root/src/roles/developer.md`.
Read `framework_checkout_root/src/conventions/process/tasks.md`.
Read `framework_checkout_root/src/references/required-design-alignment.md`.

## Input

Require one selected full-mode `verification-check-format-v0.1` case.
Use an explicit task directory and artifact paths when provided.
When a task directory resolves, read its task brief, solution brief, current implementation design, target API, and test-case artifacts when present.

## Scope

Design only the production and test-side interfaces, boundary data, and configuration required to code the selected case.
When the case has a provisional `Feature`, design its missing SUT interface and append the resulting evidence-backed SUT reference to the target test-case artifact.
For a new or changed JSON-over-HTTP contract, invoke `$describe-rest-api` and use its validated IR and rendered target artifact.
Do not write production code, test code, build configuration, migrations, schemas, or generated code.
Do not widen the selected behavior or design implementation details beyond the required interfaces.

## Artifact Updates

When a task directory resolves, change only its task, target API, target test-case, solution, and implementation-design artifacts required by the selected case.
Keep the selected behavior unchanged while materializing a provisional `Feature`.
When no task directory resolves, return the aligned contracts and materialized `Feature` text; permit only the temporary API artifacts required by `$describe-rest-api`.

## Output

Return:

- `status`: `complete` or `blocked`;
- `outcome: required-design-aligned` when complete;
- one `reuse`, `add`, `change`, or `no-change` decision for every examined surface;
- the materialized `Feature` when the input was provisional;
- changed artifacts and validation performed;
- the exact unresolved product behavior, approved-artifact conflict, or required scope widening when blocked.

Do not return `required-design-aligned` while the selected case still has a provisional `Feature`.
