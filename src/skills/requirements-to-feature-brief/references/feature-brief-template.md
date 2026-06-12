# Feature Brief Template

Use this template as the default output shape.
Render headings in `artifact_language`.
For this repo with `artifact_language: ru`, use the Russian headings below.

## File Template

This fenced block is the target file content.

~~~md
# <YYMMDD — краткое название - фича-бриф|сабфича-бриф>

## Контекст

<что уже есть, что меняется сейчас, и границы этой итерации>

## Изменения в UI

<что пользователь делает и что видит>

## Изменения в поведении системы

1. <наблюдаемое правило поведения>
2. <ещё правило>

## Бизнес-правила

1. <ограничение, инвариант, порядок, fallback, исключение>

## Термины

- `<термин>` — <точное пользовательское значение>

## Открытые вопросы

1. <что ещё нужно уточнить>

## Приёмочные проверки

1. <Feature>
   1. <проверяемое свойство>
      1. <именованный пример проверки, если нужен>
~~~

## Agent Rules

The rules below guide how to fill the template.
They are not part of the output file.

- Core sections are mandatory: `Контекст`, `Изменения в поведении системы`, `Бизнес-правила`, `Приёмочные проверки`.
- `Изменения в UI`, `Термины`, and `Открытые вопросы` are optional but preferred when they add clarity.
- `Этапы реализации` is optional and should be added only when the user explicitly asked for staged layout or explicitly approved adding stages.
- Write only in end-user domain language.
- Describe only behavior a user can trigger or observe through UI.
- Translate technical source material into user-visible effects.
- Do not add endpoint lists, API contracts, persistence details, or implementation design outside `Этапы реализации`.
- Keep the feature flat by default and omit `Этапы реализации`.
- Include `Этапы реализации` only when one feature needs several implementation slices and staged layout is explicit or approved.
- If several implementation slices are implied but staged layout is not yet explicit or approved, propose it and wait.
- In `Этапы реализации`, identify each stage as `<feature-code>/<stage-code>`, for example `014/01`.
- Use exactly two digits for `<stage-code>`.
- Each behavior stage covers at most one endpoint/API surface; large preparatory refactoring gets its own stage.
- In `Этапы реализации`, exact endpoint/API names are allowed only as stage boundaries.
- Keep scope boundaries explicit.
- Put unresolved but non-blocking gaps into `Открытые вопросы`.
- `Приёмочные проверки` use only short checks: `Feature`, then rules, then optional named examples.
- Do not put `Given` / `When` / `Then` in the feature brief.
