# Скрытые фиксированные данные в хелперах фикстур

## Свидетельства

Сессия: `01a186ba-4643-7da0-8b0d-34b2a918e2b2`.
При рефакторинге тестов хелперы фикстур скрывали фиксированные входные данные, которые кейс не мог переопределить.

Релевантный запрос пользователя, обобщённый пересказ: убрать фиксированные тестовые данные из реализации хелперов фикстур, оставив их только как переопределяемые значения параметров по умолчанию.

## Проблемный код

Сокращённая обезличенная реконструкция хелпера; тест иллюстрирует дублирование его скрытых значений.
Имена и значения заменены.

```kotlin
fun fixture(value: Double, status: Status): Fixture {
    val range = Range(10.0, 20.0)
    val recordedAt = Instant.parse("2025-01-01T12:00:00Z")
    val event = anEvent(value = value, recordedAt = recordedAt)
    return Fixture(
        range = range,
        event = event,
        warning = Warning(event.id, value, recordedAt, status),
    )
}

@Test
fun test_warning() {
    // Given
    val fixture = installer.install(fixture(value = 9.0, status = Status.LOW))
    val warning = Warning(
        fixture.event.id,
        9.0,
        Instant.parse("2025-01-01T12:00:00Z"),
        Status.LOW,
    )

    // When
    val result = api.getState()

    // Then
    result.warning shouldBe warning
}
```

Кейс может задать значение и статус, но не диапазон и время события.
Чтобы согласовать вход с ожиданием, ему приходится знать реализацию хелпера, что подталкивает к дублированию скрытых значений при вызове SUT или проверке.

## Целевой код

Хелпер принимает все данные через параметры, сохраняя удобные значения по умолчанию.
Тест явно задаёт значимые входные данные и использует их же для ожидания.

```kotlin
fun fixture(
    value: Double,
    status: Status,
    range: Range = Range(10.0, 20.0),
    recordedAt: Instant = Instant.parse("2025-01-01T12:00:00Z"),
): Fixture {
    val event = anEvent(value = value, recordedAt = recordedAt)
    return Fixture(
        range = range,
        event = event,
        warning = Warning(event.id, value, recordedAt, status),
    )
}

@Test
fun test_warning() {
    // Given
    val range = Range(30.0, 40.0)
    val value = 29.0
    val status = Status.LOW
    val recordedAt = Instant.parse("2025-02-01T09:00:00Z")
    val fixture = installer.install(fixture(value, status, range, recordedAt))
    val warning = Warning(fixture.event.id, value, recordedAt, status)

    // When
    val result = api.getState()

    // Then
    result.warning shouldBe warning
}
```

## Контекст и причина

В сессии есть вызовы чтения `src/context/tests.md` и соглашений `test-design.md`, `test-fixture-architecture.md`, `test-implementation.md` из `src/conventions/core/`.
Сам факт вызова не подтверждает полноту прочитанного контекста: объём вывода был ограничен.
Подтверждённый пробел соглашений до исправления — отсутствие запрета скрытых фиксированных тестовых данных в хелперах.
Пропуск маршрутизации как причина не подтверждён.

## Исправление

- В разделе «Границы хелперов» файла `test-fixture-architecture.md` запрещены фиксированные тестовые данные вне переопределяемых значений параметров по умолчанию.
  Данные передаются параметрами или описанием фикстуры, а связанные значения выводятся из них.
- В `test-implementation-checklist.md` добавлена проверка хелперов.

## Проверка и влияние

Соглашение и чек-лист уже подключены через `src/context/tests.md`; маршрутизация не меняется.
Пользовательские операции, установка, поддерживаемая область и точки входа не меняются, поэтому обновление `README.md` не требуется.
Тесты на человекочитаемые формулировки не добавляются.
При проверке исправления соглашений `pytest -q`: 151 passed.
`git diff --check`: замечаний нет.
Ревью по `review-framework-changes`: `ok`, замечаний нет.
