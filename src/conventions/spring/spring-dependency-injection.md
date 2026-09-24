---
keywords:
  - spring
  - dependency-injection
---

# Внедрение зависимостей Spring

- Используй constructor injection для управляемых Spring зависимостей.
- Используй field injection только когда constructor injection недоступен или несовместим с lifecycle фреймворка либо теста.
- Не вводи managed bean, если компоненту не нужны другие managed beans как зависимости; используй обычный `object` в Kotlin или класс со static-методами в Java.
