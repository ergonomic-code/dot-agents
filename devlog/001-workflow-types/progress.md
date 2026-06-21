# Прогресс реализации

## Прояснение требований

- [x] [Фича-бриф](010-feature-brief.md)
- [x] Решить заводить ли отдельный поток для багфикса: [решение](decisions/bug-fix-flow-decision.md)
- [x] Решить как оформлять нетиповые задачи вроде нагрузочного тестирования: [решение](decisions/unusual-task-flow-decision.md)

## Понимание текущего устройства реализации

- [x] [Целевые файлы](020-code-anchors.md)

## Выбор принципиального направления решения

- [x] Принципиальное решение: [030-design-blueprint.md](030-design-blueprint.md)

## Реализация

- [ ] Завести самостоятельный refactor-flow без behavior changes
- [ ] Подчистить preliminary refactoring в feature-flow и сослать его на refactor mechanics
- [ ] Ввести базовый `Task flow` без breaking rename существующих paths
- [ ] Привязать feature-flow к `Task flow`
- [ ] Привязать refactor-flow к `Task flow`
- [ ] Переименовать shared `feature-*` framework API в task/workflow-neutral paths
- [ ] Проверить старую feature-as-base terminology и representative runtime skill loading paths
