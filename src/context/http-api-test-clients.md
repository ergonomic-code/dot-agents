---
requires_modules:
  - http-api
applies_when: Работа затрагивает тестовые HTTP-клиенты, их сессии, фабрики или инфраструктуру проверки тел запросов.
routing_order: 105
---

# Контекст тестовых клиентов HTTP API

Прочитай `../conventions/http-api/test-clients.md`.

При проектировании или изменении сессий, их фабрик и доменных классов API прочитай `../patterns/spring/test-client-sessions.md`.

При создании или изменении общей инфраструктуры HTTP-тестов прочитай `../patterns/spring/http-api-test-support.md`.
