---
keywords:
  - tests
---

# Именованные варианты фрагмента

Кейс должен назвать нужную ситуацию, а не вручную согласовывать все связи.
Несколько фабрик строят разные ситуации в одной модели фрагмента и используют один установщик.

## Один фрагмент с разным наполнением

Фабрики различаются гарантируемой ситуацией, а не только произвольным именем.

### Пример 1. Календарь без событий и с событием

```kotlin
fun withSingleCalendar(): CalendarsFixture {
    val account = anAccount()
    return CalendarsFixture(account, listOf(aCalendar(account.ref())), emptyList())
}

fun withCalendarAndEvent(event: CalendarEvent): CalendarsFixture {
    val account = anAccount()
    val calendar = aCalendar(account.ref(), externalId = event.calendarId)
    return CalendarsFixture(account, listOf(calendar), listOf(event))
}
```

### Пример 2. Пустой день и день с измерением

```kotlin
fun emptyDay(day: LocalDate) = MeasurementsFixture(
    day = day, samples = emptyList(), expectedCount = 0,
)

fun dayWithSample(day: LocalDate) = MeasurementsFixture(
    day = day,
    samples = listOf(aSample(at = day.atTime(12, 0))),
    expectedCount = 1,
)
```

## Список фрагментов для общей ситуации

Если описание одного объекта уже достаточно, фабрика возвращает список таких фрагментов.

### Пример 1. Подписки в разных состояниях

```kotlin
fun subscriptionsInAllStates(owner: Owner, now: Instant): List<MemberFixture> = listOf(
    member(owner, confirmed = true, deleted = false, createdAt = now),
    member(owner, confirmed = false, deleted = false, createdAt = now),
    member(owner, confirmed = true, deleted = true, createdAt = now),
)
```

### Пример 2. Свои и чужие участники

```kotlin
fun selection(owner: Owner, otherOwner: Owner, now: Instant): List<MemberFixture> = listOf(
    member(owner, confirmed = true, deleted = false, createdAt = now),
    member(owner, confirmed = false, deleted = false, createdAt = now),
    member(otherOwner, confirmed = true, deleted = false, createdAt = now),
)
```

## Границы применения

Не нужен класс на каждый вариант ситуации.
Если параметры фабрики противоречат её имени, лучше изменить контракт фабрики, чем заставлять кейс помнить скрытые условия.

[К каталогу](../test-patterns.md).
