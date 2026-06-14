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
- When this run creates a new feature directory, also create `<feature-dir>/progress.md` from the local template.
- Create a flat feature directory by default.
- If the user explicitly requests staged layout or explicitly approves adding stages, adapt `progress.md` and stage directories per `feature-workdir.md`.
- Keep implementation-stage breakdown out of the feature brief.
- Create or update the resolved brief path.
- Build context only from the user request, explicitly referenced files, files already inside the target feature directory when it exists, and interview answers.
- Use loaded project context only to identify named external systems for integration observation points.
- Do not read code, OpenAPI, tests, or contracts to discover missing requirements.
- If a technical task needs code anchors, use only classes, contracts, or files named by the source material or ask for them, but do not put them into `Точки наблюдения`.
- Work in interview mode before writing or updating the brief.
- If customer, scope, target changes, observation points, assumptions, or acceptance criteria are unclear, ask the first blocking question and stop.
- Ask exactly one question per turn.
- If the feature changes UI and the changed screens or states are unclear, ask for the first needed screenshot or UI detail and stop.
- Confirm each assumption in chat before relying on it.
- After the user confirms an assumption, write it as context, a requirement, a business rule, a term, or an acceptance criterion.
- Do not write unconfirmed assumptions into the brief.
- Do not convert silence into approval.
- Propose subfeatures only for independent product changes.
- Write the brief in the feature customer's language.
- Use end-user domain language for user-facing product changes.
- Preserve technical terms, classes, contracts, and integration names when the customer is technical or when they are part of the requested change.
- Write only the target changes in this feature.
- Keep the brief short.
- Before writing, deduplicate semantically across `Целевые изменения`, `Бизнес-правила`, and `Критерии приёмки`.
- If two bullets would be true or false together, keep one bullet and fold in only the unique detail.
- Do not split one scenario into separate bullets for the action, successful outcome, and missing error.
- Do not restate current behavior, static context, or unchanged flows unless they are needed to explain the change boundary.
- Use `Точки наблюдения` only for places outside the implementation where the target change can be observed or agreed: UI screens, UI fragments, user actions, or external systems that interact with the target system.
- Do not use backend, frontend, a system layer, internal operation, endpoint, method, update action, result, class, or code contract as an observation point.
- If no UI or external-system observation point is known, ask instead of inventing one.
- Treat integrations only as external systems named in project context or by the user.
- Do not label an internal operation, endpoint, method, or update action as an integration.
- Do not describe implementation strategy, task sequence, storage strategy, or migrations unless the customer explicitly requires them as acceptance scope.
- Keep one consistent domain term per entity.
- Identify and record the feature customer as the accepting role: product-side customer for an end-user or stakeholder role, or technical lead for technical/internal engineering work.
- Do not use an issue reporter, assignee, author, or commenter as the customer unless the source explicitly names them as that accepting role.
- Make acceptance criteria explicit.
- Keep business rules distinct.
- Keep `Бизнес-правила` for stable rules, invariants, conditions, and exclusions that are not already clear from target changes.
- Keep `Критерии приёмки` to the smallest set of independently checkable outcomes, preferably one end-to-end criterion per scenario.
- Put absence of an error inside the same acceptance criterion as the successful scenario unless that absence is the only accepted outcome.
- Preserve correct parts of an existing brief.
- Rewrite only vague, conflicting, duplicated, overly technical, or scope-breaking parts.
- Always produce a complete formal brief with the core sections from the template.
- Add optional sections only when they add signal.
- Do not leave placeholders in a generated or updated brief.
- If a non-critical gap remains, ask whether to keep it open or resolve it now.
- Add `Открытые вопросы` only when the user explicitly says to leave a question open.
- If a critical gap blocks a correct behavior description, stop and ask.

## Output Rules

- Write the brief in `artifact_language`.
- Write the brief in the language of the feature customer.
- Describe the delta from the current product, integration, or code state, not the whole feature area.
- Keep the brief at target-change and acceptance level.
- Keep implementation planning and stage breakdown out of the brief.
- Acceptance criteria must describe customer-acceptable outcomes.
- Do not include unresolved assumptions.
- Do not include open questions unless explicitly requested by the user.
- Cover the main flow, invariants, fallbacks, and important edge cases.
