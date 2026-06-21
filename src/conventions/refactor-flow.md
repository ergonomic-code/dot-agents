# Refactor flow

Use this rule for standalone refactor-only tasks.
Use `task-boundaries.md` for coding-slice boundaries while applying this flow.

## Purpose

- Refactor flow changes code structure without changing externally observable behavior.
- It is a standalone workflow for structural work that is not merely a post-green-case cleanup.
- Use it when the user asks for refactoring as the work itself, or when a large preparatory refactoring must be done before dependent behavior work.

## Boundaries

- Preserve externally observable behavior inside and outside the selected refactor boundary.
- Do not add new behavior requirements, endpoint contracts, config, retries, defaults, or compatibility branches.
- Before changing production code, you may add or strengthen checks that capture current factual behavior without changing it.
- In one refactor slice, refactor either production code or test code, not both.
- Do not broaden the target beyond the selected refactor boundary except for compile-required call-site propagation.
- Stop if the desired cleanup requires behavior clarification, new product decisions, or wider redesign.

## Progress model

- Keep `progress.md` flat.
- Use level-2 headings for workflow phases.
- Use level-3 headings only for phase-local subdivisions when they materially improve navigation.
- Track each structural increment as one flat checklist item named `Рефакторинг: <краткий инкремент>`.
- Keep todo lists short.

Use these phases for a standalone refactor task:

~~~md
# Прогресс рефакторинга

## Цель рефакторинга

- [ ] Определить границу и ожидаемое структурное улучшение

## Понимание текущего устройства

- [ ] Найти целевые компоненты
- [ ] Найти проверку сохранения поведения

## Выбор направления рефакторинга

- [ ] Зафиксировать принципиальный structural-change подход

## Выполнение

- [ ] Рефакторинг: <краткий инкремент>

## Проверка поведения

- [ ] Запустить минимальную проверку сохранения поведения
~~~

## Execution

- Before editing, state the target boundary, whether the slice targets production code or test code, structural problem, planned increments, and validation command.
- Change structure only.
- Prefer moving, extracting, renaming, or introducing a narrow helper over broad shared abstractions.
- Keep public signatures stable unless the refactor boundary explicitly includes internal call-site propagation.
- After each increment, run the smallest relevant behavior-preservation check.
- If shared APIs or broad call sites changed, also run the smallest relevant compile or module test.
