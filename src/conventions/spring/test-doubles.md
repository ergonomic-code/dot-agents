---
keywords:
  - spring
  - tests
---

# Spring test doubles

- Do not use Spring bean override mechanisms such as `@MockBean`, `@SpyBean`, `@MockitoBean`, or `@MockitoSpyBean`.
- When a class-level double is required, construct the target dependency graph explicitly from real dependencies in the existing application context and substitute only the simulated dependency.
- Resolve real collaborators, нужные только этому graph, локально через inherited helper доступа к application context языка теста; не inject их или application context в constructors либо fields test class.
- Если у shared test superclass нет этого helper, добавь protected helper, делегирующий existing application context.
- If framework proxies are required, register the explicit graph through existing test infrastructure in the same application context without overriding beans.
