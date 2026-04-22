---
name: fix-feature-context
description: Analyze a problem in feature analysis or design artifacts from `problem`, `target behavior`, and optional `codex session id`; load `feature-context-engineer`; resolve the active feature workdir; propose `minimal`, `systemic`, and `optimal` fixes; wait for explicit choice; then implement it.
---

# Fix feature context

Read `../fix-framework-context/references/minimality.md`.
Read `../fix-framework-context/references/shared-workflow.md`.
Read `framework_checkout_root/src/conventions/feature-workdir.md`.

This skill always resolves the role to `feature-context-engineer`.
Before task triage, load `framework_checkout_root/src/roles/feature-context-engineer.md`.
If that file is missing, say so and stop.

Resolve the active feature directory via `feature-workdir.md`.
If no active feature directory is resolved, ask for the feature directory or feature id and stop.

Treat editable roots as:
- `<active-feature-dir>/**`

Preserve the artifact's human-facing role.
Prefer edits that make intent, decisions, constraints, boundaries, and open questions explicit enough to guide AI agents without turning the artifact into an AI-only prompt.

If the case is about framework-provided context under `framework_checkout_root/src/**`, stop and tell the user to use `$fix-framework-context`.
If the case is about current-repo `AGENTS.md`, or project-local `.agents/**` or `.codex/**` outside `framework_checkout_root/**` and outside `<active-feature-dir>/**`, stop and tell the user to use `$fix-project-context`.
If the case is about product code, tests, build files, or repo config outside `<active-feature-dir>/**`, stop and tell the user to use the `developer` role.

## Skill-specific scope and classification

Work from the smallest relevant feature analysis/design artifact set under `<active-feature-dir>/**`.
Treat only human-facing feature analysis and design artifacts that should also guide AI agents as in scope.
Classify each candidate by layer (`feature-index` | `feature-log` | `stage-artifact` | `tmp-artifact` | `reference`).
