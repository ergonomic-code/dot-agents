---
keywords:
  - tests
---

# Отдельные фрагмент и инсталлер

Фрагмент хранит описание состояния, инсталлер выполняет обращения к зависимостям SUT.
Для этого нужны два класса: сам фрагмент и его инсталлер.
Отдельные классы фабрик и обёрток появляются только при необходимости.

## Данные плюс install(fixture)

Фабрика может быть функцией или методом companion object, а именованная подготовка — extension-функцией.

### Пример 1. Отель и комнаты

```kotlin
data class HotelFixture(val hotel: Hotel, val rooms: List<Room>)

class HotelFixtureInstaller(
    private val hotels: HotelsTestApi,
    private val rooms: RoomsTestApi,
) {
    fun install(fixture: HotelFixture): HotelFixture {
        val savedHotel = hotels.save(fixture.hotel)
        val savedRooms = rooms.saveAll(fixture.rooms)
        return HotelFixture(savedHotel, savedRooms)
    }
}
```

### Пример 2. Участник с необязательной карточкой

```kotlin
data class MemberFixture(val member: Member, val card: Card?)

class MemberFixtureInstaller(
    private val members: MembersTestApi,
    private val cards: CardsTestApi,
) {
    fun install(fixture: MemberFixture): MemberFixture {
        members.save(fixture.member)
        fixture.card?.let { cards.save(it) }
        return fixture
    }
}
```

## Границы применения

Определяй роль класса по его ответственности, а не только по имени.
Установщик оркестрирует несколько ресурсов; TestApi ограничен одним ресурсом.
Для согласованной группы разнородных объектов нужна фабрика фрагмента, а не расширение ObjectMother на любые типы.

[К каталогу](../test-patterns.md).
