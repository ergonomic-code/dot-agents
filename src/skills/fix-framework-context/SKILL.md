---
name: fix-framework-context
description: Analyze a framework-context fix or feature request from `problem`, `target behavior`, and optional `codex session id` in the caller-selected `framework-context-engineer` role; propose `minimal`, `systemic`, and `optimal` changes; wait for explicit choice; then implement it.
---

# Fix or extend framework context

Read `framework_checkout_root/src/references/context-fix-minimality.md`.
Read `framework_checkout_root/src/references/context-fix-workflow.md`.
Read `framework_checkout_root/src/references/context-layering.md`.

Require the caller to invoke this skill from the `framework-context-engineer` role.

Treat editable roots as:
- `framework_checkout_root/src/**`

Treat framework-context fixes and new framework-context capabilities under `framework_checkout_root/src/**` as in scope.
For new capability work without a defect, treat the missing capability or limitation as the `problem`.

If the case is about current-repo `AGENTS.md`, or project-local `.agents/**` or `.codex/**` outside `framework_checkout_root/**`, stop and tell the user to use `$fix-project-context`.

## Skill-specific scope and classification

Work from the smallest relevant framework file set under `framework_checkout_root/src/**`.
Classify each candidate by layer (`project-baseline` | `roles-index` | `role` | `context-index` | `convention` | `skill` | `artifact` | `reference` | `task-workdir`).

## Architecture boundary

- Use the dependency invariant in `context-layering.md` when analyzing options and implementing the selected change.
- Put applicability based on what requested or planned work touches in context indexes.
- Keep topical routing out of roles, generic skills, conventions, and baseline orchestration.
- Keep one to three YAML front-matter keywords on every convention file, require every rule in the file to concern every keyword, and split and independently route rules with a different keyword intersection.
- Keep intrinsic skill dependencies in the skill.
- Treat skills under `framework_checkout_root/src/skills/**` as generic and independent of task-workdir storage.
- Allow task layout, filenames, artifact codes, and progress rules under `framework_checkout_root/src/task-workdir/**`.
- Keep implicit task resolution in the baseline and concrete task bindings in task-workdir context.
- Require roles to receive those bindings and pass explicit semantic inputs and output destinations to generic skills.
- Do not make any skill select or load a role.
- Do not report task-workdir skills as generic-skill violations.
