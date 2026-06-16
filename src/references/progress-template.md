# Progress Template

Use this template for `progress.md`.
Render all human-readable text in configured `artifact_language`.
For `ru`, use the Russian text below.

## File Template

~~~md
# Прогресс реализации

## Прояснение требований

- [ ] Фича-бриф
- [ ] Дополнительные требования

## Понимание текущего устройства реализации

- [ ] Целевые компоненты
- [ ] Тесты целевых компонентов
- [ ] Смежная функциональность

## Выбор принципиального направления решения

- [ ] Принципиальное решение

## Предварительный рефакторинг

- [ ] Определить необходимость предварительного рефакторинга
- [ ] Рефакторинг: <краткий инкремент>

## Реализация

- [ ] <краткое описание тестируемого поведения>
  - [ ] красный кейс
  - [ ] зелёный кейс
~~~

## Agent Rules

- Keep checklist items short.
- Use nested checklist items only for the temporary TDD child items below one tested-behavior parent.
- Use level-2 headings for workflow phases.
- Use level-3 headings for implementation stages or phase-local subdivisions.
- For implementation stages, add `### Этап <feature-code>/<stage-code>: <название>` under `## Реализация`.
- Use exactly two digits for `<stage-code>`.
- Do not create `stage-<stage-code>/` directories.
- For TDD increments, use one parent behavior item with child items `красный кейс` and `зелёный кейс`.
- After the case is green, remove both child items and mark the parent behavior item done.
