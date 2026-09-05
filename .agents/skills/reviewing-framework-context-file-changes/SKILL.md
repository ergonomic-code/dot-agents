---
name: reviewing-framework-context-file-changes
description: Review changes in framework context files for conciseness, minimality, task fit, framework integration, ambiguity, actionability, verifiability, contradictions, scope clarity, and language consistency. Use when Codex reviews diffs or changed files in `.agents/`, `src/project-baseline.md`, `src/context/`, `src/conventions/`, `src/roles/`, framework templates, or `README.md`.
---

# Review framework context file changes

## Scope

Treat these as framework context files:

- `.agents/**`
- `src/**`
- `AGENTS.md`
- `README.md`
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

- written in the file's explicitly required language or, when none is specified, its established language; default new files to English
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
- `README.md` is updated when changes affect user-facing framework capabilities, installation, usage, supported scope, or documented entry points
- internal-only changes do not introduce speculative `README.md` edits
- dependency direction remains `baseline -> role`, `baseline -> context routing -> conventions and references`, `role -> skill`, and `skill -> intrinsic dependencies`
- the baseline reaches and orchestrates the root context index without duplicating topical conditions
- every topical index is reachable from the root, all matching indexes compose, and the index layer is neither deep nor split without an applicability boundary
- roles do not route engineering context
- generic skills do not route general task context, and their convention or reference dependencies are intrinsic to the skill
- conventions define rules rather than general applicability routing, with no routing conditions duplicated across layers
- every convention declares one to three YAML front-matter keywords, every rule in the file concerns every keyword, and rules with a different keyword intersection are split and routed independently
- selective routing preserves intersections without loading unrelated branches, including separating tests from production code
- generic skills under `src/skills/**` do not resolve tasks, discover task artifacts, choose task paths, or select or load roles
- task layout and progress knowledge is confined to `src/task-workdir/**`, whose skills are exempt from the generic-skill restriction
- task-workdir context is conditional and supplies concrete bindings to roles before generic skills receive semantic inputs and caller-selected outputs
- task-workdir-specific routing remains under `src/task-workdir/**`
- project-local context continues to compose through project `AGENTS.md`

## Output

Return:

- verdict: `ok` | `ok_with_notes` | `needs_fix`
- findings list

For each finding include:

- severity: `major` | `minor`
- file
- issue
- why it is a problem
- minimal fix, including suggested wording in the required or established language for unintended language deviations

## Review rule

Prefer deletion, shortening, reuse, and direct fixes over expansion.
Treat ambiguity, non-actionability, non-verifiability, contradiction, unclear scope, missing integration, context-layering violations, and unintended deviations from the required or established language as defects.
For language-consistency findings, suggest a rewrite in the required or established language that preserves intent and maximizes inference impact.
Do not praise.
Report only real issues.
