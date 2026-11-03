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
- Если работа предполагает добавление или изменение имён тестовых групп или кейсов (в том числе при рефакторинге), прочитай `../conventions/core/test-naming.md` и `../artifacts/test-case-specification-format/references/feature-naming.md`;
- Если работа предполагает добавление или изменение тел тест-кейсов, источников параметров, фикстур, тестовых помощников или адаптеров, прочитай `../conventions/core/test-implementation.md`.

- Если работа затрагивает запуск, сброс или освобождение тестовой инфраструктуры и общей фикстуры, прочитай `../conventions/core/test-fixture-lifecycle.md`;
- Если работа затрагивает `*TestApi`, подготовку или наблюдение состояния ресурсов, прочитай `../conventions/core/test-api.md`;
- Если работа затрагивает фрагменты фикстур, их фабрики или установщики, прочитай `../conventions/core/test-fixture-fragments.md`.

- Для обзора приёмов реализации подготовки фикстур прочитай `../conventions/core/test-patterns.md`.
- Если работа затрагивает генерацию тестовых данных, используй соответствующие описания:
  - `../conventions/core/fixture-setup-patterns/01-overridable-defaults.md`;
  - `../conventions/core/fixture-setup-patterns/02-domain-generators.md`;
  - `../conventions/core/fixture-setup-patterns/03-minimal-and-full.md`;
  - `../conventions/core/fixture-setup-patterns/04-collections.md`;
  - `../conventions/core/fixture-setup-patterns/05-repeatable-generation.md`;
- Если работа затрагивает построение и установку фрагментов фикстур, используй соответствующие описания:
  - `../conventions/core/fixture-setup-patterns/06-in-memory-graph.md`;
  - `../conventions/core/fixture-setup-patterns/07-named-fragments.md`;
  - `../conventions/core/fixture-setup-patterns/08-inputs-and-expectations.md`;
  - `../conventions/core/fixture-setup-patterns/09-fixture-and-installer.md`;
  - `../conventions/core/fixture-setup-patterns/10-installed-values.md`;
  - `../conventions/core/fixture-setup-patterns/11-named-setup.md`;
- Если работа затрагивает подготовку состояния ресурсов через TestApi, используй соответствующие описания:
  - `../conventions/core/fixture-setup-patterns/12-resource-test-api.md`;
  - `../conventions/core/fixture-setup-patterns/13-targeted-sql.md`;
- Если работа затрагивает настройку внешних зависимостей, используй соответствующие описания:
  - `../conventions/core/fixture-setup-patterns/15-http-double.md`;
  - `../conventions/core/fixture-setup-patterns/16-local-and-external-state.md`;
- Если работа затрагивает жизненный цикл тестового окружения, используй соответствующие описания:
  - `../conventions/core/fixture-setup-patterns/17-restore-background.md`;
  - `../conventions/core/fixture-setup-patterns/18-separate-lifetimes.md`;
  - `../conventions/core/fixture-setup-patterns/19-composable-base.md`;
  - `../conventions/core/fixture-setup-patterns/20-database-baseline.md`;
  - `../conventions/core/fixture-setup-patterns/21-provided-dependency.md`;
  - `../conventions/core/fixture-setup-patterns/22-spring-managed-sut.md`;
- Если работа затрагивает композицию подготовки в кейсе, прочитай `../conventions/core/test-case-patterns/14-direct-composition.md`.

После внесения изменений в код тестов выполни `../conventions/core/ergonomic-approach-checklist.md` и `../conventions/core/test-implementation-checklist.md`.
Если подключён модуль `ergonomic-testing`, также выполни `../conventions/ergonomic-testing/checklist.md`.
Если найдёшь нарушения — исправь их.
