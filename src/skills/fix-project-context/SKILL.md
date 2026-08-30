---
name: fix-project-context
description: Analyze a project-context problem from `problem`, `target behavior`, and optional `codex session id` in the caller-selected `project-context-engineer` role; propose `minimal`, `systemic`, and `optimal` fixes; wait for explicit choice; then implement it.
---

# Fix project context

Read `framework_checkout_root/src/references/context-fix-minimality.md`.
Read `framework_checkout_root/src/references/context-fix-workflow.md`.

Require the caller to invoke this skill from the `project-context-engineer` role.

Treat editable roots as:
- `./AGENTS.md`
- project-local `./.agents/**` outside `framework_checkout_root/**`
- project-local `./.codex/**` outside `framework_checkout_root/**`
- `./README.md` only when it is an active agent-facing entry point or the narrowest consistent location.

If the case is about framework-provided context under `framework_checkout_root/src/**`, stop and tell the user to use `$fix-framework-context`.

## Skill-specific scope and classification

Work from the smallest relevant project context file set under:
- `./AGENTS.md`
- project-local `./.agents/**` outside `framework_checkout_root/**`
- project-local `./.codex/**` outside `framework_checkout_root/**`
- `./README.md` only when it is agent-facing or already part of the current context flow.

Classify each candidate by layer (`agents-root` | `agents-dir` | `codex-dir` | `readme` | `reference`).
