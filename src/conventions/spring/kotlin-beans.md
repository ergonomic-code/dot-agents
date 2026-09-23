---
keywords:
  - spring
  - kotlin
---

# Spring Kotlin beans

- In Kotlin Spring code, use Spring Kotlin extensions such as `getBean<T>("name")` over equivalent Java `Class<T>` overloads, importing the extension when needed.
- Не вводи managed bean, если component не нуждается в других managed beans как dependencies; в таком случае используй plain Kotlin singleton object.
