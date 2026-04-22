---
name: fix-project-context
description: Analyze a project-context problem from `problem`, `target behavior`, and optional `codex session id`; load `project-context-engineer`; propose `minimal`, `systemic`, and `optimal` fixes; wait for explicit choice; then implement it.
---

# Fix project context

Read `../fix-framework-context/references/minimality.md`.
Read `../fix-framework-context/references/shared-workflow.md`.

This skill always resolves the role to `project-context-engineer`.
Before task triage, load `framework_checkout_root/src/roles/project-context-engineer.md`.
If that file is missing, say so and stop.

Treat editable roots as:
- `./AGENTS.md`
- project-local `./.agents/**` outside `framework_checkout_root/**` and `./devlog/**`
- project-local `./.codex/**` outside `framework_checkout_root/**` and `./devlog/**`
- `./README.md` only when it is an active agent-facing entry point or the narrowest consistent location.

If the case is about framework-provided context under `framework_checkout_root/src/**`, stop and tell the user to use `$fix-framework-context`.
If the case is about feature-local context under `./devlog/**`, stop and tell the user to use `$fix-feature-context`.

## Skill-specific scope and classification

Work from the smallest relevant project context file set under:
- `./AGENTS.md`
- project-local `./.agents/**` outside `framework_checkout_root/**` and `./devlog/**`
- project-local `./.codex/**` outside `framework_checkout_root/**` and `./devlog/**`
- `./README.md` only when it is agent-facing or already part of the current context flow.

Classify each candidate by layer (`agents-root` | `agents-dir` | `codex-dir` | `readme` | `reference`).
