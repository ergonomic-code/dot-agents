---
keywords:
  - tests
---

# Точечная установка служебного состояния через SQL

Некоторые поля неудобно задавать обычным API ресурса: например, аудит заменяет указанное время текущим.
TestApi даёт именованный метод коррекции и скрывает SQL от вызывающего кода.

## Параметризованная коррекция нужных строк

Метод получает доменные идентификаторы и значения, а выбор таблиц и колонок остаётся внутри инфраструктуры.

### Пример 1. Время создания одной записи

```kotlin
fun setCreatedAt(id: UUID, createdAt: Instant) {
    val updated = jdbc.sql("UPDATE posts SET created_at = :at WHERE id = :id")
        .param("id", id).param("at", Timestamp.from(createdAt)).update()
    check(updated == 1) { "Публикация не найдена" }
}
```

### Пример 2. Активность нескольких записей

```kotlin
fun setActive(codes: List<String>, active: Boolean) {
    if (codes.isEmpty()) return
    jdbc.sql("UPDATE panels SET active = :active WHERE code IN (:codes)")
        .param("active", active).param("codes", codes).update()
}
```

## Границы применения

Коррекция через SQL не меняет границу TestApi.
Метод коррекции обслуживает состояние одного ресурса.
После SQL может понадобиться перечитывание данных — см. [возврат установленного состояния](10-installed-values.md).

[К каталогу](../test-patterns.md).
