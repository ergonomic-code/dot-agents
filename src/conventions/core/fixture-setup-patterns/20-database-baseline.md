---
keywords:
  - tests
---

# Подготовленное начальное состояние БД

Повторное создание всей схемы с нуля может занимать значительную часть бюджета тестов.
Окружение стартует с подготовленной схемы или БД-шаблона; сброс строк перед кейсом остаётся отдельной операцией.

## Клонирование тестовой БД из шаблона

Заранее подготовленная БД служит источником начального состояния.

### Пример 1. База приложения

```kotlin
connection.createStatement().use { statement ->
    statement.execute("DROP DATABASE IF EXISTS test_app")
    statement.execute("CREATE DATABASE test_app TEMPLATE test_app_template")
}
```

### Пример 2. База конфигурации

```kotlin
connection.createStatement().use { statement ->
    statement.execute("DROP DATABASE IF EXISTS test_settings")
    statement.execute("CREATE DATABASE test_settings TEMPLATE test_settings_template")
}
```

## Загрузка снимка при старте контейнера

Файл снимка и скрипт его применения передаются в инициализацию PostgreSQL.

### Пример 1. Один снимок

```kotlin
val container = PostgreSQLContainer("postgres:15.2")
    .withCopyFileToContainer(
        MountableFile.forClasspathResource("db/app-baseline.psql"),
        "/docker-entrypoint-initdb.d/app-baseline.psql",
    )
    .withCopyFileToContainer(
        MountableFile.forClasspathResource("db/init.sh"),
        "/docker-entrypoint-initdb.d/init.sh",
    )
```

### Пример 2. Несколько снимков

```kotlin
val container = createPgContainer(initFiles = listOf(
    InitFile("db/accounts-baseline.psql", "/docker-entrypoint-initdb.d/accounts-baseline.psql"),
    InitFile("db/content-baseline.psql", "/docker-entrypoint-initdb.d/content-baseline.psql"),
    InitFile("db/init.sh", "/docker-entrypoint-initdb.d/init.sh"),
))
```

## Границы применения

Снимок схемы и общая фикстура строк решают разные задачи.
Здесь не фиксируется единая политика обновления снимков и применения последующих миграций: её нельзя вывести из одних вызовов загрузки.
Команды пересоздания предназначены только для выделенных тестовых БД.

[К каталогу](../test-patterns.md).
