---
name: design-solution-blueprint
description: Design and record a feature-wide `030-design-blueprint.md` from a feature brief and code anchors. Use when the user asks to choose a principled implementation direction, solution approach, architecture direction, or "how we implement this" for a feature after requirements and current-code anchors are available.
---

# Design Solution Blueprint

Read `framework_checkout_root/src/conventions/feature-workdir.md`.
Read `framework_checkout_root/src/conventions/feature-stage-skill.md`.
Read `framework_checkout_root/src/conventions/feature-artifact-phases.md`.
Read `framework_checkout_root/src/conventions/lightwight-markup-authoring.md`.
Read `framework_checkout_root/src/conventions/ergonomic-approach.md`.
Read `framework_checkout_root/src/conventions/task-boundaries.md`.

## Feature artifact bindings

- artifact phase code: `030`
- default feature-dir output path: `<feature-dir>/030-design-blueprint.md`
- progress.md checklist item: `Принципиальное решение`
- human-readable artifact title: `Принципиальное решение`

## Inputs

Required:
- feature brief, normally `<feature-dir>/010-feature-brief.md`;
- verified code anchors, normally `<feature-dir>/020-code-anchors.md`.

Optional:
- explicit output path;
- user-provided constraints, preferred direction, or rejected directions.

## Workflow

1. Resolve the active feature directory and output path by the feature artifact lifecycle.
2. Read the feature brief, code anchors, existing blueprint if present, and explicit user constraints.
3. If the brief or anchors are missing, stale, or too vague to design from, stop and ask for the missing artifact or clarification.
4. Derive the core design problem, impacted surfaces, invariants, task boundaries, and implementation risks.
5. Present `2-4` materially different solution approaches in chat.
   Keep each approach high level.
   Include short pros and cons.
   Recommend one approach when the evidence supports it.
6. Stop for user choice or discussion.
   Do not write `030-design-blueprint.md` before the final approach is explicitly chosen.
7. After the user chooses, write or update the blueprint.
8. Sync `progress.md` through the feature artifact lifecycle when possible.

## Approach Rules

- Compare directions, not detailed implementation plans.
- Keep options grounded in the feature brief and verified code anchors.
- If the brief or user constraints cite a named architecture source, preserve that source's component terminology in the blueprint and do not introduce adjacent local synonyms or alternative taxonomy.
- Prefer approaches that preserve task boundaries, one externally visible API surface per behavior slice, ergonomic state/data design, and simple dependency shape.
- Add implementation stages only when the chosen approach needs coarse decomposition.
- Treat stages as large slices: roughly `5+` TDD cycles, one endpoint/API surface, a group of similar endpoints or similar endpoint edits, or a large self-contained refactor.
- Do not turn ordinary red-green-refactor steps, one endpoint fix, or the verification command into stages.
- If progress needs stages, use level-3 `Этап <feature-code>/<stage-code>: <название>` headings in root `progress.md`.
- Keep preliminary refactoring separate from behavior changes.
- State assumptions and open questions instead of hiding them in a chosen design.
- Do not invent requirements, code anchors, APIs, storage, migrations, or tests.

## Output

Write the blueprint in Markdown and in the configured `artifact_language`.
Use compact one-sentence-per-line prose.
Structure dense technical detail with headings, short paragraphs, and lists so the document stays scannable.
Include these sections:
- `# Принципиальное решение`
- `## Контекст`
- `## Выбранный подход`
- `## Открытые вопросы`
- `## Приложение: отброшенные варианты`

Add `## Этапы` before `## Открытые вопросы` only when coarse implementation stages are needed.
In `Контекст`, include the problem, decision drivers, and constraints needed to understand the chosen direction.
In `Выбранный подход`, record the final decision, why it was chosen, and the technical details needed to implement it correctly.
Use paragraphs as the primary structure for `Контекст` and `Выбранный подход`.
Group adjacent sentences into one short paragraph when they explain the same concern, decision driver, boundary, invariant, or risk.
Split `Выбранный подход` into level-3 subsections when it contains several distinct concern groups, phases, boundaries, invariants, or validation criteria.
Use lists only for ordered sequences, comparable alternatives, stages, checklists, or compact enumerations that would be harder to scan as prose.
In `Этапы`, write only a short ordered outline of coarse implementation slices.
In `Открытые вопросы`, write `Нет.` when no material question remains.
In `Приложение: отброшенные варианты`, preserve the rejected chat-presented approaches with their main pros, cons, and rejection reason.
Do not render important technical detail as one long prose block.
Do not render a design section as a flat stream of isolated one-sentence paragraphs.

## Before Finishing

Check that:
- the chat contained `2-4` approaches before the file was written;
- the user explicitly chose the final approach;
- every approach is traceable to the brief and anchors;
- rejected alternatives are preserved only in the appendix;
- dense technical detail is split into meaningful subsections, lists, or short paragraphs;
- `Контекст` and `Выбранный подход` use paragraphs grouped by concern instead of flat sentence streams;
- `Этапы` is present only for coarse decomposition and does not mutate feature layout;
- progress stages use root `progress.md` headings;
- `progress.md` is updated when the lifecycle permits it.
