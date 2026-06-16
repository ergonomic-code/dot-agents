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
Read `framework_checkout_root/src/references/feature-brief-template.md`.
Read `framework_checkout_root/src/references/progress-template.md`.
Treat `framework_checkout_root/src/references/feature-brief-template.md` as the source of truth for brief-content rules, including `Точки наблюдения`, customer wording, deduplication, and acceptance-criteria shape.
If the request or referenced material mentions Ergonomic Architecture, `EA`, `EP`, aggregates, operations, resources, DOPs, target architecture, architecture refactoring, or acceptance by tech lead through code shape, also read `framework_checkout_root/src/conventions/ergonomic-architecture.md` before writing.

## Feature artifact bindings

- artifact phase code: `010`
- default feature-dir output path: `<feature-dir>/010-feature-brief.md`
- progress.md checklist item: `Фича-бриф`
- artifact phase `010` bootstrap: this skill may create the feature directory when unresolved

## Workflow

- Treat an explicit feature directory or brief path as the target.
- When this run creates a new feature directory, also create `<feature-dir>/progress.md` from the loaded progress template.
- Create a flat feature directory by default.
- If the user explicitly requests or approves implementation stages, adapt root `progress.md` with stage headings per `feature-workdir.md`.
- Keep implementation-stage breakdown out of the feature brief.
- Create or update the resolved brief path.
- Build context only from the user request, explicitly referenced files, files already inside the target feature directory when it exists, and interview answers.
- Use loaded project context only to identify named external systems for integration observation points.
- Do not read code, OpenAPI, tests, or contracts to discover missing requirements.
- If a technical task needs code anchors outside `Точки наблюдения`, use only current classes, contracts, or files named by the source material or ask for them.
- If a technical task is constrained by a named architecture source, derive the brief's architecture constraints and technical acceptance criteria from the applicable rules in that source instead of inventing local shape checks.
- Work in interview mode before writing or updating the brief.
- If customer, scope, target changes, observation points, assumptions, or acceptance criteria are unclear, ask the first blocking question and stop.
- Ask exactly one question per turn.
- If the feature changes UI and the changed screens or states are unclear, ask for the first needed screenshot or UI detail and stop.
- Confirm each assumption in chat before relying on it.
- After the user confirms an assumption, write it as context, a requirement, a business rule, a term, or an acceptance criterion.
- Do not write unconfirmed assumptions into the brief.
- Do not convert silence into approval.
- Propose subfeatures only for independent product changes.
- Write only the target changes in this feature.
- Do not restate current behavior, static context, or unchanged flows unless they are needed to explain the change boundary.
- Treat integrations only as external systems named in project context or by the user.
- Do not label an internal operation, endpoint, method, or update action as an integration.
- Do not describe implementation strategy, task sequence, storage strategy, or migrations unless the customer explicitly requires them as acceptance scope.
- Preserve correct parts of an existing brief.
- Rewrite only vague, conflicting, duplicated, overly technical, or scope-breaking parts.
- Before writing a technical brief for tech-lead acceptance, check three things explicitly:
- `Точки наблюдения` are deduplicated roots, not repeated-labeled per-method bullets.
- Each such root stands for the reachable current call tree from that root, not only the named method.
- `Бизнес-правила` are omitted unless the task has separate stable business or domain rules beyond scope and architecture constraints.
- Always produce a complete formal brief with the core sections from the template.
- Add optional sections only when they add signal.
- Do not leave placeholders in a generated or updated brief.
- If a non-critical gap remains, ask whether to keep it open or resolve it now.
- Add `Открытые вопросы` only when the user explicitly says to leave a question open.
- If a critical gap blocks a correct behavior description, stop and ask.

## Output Rules

- Write the brief in `artifact_language`.
- Describe the delta from the current product, integration, or code state, not the whole feature area.
- Keep the brief at target-change and acceptance level.
- Keep implementation planning and stage breakdown out of the brief.
- Do not include unresolved assumptions.
- Do not include open questions unless explicitly requested by the user.
- Cover the main flow, invariants, fallbacks, and important edge cases.
