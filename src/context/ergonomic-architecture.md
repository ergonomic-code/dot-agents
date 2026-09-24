---
requires_modules:
  - ergonomic-architecture
applies_when: Работа касается архитектуры, операций, формы данных или компонентов либо границ абстракций.
routing_order: 60
---

# Архитектурный контекст

Загружай только пункты, соответствующие запрошенной или запланированной работе:

- внесение изменений в операции (потоки работ, operations, workflows), которые читают, вычисляют, записывают или возвращают доменные данные: `../conventions/ergonomic-architecture/operations-design.md`;
- проектирование архитектуры, добавление в систему новых компонентов или Эргономичная архитектура явно упомянута в запросе: `../conventions/ergonomic-architecture/ergonomic-architecture.md`;
- проектриование или внесение изменений в формы доменных данных, сущности, объекты-значения, агрегаты, ссылки между агрегатами или границы агрегатов: `../conventions/ergonomic-architecture/ergonomic-architecture.md` и `../conventions/ergonomic-architecture/ergonomic-data-structure.md`;
- проектирование или внесение изменений в порты (Ports, Controllers, Listeners), операции (Ops), доменные операции (Dops), ресурсы (Repos, Daos, Clients, Queues, Services etc), зависимости или форму графа эффектов: `../conventions/ergonomic-architecture/ergonomic-architecture.md` и `../conventions/ergonomic-architecture/ergonomic-component-structure.md`;
- проектирование или внесение изменений в input, transformation, output, orchestration, структура method или subprogram, декомпозиция поведения или cognitive complexity: `../conventions/ergonomic-architecture/ergonomic-architecture.md` и `../conventions/ergonomic-architecture/ergonomic-behavior-structure.md`;
- ревью, рефакторинг или выделение callable unit либо class: `../conventions/ergonomic-architecture/abstraction-level-boundaries.md`.

После внесения изменений выполни `../conventions/ergonomic-architecture/checklist.md`.
Если найдёшь нарушения - внеси правки для их устранения.
