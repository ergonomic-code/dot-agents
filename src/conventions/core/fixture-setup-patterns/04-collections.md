---
keywords:
  - tests
---

# Коллекция через фабрику одного элемента

Для списка не нужно повторять устройство отдельного объекта.
Функция коллекции управляет количеством и различиями элементов, а создание каждого объекта оставляет его фабрике.

## Только количество

Подходит, когда элементы отличаются лишь несущественными сгенерированными значениями.

### Пример 1. Карточки клиентов

```kotlin
fun createClientCardDtos(count: Int): List<ClientCardDto> =
    (1..count).map { createClientCardDto() }
```

### Пример 2. Запросы на публикацию

```kotlin
fun aPostRequests(count: Int = 3): List<PostRq> =
    (1..count).map { aPostRq() }
```

## Настройка элемента по индексу

Вызывающий код задаёт различия элементов функцией, сохраняя остальные дефолты фабрики.

### Пример 1. Разные заголовки

```kotlin
fun aPostRequests(
    count: Int,
    create: (Int) -> PostRq = { aPostRq() },
) = (1..count).map(create)

val requests = aPostRequests(3) { index -> aPostRq(title = "Пост $index") }
```

### Пример 2. Разные периоды действия

```kotlin
val now = Instant.parse("2030-04-01T00:00:00Z")
val periods = listOf(
    DatePeriod(now.minusSeconds(7200), now.minusSeconds(3600)),
    DatePeriod(now.minusSeconds(60), now.plusSeconds(3600)),
    DatePeriod(now.plusSeconds(7200), now.plusSeconds(10800)),
)
val requests = aPostRequests(7) { index ->
    aPostRq(period = periods[(index - 1) % periods.size])
}
```

## Границы применения

Функция коллекции может обеспечивать согласованность объектов одного типа, например уникальные логины.
Наличие случайных значений само по себе не гарантирует уникальности.
Согласование разнородных объектов относится к фабрике фрагмента.

[К каталогу](../test-patterns.md).
