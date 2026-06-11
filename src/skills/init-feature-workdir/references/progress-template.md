# Progress Template

Use this template for `progress.md`.
Render all human-readable text in configured `artifact_language`.
For `ru`, use the Russian text below.

## File Template

~~~md
# Прогресс реализации

- [ ] Проработка требований
  - [ ] [Фича-бриф](./010-feature-brief.md)
  - [ ] Дополнительные требования
- [ ] Анализ текущего кода
  - [ ] Текущее API
  - [ ] Текущие тест-кейсы
  - [ ] Текущая доменная модель
  - [ ] Текущая модель персистентности
  - [ ] Текущая схема БД
- [ ] Проект реализации
  - [ ] Изменения API
  - [ ] Изменения тест-кейсов
  - [ ] Целевая доменная модель
  - [ ] Целевая модель персистентности
  - [ ] Целевая схема БД
- [ ] Реализация
  - [ ] SUT: <название>
    - [ ] Кейс №X
      - [ ] Красный тест
      - [ ] Зелёный тест
- [ ] Финализация
  - [ ] Залить/актуализировать артефакты
~~~

## Agent Rules

- Keep the default template flat.
- For staged layout, group implementation cases under `Реализация` by `Этап <feature-code>/<stage-code>: <название>`.
- Use exactly two digits for `<stage-code>`.
