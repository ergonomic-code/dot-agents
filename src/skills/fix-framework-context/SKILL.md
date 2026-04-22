---
name: fix-framework-context
description: Analyze a framework-context problem from mandatory `codex session id`, `problem`, and `target behavior`; load `framework-context-engineer`; propose `minimal`, `systemic`, and `optimal` fixes; wait for explicit choice; then implement it.
---

# Fix framework context

Read `references/minimality.md`.
Read `references/shared-workflow.md`.

This skill always resolves the role to `framework-context-engineer`.
Before task triage, load `framework_checkout_root/src/roles/framework-context-engineer.md`.
If that file is missing, say so and stop.

Treat editable roots as:
- `framework_checkout_root/src/**`

If the case is about current-repo `AGENTS.md`, or project-local `.agents/**` or `.codex/**` outside `framework_checkout_root/**`, stop and tell the user to use `$fix-project-context`.

## Skill-specific scope and classification

Work from the smallest relevant framework file set under `framework_checkout_root/src/**`.
Classify each candidate by layer (`project-baseline` | `roles-index` | `role` | `convention` | `skill` | `artifact` | `reference`).
