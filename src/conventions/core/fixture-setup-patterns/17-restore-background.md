---
keywords:
  - tests
---

# Восстановление общего фона перед кейсом

Общая фикстура даёт фон, нужный многим кейсам.
Базовый слой восстанавливает его до подготовки специфичной фикстуры, включая изменяемое состояние дублёров.

## SQL через обработчик тестового фреймворка

Декларация связывает скрипт и нужный источник данных; запуск выполняет общий жизненный цикл.

### Пример 1. Одна база

```kotlin
@Sql("classpath:db/reset-data.sql")
abstract class DatabaseTest
```

### Пример 2. Две базы

```kotlin
@Sql("classpath:db/accounts-fixture.sql",
    config = SqlConfig(dataSource = "accountsDataSource", transactionManager = "accountsTx"))
@Sql("classpath:db/content-fixture.sql",
    config = SqlConfig(dataSource = "contentDataSource", transactionManager = "contentTx"))
abstract class ApplicationTest
```

## Явный общий обработчик

Нужен для комбинации SQL-подготовки с очисткой дублёров и генераторов.

### Пример 1. База, генератор и HTTP-дублёр

```kotlin
@BeforeEach
fun setupTestData() {
    dataSource.setupDb()
    resetFaker()
    WireMock.reset()
}
```

### Пример 2. Дублёры компонентного окружения

```kotlin
@BeforeEach
fun resetDoubles() {
    fakeEmailSender.reset()
    fakeEventBus.reset()
}
```

## Границы применения

Общая фикстура определяется повторяемостью нужного фона, а не тем, создаётся ли она один раз.
Переиспользование контейнера не обязывает переиспользовать изменённые строки.
Перенос сброса с каждого кейса на каждый класс требует отдельно обеспечить изоляцию кейсов; это не автоматическое следствие данного приёма.

[К каталогу](../test-patterns.md).
