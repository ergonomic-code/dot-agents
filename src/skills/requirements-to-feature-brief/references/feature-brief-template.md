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

## Приёмочные тесты

```gherkin
Feature: <краткое имя поведения>

  Rule: <ключевое правило>

    Scenario: <наблюдаемый сценарий>
      Given ...
      When ...
      Then ...
```
~~~

## Agent Rules

The rules below guide how to fill the template.
They are not part of the output file.

- Core sections are mandatory: `Контекст`, `Изменения в поведении системы`, `Бизнес-правила`, `Приёмочные тесты`.
- `Изменения в UI`, `Термины`, and `Открытые вопросы` are optional but preferred when they add clarity.
- Write only in end-user domain language.
- Describe only behavior a user can trigger or observe through UI.
- Translate technical source material into user-visible effects.
- Do not add endpoint lists, API contracts, persistence details, or implementation design.
- Keep scope boundaries explicit.
- Put unresolved but non-blocking gaps into `Открытые вопросы`.
- Gherkin must stay observable and non-technical.
