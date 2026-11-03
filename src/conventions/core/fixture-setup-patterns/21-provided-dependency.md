---
keywords:
  - tests
---

# Готовая зависимость с резервным запуском контейнера

Локально тестовая зависимость может быть уже запущена.
Базовый слой сначала пробует её использовать и при недоступности запускает контейнер, предоставляя кейсам один и тот же тип клиента.

## Проверка подключения и резервный путь

Выбор способа запуска остаётся в инфраструктуре, а не в кейсе.

### Пример 1. PostgreSQL

```kotlin
val testJdbcUrl by lazy {
    try {
        DriverManager.getConnection(providedTestUrl, user, password).use { connection ->
            prepareTestDatabase(connection)
        }
        providedTestUrl
    } catch (e: SQLException) {
        pgContainer.jdbcUrl
    }
}
```

### Пример 2. Объектное хранилище

```kotlin
val providedClient by lazy {
    runCatching { minioClient(providedTestUrl).also { it.listBuckets() } }
}

val testStorage by lazy {
    providedClient.getOrElse {
        minioClient("http://${minioContainer.host}:${minioContainer.firstMappedPort}")
    }
}
```

## Границы применения

В показанном варианте перехватываются также ошибки подготовки, а не только недоступность сервера.
Это не обязательное условие паттерна: политика резервного запуска должна позволять отличить недоступность от поломанной подготовки.
Приём не является обязательной частью архитектуры фикстур.

[К каталогу](../test-patterns.md).
