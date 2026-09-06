---
keywords:
  - spring
  - beans
---

# Spring beans

- Do not introduce managed beans if the component does not need other managed beans as dependencies.
- Use plain Kotlin singleton objects in this case.
- In Kotlin Spring code, use Spring Kotlin extensions such as `getBean<T>("name")` over equivalent Java `Class<T>` overloads, importing the extension when needed.
