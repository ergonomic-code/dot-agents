---
keywords:
  - tests
---

# Прямая композиция подготовки в кейсе

Кейс выбирает подходящий уровень инфраструктуры для каждого шага.
Пресет не является обязательной точкой входа: можно сочетать готовую подготовку, фабрики, инсталлеры и прямые вызовы TestApi.


## Пресет и дополнительный вызов TestApi

Готовая подготовка создаёт фон, а кейс уточняет существенный для проверки признак.

### Пример 1. Дата публикации для фильтра

```kotlin
val fixture = postInstaller.setupPublished()
val createdAt = Instant.parse("2030-04-01T10:00:00Z")
posts.setCreatedAt(fixture.post.id, createdAt)

val result = api.listPosts(createdAfter = createdAt.minusSeconds(1))
result.ids shouldContain fixture.post.id
```

### Пример 2. Изменение ответа внешнего календаря

```kotlin
val fixture = calendarInstaller.setupSingleCalendar()
mockCalendar.OnGetCalendars(fixture.token).returnsForbidden()

val result = api.getCalendarSettings()
result.accountStatus shouldBe AccountStatus.UNAVAILABLE
```

## ObjectMother и прямой вызов TestApi

Для простого состояния достаточно сгенерировать объект и сохранить его, не создавая отдельный пресет.

### Пример 1. Содержимое вложения

```kotlin
val attachment = anAttachment()
val request = aFullPostRq(file = attachment)
val post = posts.create(request)

val result = api.getAttachment(post.fileRef!!.id, attachment.mediaType)
result shouldBe attachment.content
```

### Пример 2. Имя скачиваемого файла

```kotlin
val filename = "guide.pdf"
val attachment = anAttachment(name = filename)
val post = posts.create(aFullPostRq(file = attachment))

val response = api.getAttachmentResponse(post.fileRef!!.id)
response.expectHeader().contentDisposition(
    ContentDisposition.attachment().filename(filename).build(),
)
```

## Фабрика фрагмента и явная установка

Кейс получает описание до установки и может использовать его при подготовке запроса и ожидания.

### Пример 1. Отель с комнатой

```kotlin
val fixture = HotelFixture.withRoom(RoomType.SINGLE)
val installed = hotelInstaller.install(fixture)

val request = aReservationRq(room = installed.rooms.single().ref())
val result = api.reserve(request)
result.roomId shouldBe installed.rooms.single().id
```

### Пример 2. Измерение за пределами диапазона

```kotlin
val fixture = MemberFixture.withMeasurement(value = 25.0, allowed = 10.0..20.0)
memberInstaller.install(fixture)

val result = api.getAlerts(fixture.member.id)
result.status shouldBe AlertStatus.ABOVE_RANGE
```

## Границы применения

Прямое использование TestApi не переносит в кейс SQL или устройство HTTP-дублёра.
Если из уточнений складывается повторяющаяся согласованная ситуация, её можно оформить фабрикой фрагмента.
Перечисленные варианты — способы организации Given, а не дополнительные обязанности инфраструктурных классов.

[К каталогу](../test-patterns.md).
