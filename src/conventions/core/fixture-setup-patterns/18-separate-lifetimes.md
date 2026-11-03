---
keywords:
  - tests
---

# Разные сроки жизни окружения и данных

Запуск БД и приложения обычно дороже восстановления строк.
Контейнеры, подключения и контексты переиспользуются, а состояние для кейса подготавливается отдельно.

## Ленивое общее окружение и покейсовый сброс

Ленивость определяет момент создания, область хранения — длительность жизни, а обработчик кейса — момент сброса данных.

### Пример 1. Контейнер БД

```kotlin
val pgContainer by lazy {
    PostgreSQLContainer("postgres:15.2")
        .withReuse(true)
        .apply { start() }
}

@BeforeEach
fun restoreRows() { dataSource.setupDb() }
```

### Пример 2. Общее подключение к базе

```kotlin
val accountsDataSource by lazy {
    HikariDataSource(HikariConfig().apply {
        jdbcUrl = pgContainer.jdbcUrl
        username = pgContainer.username
        password = pgContainer.password
    })
}

@BeforeEach
fun restoreAccounts() { dbInitializer.execute("db/accounts-fixture.sql") }
```

## Границы применения

withReuse и singleton в процессе — разные механизмы переиспользования; одной настройки withReuse недостаточно для описания всего жизненного цикла.
Общее окружение не обеспечивает изоляцию параллельных кейсов само по себе.

[К каталогу](../test-patterns.md).
