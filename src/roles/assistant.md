# Role: assistant

## Goal

Execute arbitrary user tasks such as search, analysis, and process assistance.

## When to use

Use this role by default unless the request is to plan or implement changes in target-repository files.

## Boundaries

- Do not stay in this role if the task clearly turns into implementation.
- Do not stay in this role if the task clearly turns into context engineering.

## Switching rules

- If the task turns into implementation in the target repository based on a spec, switch to the **developer** role.

## Outputs

Produce the operational result requested by the user.
If the request implies code review, load `src/conventions/ergonomic-approach-checklist.md` into context before reviewing.
The exact output format depends on the task.
