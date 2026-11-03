---
keywords:
  - tests
---

# Возврат фактически установленного состояния

Сохранение может назначить ID, изменить время аудита или точность значения.
Возвращённое описание должно позволять кейсу ссылаться на действительно установленное состояние.

## Использовать результат сохранения

Если save возвращает нужные значения, из них собирается обновлённый фрагмент.

### Пример 1. Сохранённые отель и комнаты

```kotlin
fun install(fixture: HotelFixture): HotelFixture {
    val hotel = hotels.save(fixture.hotel)
    val rooms = rooms.saveAll(fixture.rooms)
    return HotelFixture(hotel, rooms)
}
```

### Пример 2. Созданная учётная запись и профиль

```kotlin
fun install(request: CreateAccountRq): AccountFixture {
    val account = accounts.createConfirmed(request)
    val profileId = profiles.getIdByAccount(account.id)
    return AccountFixture(account, profileId)
}
```

## Перечитать после коррекции состояния

Когда установка включает дополнительное изменение записи, результат читается после последнего шага.

### Пример 1. Заданное время вместо времени аудита

```kotlin
fun install(fixture: MemberFixture): MemberFixture {
    val installed = fixture.subscriptions.map { subscription ->
        val saved = subscriptions.create(subscription)
        subscriptions.create(saved.copy(createdAt = subscription.createdAt))
        subscriptions.get(saved.id)
    }
    return fixture.copy(subscriptions = installed)
}
```

### Пример 2. Перечитывание после SQL-коррекции

```kotlin
fun install(fixture: PostFixture): PostFixture {
    val saved = posts.create(fixture.post)
    posts.setCreatedAt(saved.id, fixture.post.createdAt)
    return fixture.copy(post = posts.get(saved.id))
}
```

## Границы применения

Перечитывание нужно, когда сохранение действительно меняет значимые для последующих действий значения.
Если описание уже соответствует установленному состоянию, можно вернуть исходный фрагмент.
Возврат фактических данных не должен подменять ожидаемый результат проверяемого действия его реальным результатом.

[К каталогу](../test-patterns.md).
