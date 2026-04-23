---
name: fix-framework-context
description: Analyze a framework-context fix or feature request from `problem`, `target behavior`, and optional `codex session id`; load `framework-context-engineer`; propose `minimal`, `systemic`, and `optimal` changes; wait for explicit choice; then implement it.
---

# Fix or extend framework context

Read `references/minimality.md`.
Read `references/shared-workflow.md`.

This skill always resolves the role to `framework-context-engineer`.
Before task triage, load `framework_checkout_root/src/roles/framework-context-engineer.md`.
If that file is missing, say so and stop.

Treat editable roots as:
- `framework_checkout_root/src/**`

Treat framework-context fixes and new framework-context capabilities under `framework_checkout_root/src/**` as in scope.
For new capability work without a defect, treat the missing capability or limitation as the `problem`.

If the case is about current-repo `AGENTS.md`, or project-local `.agents/**` or `.codex/**` outside `framework_checkout_root/**` and outside `./devlog/**`, stop and tell the user to use `$fix-project-context`.
If the case is about feature-local context under `./devlog/**`, stop and tell the user to use `$fix-feature-context`.

## Skill-specific scope and classification

Work from the smallest relevant framework file set under `framework_checkout_root/src/**`.
Classify each candidate by layer (`project-baseline` | `roles-index` | `role` | `convention` | `skill` | `artifact` | `reference`).
