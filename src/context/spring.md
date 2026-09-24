---
requires_modules:
  - spring
applies_when: Работа затрагивает Spring API или Spring infrastructure.
routing_order: 80
---

# Контекст Spring

Загружай только пункты, соответствующие запрошенной или запланированной Spring-работе:

- при любой работе со Spring-бинами: `../conventions/spring/spring-dependency-injection.md`;
- при создании Spring-бинов с тестовыми дублями в качестве зависимостей: `../conventions/spring/test-doubles.md`.

После внесения изменений тестов выполни `../conventions/spring/checklist.md`.
Если найдёшь нарушения — исправь их.
