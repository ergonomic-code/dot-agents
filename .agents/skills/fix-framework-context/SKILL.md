---
name: fix-framework-context
description: Analyze a framework-context problem from `problem`, `target behavior`, and optional `codex session id`; load `framework-context-engineer`; propose `minimal`, `systemic`, and `optimal` fixes; wait for explicit choice; then implement it in this repository.
---

# Fix framework context

Read `../../../src/skills/fix-framework-context/SKILL.md` first.
Use its workflow for required input, evidence, option design, long-file handling, implementation, and output.
In this wrapper, do not apply the runtime redirect from current-repo `AGENTS.md`, `.agents/**`, or `.codex/**` to `$fix-project-context`.

This wrapper always resolves the role to `framework-context-engineer`.
Before task triage, load `./.agents/roles/framework-context-engineer.md`.

In this repository, classify `framework surface` before options:
- `authoring-context`
- `runtime-context`

Report `Framework surface` before `Editable roots`.

If `framework surface` is `authoring-context`, treat editable roots as:
- `./.agents/**`
- `./.codex/**`
- `./AGENTS.md`
- `./README.md`

If `framework surface` is `runtime-context`, treat editable roots as:
- `./src/**`

For `authoring-context`, use layers (`agents-root` | `agents-dir` | `codex-dir` | `readme` | `reference`).
For `runtime-context`, reuse the runtime skill classification.
