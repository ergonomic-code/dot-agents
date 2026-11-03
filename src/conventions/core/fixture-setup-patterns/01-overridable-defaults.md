---
keywords:
  - tests
---

# Фабрика с переопределяемыми дефолтами

Кейсу нужны конкретные значения нескольких полей, но для создания валидного объекта приходится заполнить остальные.
Фабрика принимает поля именованными параметрами и даёт несущественным значениям дефолты.
Один ObjectMother обслуживает сущность и DTO вокруг неё.

## Именованные параметры фабрики

Фабрика передаёт значения обычному конструктору, не обращаясь к зависимостям SUT.

### Пример 1. Комната отеля

```kotlin
fun aRoom(
    hotel: HotelRef = theHotel.ref,
    roomType: RoomType = RoomType.entries.randomElement(),
    roomNumber: Int = aRoomNumber(),
) = Room(hotel, roomType, roomNumber)

val room = aRoom(roomType = RoomType.SINGLE)
```

### Пример 2. Запрос на публикацию

```kotlin
fun aPublishPostRq(
    title: String = aPostTitle(),
    text: String = aPostText(),
    attachment: FileContent? = null,
) = PublishPostRq(title, text, attachment)

val request = aPublishPostRq(title = "Обновление расписания")
```

## Границы применения

Дефолты должны давать допустимый фон, а значения, определяющие проверяемое поведение, задаёт вызывающий код.
Группу разных типов, согласованную для общей ситуации, строит фабрика фрагмента — см. [построение графа](06-in-memory-graph.md).

[К каталогу](../test-patterns.md).
