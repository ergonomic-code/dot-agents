---
name: reviewing-framework-context-file-changes
description: Review changes in framework context files for conciseness, minimality, task fit, framework integration, ambiguity, actionability, verifiability, contradictions, and scope clarity. Use when Codex reviews diffs or changed files in `.agents/`, `src/project-baseline.md`, `src/conventions/`, `src/roles/`, or framework templates.
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
- original task, if available

## Checks

Check that changes are:

- concise
- minimal and non-duplicating
- effective for the stated task
- integrated into the framework
- unambiguous
- actionable by an agent
- verifiable from files or output
- non-contradictory to existing framework files
- clear in scope of applicability

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
- minimal fix

## Review rule

Prefer deletion, shortening, reuse, and direct fixes over expansion.
Treat ambiguity, non-actionability, non-verifiability, contradiction, unclear scope, and missing integration as defects.
Do not praise.
Report only real issues.
