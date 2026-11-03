---
keywords:
  - tests
---

# Согласованная установка локального и внешнего состояния

Одна ситуация может включать строки БД и объекты, доступные только через внешний API.
Общее описание связывает их идентификаторы; инсталлер применяет его ко всем нужным зависимостям.

## Один инсталлер устанавливает несколько частей

Многоресурсная координация находится в инсталлере, а каждый нижележащий TestApi или дублёр ограничен своим ресурсом.

### Пример 1. Аккаунт и внешние календари

```kotlin
fun install(fixture: CalendarsFixture) {
    fixture.accounts.forEach { (account, token) ->
        accounts.save(account)
        oauth.OnRefreshToken(account.refreshToken).returnsToken(token)
        val calendars = fixture.calendarsFor(account)
        calendarServer.OnGetCalendars(token).returnsCalendars(calendars)
    }
}
```

### Пример 2. Настройки и внешние события

```kotlin
fun install(fixture: CalendarEventsFixture) {
    settings.saveAll(fixture.settings)
    fixture.calendars.forEach { calendar ->
        val events = fixture.events.filter { it.calendarId == calendar.id }
        calendarServer.OnGetEvents(fixture.token, calendar.id).returnsEvents(events)
        events.forEach { event ->
            calendarServer.OnGetEventById(fixture.token, event.id).returnsEvent(event)
        }
    }
}
```

## Композиция вложенных инсталлеров

Общая ситуация может включать самостоятельный фрагмент со своим установщиком.

### Пример 1. Расписание и интеграция календаря

```kotlin
fun install(fixture: ScheduleFixture) {
    clients.saveAll(fixture.clients)
    appointments.saveAll(fixture.appointments)
    calendarInstaller.install(fixture.calendars)
}
```

### Пример 2. Та же композиция с другой ситуацией

```kotlin
val fixture = ScheduleFixture(
    clients = emptyList(),
    appointments = emptyList(),
    calendars = CalendarsFixture.withCalendarAndEvent(anExternalEvent()),
)
scheduleInstaller.install(fixture)
```

## Границы применения

Совпадающие идентификаторы должны происходить из общего описания, а не из неявно одинаковых литералов в разных хелперах.
TestApi нескольких ресурсов был бы нарушением границы; перенос координации в инсталлер сохраняет эту границу.
Наличие вложенного фрагмента не требует выделять отдельный класс фабрики.

[К каталогу](../test-patterns.md).
