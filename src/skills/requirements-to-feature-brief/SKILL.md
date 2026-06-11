---
name: requirements-to-feature-brief
description: Write or update a formal `010-feature-brief.md` from raw requirements. Use when the user provides a one-liner, notes, chat dump, issue text, interview answers, or an incomplete feature brief and wants a repo-style brief ready for code analysis in the feature workdir.
---

# Write Feature Brief From Requirements

Use configured `artifact_language` for the brief artifact.
Read `framework_checkout_root/src/conventions/lightwight-markup-authoring.md` before writing.
Use it only for documentation formatting.
If it conflicts with this skill or the feature-brief structure, keep this skill.
Read `framework_checkout_root/src/conventions/feature-workdir.md`.
Read `framework_checkout_root/src/conventions/feature-stage-skill.md`.
Read `framework_checkout_root/src/conventions/feature-artifact-phases.md`.
Read `./references/feature-brief-template.md`.
Read `./references/feature-dir-progress-template.md`.

## Feature artifact bindings

- artifact phase code: `010`
- default feature-dir output path: `<feature-dir>/010-feature-brief.md`
- progress.md checklist item: `Фича-бриф`
- artifact phase `010` bootstrap: this skill may create the feature directory when unresolved

## Workflow

- Treat an explicit feature directory or brief path as the target.
- Otherwise use the shared lifecycle from `feature-stage-skill.md` for the default artifact-phase `010` brief.
- When this run creates a new feature directory, also create `<feature-dir>/progress.md` from the local template.
- Create a flat feature directory by default.
- If the user explicitly requests staged layout or explicitly approves adding stages, adapt the root brief and `progress.md` to staged layout per `feature-workdir.md`, using stage directories `stage-<stage-code>` and feature-stage identifiers `<feature-code>/<stage-code>`.
- Create or update the resolved brief path.
- Build context only from the user request, explicitly referenced files, files already inside the target feature directory when it exists, and interview answers.
- Do not read code, OpenAPI, tests, or contracts to fill missing requirements.
- Interview first when scope, user-visible behavior, split boundaries, or acceptance expectations are still behavior-changingly ambiguous.
- Ask only the smallest set of high-value questions.
- If the feature changes UI and the user did not provide screenshots of the changed screens or states, ask for them.
- Do not convert silence into approval.
- If one product change needs several implementation slices and staged layout is already explicit or approved, add `Этапы реализации` using feature-stage identifiers `<feature-code>/<stage-code>` instead of splitting the feature.
- If one product change needs several implementation slices and staged layout is not yet explicit or approved, propose adding stages and wait for approval.
- Propose subfeatures only for independent product changes.
- Rewrite technical source statements into the end-user domain language.
- Write only what changes in this feature.
- Do not restate current behavior, static context, or unchanged flows unless they are needed to explain the change boundary.
- Describe only behavior that the user can trigger or observe through UI.
- Do not describe endpoints, methods, request parameters, tables, migrations, classes, packages, or storage strategy, except exact endpoint/API names in `Этапы реализации` when they define stage boundaries.
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
- Keep implementation design out of the brief unless it is an explicit or approved stage boundary or a user-visible requirement.
- Acceptance checks must describe observable behavior in domain language.
- Cover the main flow, invariants, fallbacks, and important edge cases.
