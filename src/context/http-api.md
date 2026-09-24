---
requires_modules:
  - http-api
applies_when: Работа затрагивает HTTP-операцию, HTTP-контракт, boundary-тест или типизированный HTTP test helper.
routing_order: 50
---

# Контекст HTTP API

Загружай только пункты, соответствующие запрошенной или запланированной HTTP-работе:

- добавление или изменение граничных тестов на HTTP эндпониты: `../conventions/http-api/http-api-test-design.md` и `../conventions/http-api/http-api-test-rules.md`;
- добавление или изменение тестовых HttpApi: `../conventions/http-api/http-api-test-rules.md`
- проектирование или интерпретация ошибочных ответов: `../patterns/http-json-api/error-response-body-format.md`.

После внесения изменений в тесты или HttpApi выполни `../conventions/http-api/http-api-test-checklist.md`.
Если найдёшь нарушения - внеси правки для их устранения.