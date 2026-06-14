# Feature Brief Template

Use this template for `010-feature-brief.md`.
Render headings in configured `artifact_language`.
For `ru`, use the Russian text below.

## File Template

~~~md
# <YYMMDD - краткое название>

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

- Keep the default template flat.
- Do not add implementation-stage breakdown to the feature brief.
- Use staged `progress.md` and `stage-<stage-code>/` directories for implementation-stage breakdown.
- Do not use `Открытые вопросы` unless the user explicitly asked to leave a question open.
- Use `Заказчик` for the accepting role: product-side customer for an end-user or stakeholder role, or technical lead for technical/internal engineering work.
- Do not use an issue reporter, assignee, author, or commenter as the customer unless the source explicitly names them as that accepting role.
- In `Точки наблюдения`, use only UI screens, UI fragments, user actions, or external systems that interact with the target system.
- Do not list backend, frontend, system layers, internal operations, endpoints, methods, update actions, results, classes, or code contracts as observation points.
- Confirm assumptions before writing them as facts or requirements.
- Keep the brief short.
- Deduplicate semantically across `Целевые изменения`, `Бизнес-правила`, and `Критерии приёмки`.
- Prefer one end-to-end acceptance criterion per scenario.
