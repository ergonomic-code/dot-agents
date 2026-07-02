---
name: reviewing-framework-context-file-changes
description: Review changes in framework context files for conciseness, minimality, task fit, framework integration, ambiguity, actionability, verifiability, contradictions, scope clarity, and non-English text. Use when Codex reviews diffs or changed files in `.agents/`, `src/project-baseline.md`, `src/conventions/`, `src/roles/`, or framework templates.
---

# Review framework context file changes

## Scope

Treat these as framework context files:

- `.agents/**`
- `src/**`
- `AGENTS.md`
- `skills/installing-framework/**`

## Input

- diff or changed files
- original task

If the original task is not explicit:

- use `$finding-codex-session` to locate recent session candidates
- read only material turns from candidate sessions
- show the likely task or concise alternatives to the user
- continue only after the user confirms the task
- if no likely task is found, ask the user for it

## Checks

Check that changes are:

- written in English unless the file explicitly requires another language
- effective for the stated task
- integrated into the framework
- concise
- non-duplicating
- unambiguous
- actionable by an agent
- verifiable from files or output
- non-contradictory to existing framework files
- clear in scope of applicability
- sufficient to detect under-typed data structures when changed code represents domain states, variants, or semantic subgroups with correlated nullable fields

## Integration

Verify:

- names, paths, and links are correct
- new files are reachable from existing entry points when needed
- old files were updated when new files replace or extend them
- no orphan files were introduced

## Output

Return:

- verdict: `ok` | `ok_with_notes` | `needs_fix`
- findings list

For each finding include:

- severity: `major` | `minor`
- file
- issue
- why it is a problem
- minimal fix, including suggested English wording for non-English text

## Review rule

Prefer deletion, shortening, reuse, and direct fixes over expansion.
Treat ambiguity, non-actionability, non-verifiability, contradiction, unclear scope, missing integration, and unintended non-English text as defects.
For non-English text findings, suggest an English rewrite that preserves intent and maximizes inference impact.
Do not praise.
Report only real issues.
