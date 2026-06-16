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
- Deduplicate semantically across `Целевые изменения`, `Бизнес-правила`, and `Критерии приёмки`.
- If two bullets would be true or false together, keep one bullet and fold in only the unique detail.
- Do not split one scenario into separate bullets for the action, successful outcome, and missing error.
- Use `Точки наблюдения` only for UI screens, UI fragments, user actions, or external systems that interact with the target system.
- For technical or internal engineering work accepted by a technical lead, `Точки наблюдения` may instead use architectural observation anchors.
- Allowed architectural observation anchors are stable refactor-resistant anchors, current target code anchors that already exist in the current codebase, or high-level human-readable anchors on operations, resources, or target modules.
- Do not use future, planned, target-only, renamed, or nonexistent code symbols as observation points, even if they are named in requirement notes, target-design files, or similar source material.
- In `Интеграции`, list only external systems named in project context or by the user.
- Do not list backend, frontend, system layers, internal operations, endpoints, methods, update actions, results, classes, or code contracts as observation points outside that technical-task exception.
- Do not invent observation points.
- Do not add implementation-stage breakdown to the feature brief.
- Keep scope boundaries explicit.
- Confirm assumptions in chat before writing them as facts or requirements.
- Keep business rules distinct.
- Keep `Бизнес-правила` for stable rules, invariants, conditions, and exclusions that are not already clear from target changes.
- `Критерии приёмки` describe customer-acceptable outcomes.
- Keep `Критерии приёмки` to the smallest set of independently checkable outcomes, preferably one end-to-end criterion per scenario.
- Put absence of an error inside the same acceptance criterion as the successful scenario unless that absence is the only accepted outcome.
- Do not put `Given` / `When` / `Then` in the feature brief.
