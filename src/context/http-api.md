---
requires_modules:
  - http-api
applies_when: Работа затрагивает HTTP-операцию, HTTP-контракт, тест HTTP-границы, типизированный HTTP-хелпер либо сессии и фабрики тестовых HTTP-клиентов.
routing_order: 50
---

# Контекст HTTP API

Загружай только пункты, соответствующие запрошенной или запланированной HTTP-работе:

- первоначальная настройка обвязки тестов HTTP-границы в новом проекте: `../references/http-api-test-project-start.md`;
- добавление или изменение граничных тестов HTTP-эндпоинтов: `../conventions/http-api/http-api-test-design.md` и `../conventions/http-api/http-api-test-rules.md`;
- добавление или изменение тестовых `*HttpApi`: `../conventions/http-api/http-api-test-rules.md`;
- проектирование или изменение тестовых HTTP-клиентов, их сессий и фабрик: `../patterns/http-json-api/test-client-sessions.md`;
- проектирование или интерпретация ошибочных ответов: `../patterns/http-json-api/error-response-body-format.md`.

После внесения изменений в тесты, `*HttpApi`, сессии или фабрики тестовых HTTP-клиентов выполни `../conventions/http-api/http-api-test-checklist.md`.
Если найдёшь нарушения, внеси правки для их устранения.
