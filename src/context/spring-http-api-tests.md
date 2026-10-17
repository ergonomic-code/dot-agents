---
requires_modules:
  - spring
  - http-api
applies_when: Работа затрагивает тестовые HTTP-клиенты на Spring, их сессии, фабрики или инфраструктуру проверки тел запросов.
routing_order: 105
---

# Контекст тестовых клиентов Spring HTTP API

Прочитай `../conventions/spring/http-api-tests.md`.

При проектировании или изменении сессий, их фабрик и доменных классов API на Kotlin прочитай `../patterns/spring/test-client-sessions.md`.

При создании или изменении общей инфраструктуры HTTP-тестов на Kotlin прочитай `../patterns/spring/http-api-test-support.md`.
