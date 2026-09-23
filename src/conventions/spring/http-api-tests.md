---
keywords:
  - spring
  - http-api
---

# Spring HTTP API tests

- Inside Spring `*HttpApi` clients, prefer simple URI templates over `uri { uriBuilder -> ... }` when the path is static.
- Use `ParameterizedTypeReference<T>` or a project helper built on top of it for generic decoding.
- If the project uses a custom `JsonMapper`/`ObjectMapper`, align Spring client codecs with it.
