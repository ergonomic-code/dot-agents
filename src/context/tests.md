---
requires_modules:
  - core
applies_when: Планирование, добавление, изменение, рефакторинг, выравнивание или ревью тестов, тестовых помощников либо тестовых адаптеров.
routing_order: 30
---

# Контекст тестов

Всегда читай:

- `../conventions/core/ergonomic-approach-rules.md`;
- `../conventions/core/test-design.md`;
- `../conventions/core/test-fixture-architecture.md`;

Если подключён модуль `ergonomic-testing`, прочитай `../conventions/ergonomic-testing/ergonomic-testing.md`.

- Если работа предполагает внесение изменений в код прочитай `../conventions/core/process/dev-task-boundaries.md`;
- Если работа предполагает добавление новых тестов или изменение существующих тестов для отражения изменений в требованиях прочитай `../conventions/core/process/tests-development.md`;
- Если работа предполагает рефакторинг тестов без изменений в требованиях прочитай `../conventions/core/process/tests-refactoring.md`;
- Если работа предполагает добавление или изменение тестов, которые используют тестовые дубли прочитай `../conventions/core/test-doubles.md`;
- Если работа предполагает проектирование тестов прочитай `../conventions/core/test-case-selection.md`;
- Если работа предполагает добавление или изменение имён тестов прочитай `../conventions/core/test-naming.md` и `../artifacts/test-case-specification-format/references/feature-naming.md`;
- Если работа предполагает добавление или изменение тел тест-кейсов `../conventions/core/test-implementation.md`.

После внесения изменений в код тестов выполни `../conventions/core/ergonomic-approach-checklist.md` и `../conventions/core/test-implementation-checklist.md`.
Если подключён модуль `ergonomic-testing`, также выполни `../conventions/ergonomic-testing/checklist.md`.
Если найдёшь нарушения — исправь их.
