---
keywords:
  - tests
---

# Согласованные входные и ожидаемые данные

Сгенерированное состояние нужно не только установить: из него кейс получает параметры вызова и ожидаемые значения.
Согласованное описание устраняет повторное угадывание ID, дат и связей в проверке.

## Готовое ожидание внутри фрагмента

Фабрика задаёт входные данные и ожидаемый результат рядом, независимо от работы SUT.

### Пример 1. Количество событий за день

```kotlin
fun dayWithEvents(day: LocalDate): DailyReportFixture {
    val events = listOf(anEvent(day.atTime(10, 0)), anEvent(day.atTime(11, 0)))
    return DailyReportFixture(day, events, expected = Report(count = 2))
}
```

### Пример 2. Значения за период

```kotlin
fun twoDays(): RangeReportFixture {
    val start = LocalDate.of(2030, 4, 1)
    val samples = listOf(aSample(start, 2.0), aSample(start.plusDays(1), 8.0))
    return RangeReportFixture(
        period = DatePeriod(start, start.plusDays(1)), samples = samples,
        expected = RangeReport(min = 2.0, max = 8.0),
    )
}
```

## Проекция фрагмента в ожидаемое представление

Данные хранятся во фрагменте, а простое представление для проверки собирается из них в кейсе.

### Пример 1. Настройки календарей

```kotlin
val fixture = calendarsWithVisibility(listOf(true, false))
installer.install(fixture)
val expected = fixture.calendarsAndSettings.map { (calendar, settings) ->
    CalendarView(calendar.externalId, calendar.name, settings.shouldBeShown)
}
```

### Пример 2. Данные аккаунта вокруг представления

```kotlin
val expectedAccount = AccountCalendarsView(
    email = fixture.account.email,
    calendars = fixture.calendarsAndSettings.map { (calendar, settings) ->
        CalendarView(calendar.externalId, calendar.name, settings.shouldBeShown)
    },
)
```

## Литералы в установщике с соседними входами и ожиданиями

### Пример 1. Установка фиксированного набора

```kotlin
class ReportFixtureInstaller(private val samples: SamplesTestApi) {
    fun installTwoSamples(): ReportFixture {
        val fixture = ReportFixture(
            samples = listOf(aSample(value = 2.0), aSample(value = 8.0)),
            expected = Report(min = 2.0, max = 8.0),
        )
        samples.saveAll(fixture.samples)
        return fixture
    }
}
```

### Пример 2. Установка с явно заданным порогом

```kotlin
class ThresholdFixtureInstaller(private val readings: ReadingsTestApi) {
    fun installOutOfRange(): ThresholdFixture {
        val fixture = ThresholdFixture(
            allowed = 10..20, reading = aReading(value = 25),
            expectedStatus = Status.ABOVE_RANGE,
        )
        readings.setAllowedRange(fixture.allowed)
        readings.save(fixture.reading)
        return fixture
    }
}
```

## Границы применения

Литералы в установщике допустимы при совместном задании входных и ожидаемых значений рядом.
Это не разрешение незаметно выбрать порог внутри install, оставив вызывающему коду угадывать ожидаемый статус.
Готовое ожидание задаётся по требованию к поведению; повторный запуск проверяемого алгоритма для получения ожидания не решает задачу проверки.
Два обязательных класса сохраняются и в примерах с литералами: Fixture описывает данные, FixtureInstaller устанавливает их.

[К каталогу](../test-patterns.md).
