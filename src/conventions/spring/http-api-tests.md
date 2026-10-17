---
keywords:
  - spring
  - http-api
---

# Тестовые клиенты Spring HTTP API

Для граничных HTTP тестов Spring-приложения нужна обвязка, которая вызывает приложение через HTTP, а кейсам предоставляет доменные операции и типизированные результаты.
Общий паттерн ниже объясняет разделение ответственности; примеры на Kotlin и Spring показывают его реализацию через `RestTestClient` и проверку сериализованных тел запросов.

- В Spring-клиентах `*HttpApi` предпочитай простые URI-шаблоны вместо `uri { uriBuilder -> ... }` для статических путей.
- Для декодирования параметризованных типов используй `ParameterizedTypeReference<T>` или проектный хелпер на его основе.

Паттерны:
- [Сессии тестовых HTTP-клиентов](../../patterns/http-json-api/test-client-sessions.md).
- [Общая инфраструктура тестов HTTP API](../../patterns/spring/http-api-test-support.md).
- [Пример сессий и доменного API на Kotlin и Spring](../../patterns/spring/test-client-sessions.md).
