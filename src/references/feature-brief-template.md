# Feature Brief Template

Use this template as the default output shape.
Render headings in `artifact_language`.
For this repo with `artifact_language: ru`, use the Russian headings below.

## File Template

This fenced block is the target file content.

~~~md
# <YYMMDD — краткое название - фича-бриф|сабфича-бриф>

## Заказчик

<заказчик: продакт для роли конечного пользователя или стейкхолдера, либо техлид>

## Контекст

<что уже есть, что меняется сейчас, и границы этой итерации>

## Целевые изменения

1. <изменение в терминах заказчика>
2. <ещё изменение>

## Точки наблюдения

- UI: <экран, фрагмент UI, состояние или действие пользователя, если меняется пользовательская фича>
- Интеграции: <внешняя система, с которой взаимодействует целевая система, если меняется интеграция>

## Бизнес-правила

1. <ограничение, инвариант, порядок, fallback, исключение>

## Термины

- `<термин>` — <точное значение в языке заказчика>

## Критерии приёмки

1. <критерий, по которому заказчик сможет принять изменение>
2. <ещё критерий>
~~~

## Agent Rules

The rules below guide how to fill the template.
They are not part of the output file.

- Core sections are mandatory: `Заказчик`, `Контекст`, `Целевые изменения`, `Точки наблюдения`, `Критерии приёмки`.
- `Бизнес-правила` and `Термины` are optional but preferred when they add clarity.
- `Открытые вопросы` is optional and allowed only when the user explicitly asked to leave a question open.
- Use `Заказчик` for the accepting role: product-side customer for an end-user or stakeholder role, or technical lead for technical/internal engineering work.
- Do not use an issue reporter, assignee, author, or commenter as the customer unless the source explicitly names them as that accepting role.
- Write in the feature customer's language.
- Use end-user domain language for user-facing product changes.
- Keep technical terms, classes, contracts, and integration names when they are part of the customer's requested change.
- Keep the brief short.
- Deduplicate semantically across `Целевые изменения`, `Бизнес-правила`, and `Критерии приёмки` by assigning each fact to one canonical section.
- Use `Целевые изменения` only for customer-visible target results and scope changes.
- Use `Бизнес-правила` as the canonical place for stable details, constraints, formats, mappings, limits, fallbacks, and exclusions.
- Use `Критерии приёмки` for independently checkable scenarios or outcomes, not as a copy of the detailed specification.
- When an acceptance criterion needs detailed rules already stated in `Бизнес-правила`, reference the rule group briefly instead of repeating every detail.
- If two bullets would be true or false together, keep one bullet and fold in only the unique detail.
- Do not split one scenario into separate bullets for the action, successful outcome, and missing error.
- Use `Точки наблюдения` only for UI screens, UI fragments, user actions, or external systems that interact with the target system.
- For technical or internal engineering work accepted by a technical lead, `Точки наблюдения` may instead use architectural observation anchors.
- For such technical work, render `Точки наблюдения` as a compact deduplicated list under one shared section label, not as repeated per-line prefixes like `Архитектурные якоря:`.
- Allowed architectural observation anchors are stable refactor-resistant anchors, current target code anchors that already exist in the current codebase, or high-level human-readable anchors on operations, resources, or target modules.
- Treat each architectural observation anchor as an observation root covering the reachable current call tree from that root, not only the single named port method itself.
- Do not use future, planned, target-only, renamed, or nonexistent code symbols as observation points, even if they are named in requirement notes, target-design files, or similar source material.
- In `Интеграции`, list only external systems named in project context or by the user.
- Do not list backend, frontend, system layers, internal operations, endpoints, methods, update actions, results, classes, or code contracts as observation points outside that technical-task exception.
- Do not invent observation points.
- Do not add implementation-stage breakdown to the feature brief.
- Keep scope boundaries explicit.
- Confirm assumptions in chat before writing them as facts or requirements.
- Keep business rules distinct.
- Keep `Бизнес-правила` for stable rules, invariants, conditions, and exclusions that are not already clear from target changes.
- For technical or internal engineering work, omit `Бизнес-правила` when the task has no separate stable business or domain rules beyond scope limits and architecture or implementation constraints already covered elsewhere in the brief.
- `Критерии приёмки` describe customer-acceptable outcomes.
- Keep `Критерии приёмки` to the smallest set of independently checkable outcomes, preferably one end-to-end criterion per scenario.
- For technical or internal engineering work accepted by a technical lead, derive acceptance criteria from the applicable architecture or design constraints named by the source material when such a source is provided.
- When `framework_checkout_root/src/conventions/ergonomic-architecture.md` and projection-specific EA conventions were loaded for the task, use their relevant constraints to ground technical acceptance criteria instead of writing only ad hoc code-shape checks.
- Put absence of an error inside the same acceptance criterion as the successful scenario unless that absence is the only accepted outcome.
- Do not put `Given` / `When` / `Then` in the feature brief.
