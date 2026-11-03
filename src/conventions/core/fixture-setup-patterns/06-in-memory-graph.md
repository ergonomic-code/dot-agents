---
keywords:
  - tests
---

# Связанный граф до установки

Если идентификаторы известны заранее, связанные объекты можно полностью собрать в памяти.
Фабрика фрагмента связывает разнородные объекты, а отдельный установщик затем переносит описание в зависимости SUT.

## Ссылки на заранее созданные объекты

Тип идентификатора несущественен: важно получить его до сохранения связанного графа.

### Пример 1. Отель с комнатой

```kotlin
fun hotelWithRoom(roomType: RoomType): HotelFixture {
    val hotel = aHotel()
    return HotelFixture(
        hotel = hotel,
        rooms = listOf(aRoom(hotel = hotel.ref(), roomType = roomType)),
    )
}
```

### Пример 2. Участник и подписка

```kotlin
private val nextMemberId = AtomicInteger(1_000_000)

fun subscribedMember(ownerId: Int): MemberFixture {
    val member = aMember(id = nextMemberId.getAndIncrement())
    return MemberFixture(
        member = member,
        subscriptions = listOf(aSubscription(memberId = member.id, ownerId = ownerId)),
    )
}
```

## Границы применения

У счётчика отдельно определяется срок жизни и сброс; сам факт использования AtomicInteger не делает все кейсы детерминированными.
Если ID неизбежно назначает БД, преждевременно строить ссылки на него нельзя: понадобится этап установки с возвратом фактических значений.
Минимум классов для фрагмента — сам фрагмент и инсталлер; фабрика не обязана быть отдельным классом.

[К каталогу](../test-patterns.md).
