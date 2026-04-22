---
name: requirements-to-feature-brief
description: Write or update a formal `010-feature-brief.md` from raw requirements. Use when the user provides a one-liner, notes, chat dump, issue text, interview answers, or an incomplete feature brief and wants a repo-style brief ready for code analysis in the feature workdir.
---

# Write Feature Brief From Requirements

Use configured `artifact_language` for the markdown artifact.
Read `framework_checkout_root/src/conventions/markdown.md` before writing.
Use it only for markdown formatting.
If it conflicts with this skill or the feature-brief structure, keep this skill.
Read `framework_checkout_root/src/conventions/feature-workdir.md`.
Read `./references/feature-brief-template.md`.
Read `./references/feature-dir-index-template.md`.
Read `./references/feature-dir-progress-template.md`.

## Workflow

- Determine the target feature directory.
- If the user gave a feature directory or brief path, use it.
- Otherwise, resolve the active feature directory via `framework_checkout_root/src/conventions/feature-workdir.md`.
- If no target feature directory is resolved, create one via `framework_checkout_root/src/conventions/feature-workdir.md` for the default stage `010` brief.
- When creating a new feature directory for the default stage `010` brief, also create `<feature-dir>/index.md` and `<feature-dir>/progress.md` from the local templates.
- Create or update `<feature-dir>/010-feature-brief.md`.
- Build context only from the user request, explicitly referenced files, files already inside the target feature directory, and interview answers.
- Do not read code, OpenAPI, tests, or contracts to fill missing requirements.
- Interview first when scope, user-visible behavior, split boundaries, or acceptance expectations are still behavior-changingly ambiguous.
- Ask only the smallest set of high-value questions.
- If the feature changes UI and the user did not provide screenshots of the changed screens or states, ask for them.
- Do not convert silence into approval.
- If the request clearly contains several independent rollout steps, propose a split into subfeatures and wait for approval.
- Rewrite technical source statements into the end-user domain language.
- Write only what changes in this feature.
- Do not restate current behavior, static context, or unchanged flows unless they are needed to explain the change boundary.
- Describe only behavior that the user can trigger or observe through UI.
- Do not describe endpoints, methods, request parameters, tables, migrations, classes, packages, or storage strategy.
- Keep one consistent domain term per entity.
- Preserve correct parts of an existing brief.
- Rewrite only vague, conflicting, duplicated, overly technical, or scope-breaking parts.
- Always produce a complete formal brief with the core sections from the template.
- Add optional sections only when they add signal.
- Leave explicit placeholders instead of inventing missing UI details.
- When UI screenshots are still missing, keep the unresolved UI parts as placeholders in the brief and list the required screenshots in `Открытые вопросы`.
- If a non-critical gap remains, capture it in `Открытые вопросы`.
- If a critical gap blocks a correct behavior description, stop and ask.

## Output Rules

- Write the brief in `artifact_language`.
- Write the brief in the language of the end user, not in API or implementation language.
- Describe the delta from the current product state, not the whole feature area.
- Keep the brief at UI and observable system behavior level.
- Keep implementation design out of the brief unless the requirement explicitly makes it user-visible.
- Acceptance tests must describe observable behavior in domain language.
- Cover the main flow, invariants, fallbacks, and important edge cases.
