---
keywords:
  - tests
---

# Воспроизводимые случайные данные и время

Общая цель — детерминированные даты и случайные значения, чтобы фон кейса воспроизводился при повторном запуске.
Seed управляет случайной последовательностью; источник времени нужно контролировать отдельно.

## Сброс генератора перед кейсом

Обработчик жизненного цикла возвращает генератор к одному seed.

### Пример 1. Расширение JUnit

```kotlin
private const val SEED = 1L
var faker = Faker(Locale.of("ru"), Random(SEED))

fun resetRandom() { faker = Faker(Locale.of("ru"), Random(SEED)) }

class ResetRandomExtension : BeforeEachCallback {
    override fun beforeEach(context: ExtensionContext) = resetRandom()
}
```

### Пример 2. Общий обработчик подготовки

```kotlin
var faker = Faker(Locale.ENGLISH, Random(1))
    private set

fun resetFaker() { faker = Faker(Locale.ENGLISH, Random(1)) }

@BeforeEach
fun resetGenerators() { resetFaker() }
```

## Явная опорная дата или Clock

Генерация получает время как параметр; фиксированное время и seed вместе делают результат воспроизводимым.

### Пример 1. Случайный момент относительно Clock

```kotlin
fun anInstantInPast(clock: Clock, maxAge: Duration): Instant =
    clock.instant().minusMillis(faker.random().nextLong(0, maxAge.toMillis()))

val clock = Clock.fixed(Instant.parse("2030-04-01T00:00:00Z"), ZoneOffset.UTC)
val createdAt = anInstantInPast(clock, Duration.ofDays(1))
```

### Пример 2. Случайная дата между границами

```kotlin
fun nearFutureDate(after: LocalDate, before: LocalDate): LocalDate {
    val offset = faker.number().numberBetween(0L, ChronoUnit.DAYS.between(after, before))
    return after.plusDays(offset)
}

val arrival = nearFutureDate(LocalDate.of(2030, 4, 1), LocalDate.of(2030, 5, 1))
```

## Границы применения

Текущие даты допустимы там, где это уместно, например когда сценарий намеренно задаётся относительно сегодняшнего дня.
Недетерминированные идентификаторы допустимы там, где они обязательны; это исключение не отменяет общей цели.
Воспроизводимость последовательности зависит и от порядка вызовов генератора.
Общий изменяемый генератор и его сброс требуют согласованной модели параллельного запуска.

[К каталогу](../test-patterns.md).
