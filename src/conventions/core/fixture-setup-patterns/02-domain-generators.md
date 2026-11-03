---
keywords:
  - tests
---

# Доменный генератор поверх универсального

Универсальный генератор умеет создавать строки и числа, но сам по себе не знает ограничений домена.
Небольшая именованная функция превращает его возможности в генерацию допустимого доменного значения.

## Функция с доменными ограничениями

Ограничение может быть диапазоном, форматом или выборкой допустимых значений.

### Пример 1. Номер комнаты

```kotlin
fun aRoomNumber(): Int = faker.number().numberBetween(1, 10_000)

fun aRoom(roomNumber: Int = aRoomNumber()) =
    Room(hotel = theHotel.ref, roomType = RoomType.SINGLE, roomNumber = roomNumber)
```

### Пример 2. Заголовок публикации

```kotlin
private val postTitles = listOf("Новый маршрут", "Изменение расписания")

fun aPostTitle(): String = faker.randomElementOf(postTitles)

fun aPublishPostRq(title: String = aPostTitle()) =
    PublishPostRq(title = title, text = aPostText())
```

## Границы применения

Отдельный класс для каждого генератора не нужен: функция может находиться рядом с ObjectMother или внутри него.
Генератор допустимых значений не заменяет явную подготовку граничного или невалидного значения.

[К каталогу](../test-patterns.md).
