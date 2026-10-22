# Сложные тестовые фикстуры на Kotlin и Spring

Реализация [общей модели](../../conventions/core/test-fixture-architecture.md) разделяет чистые данные и установку состояния.
Канонические фабрики одного типа `Fixture` размещай в его `companion object`, именованную подготовку — в функциях расширения установщика.

## Модель и фабрика

Пример проверяет сумму заказов не ниже настроенного порога.
Суммы заданы целыми числами в минимальных денежных единицах.

```kotlin
data class OrderSpec(val amount: Int)

data class ReportFixture(
    val orders: List<OrderSpec>,
    val minimumAmount: Int,
    val expectedTotal: Int,
) {
    companion object {
        fun onThreshold() = ReportFixture(
            orders = listOf(OrderSpec(99), OrderSpec(100), OrderSpec(101)),
            minimumAmount = 100,
            expectedTotal = 201,
        )
    }
}
```

Фабрика и модель не зависят от Spring и не обращаются к системе.

## Установщик и именованная подготовка

`OrdersTestApi.create(order)` и `ReportSettingsTestApi.setMinimumAmount(amount)` — существующие или добавляемые хелперы соответствующих областей приложения.
Они инкапсулируют обращения к продакшн-компонентам.

```kotlin
class ReportFixtureInstaller(
    private val ordersTestApi: OrdersTestApi,
    private val reportSettingsTestApi: ReportSettingsTestApi,
) {
    fun install(fixture: ReportFixture) {
        reportSettingsTestApi.setMinimumAmount(fixture.minimumAmount)
        fixture.orders.forEach { ordersTestApi.create(it) }
    }
}

fun ReportFixtureInstaller.setupOnThreshold(): ReportFixture {
    val fixture = ReportFixture.onThreshold()
    install(fixture)
    return fixture
}
```

Новый набор значений требует новой фабрики, но не нового установщика.
Если новое состояние требует дополнительной настройки системы, опиши её в фикстуре и реализуй в `install`, сохранив расширение связкой фабрики и установки.

## Подключение Spring

Регистрируй установщик через явный `@Import` в тестовой конфигурации.
Его зависимости внедряются через конструктор; соответствующие `*TestApi` должны быть зарегистрированы существующей тестовой инфраструктурой.
Чистые фабрики и функции расширения не регистрируй как Spring-бины.

```kotlin
import org.springframework.boot.test.context.TestConfiguration
import org.springframework.context.annotation.Import

@TestConfiguration(proxyBeanMethods = false)
@Import(ReportFixtureInstaller::class)
class TestFixturesConf
```

Подключи `TestFixturesConf` через `@Import(TestFixturesConf::class)` к тесту с инфраструктурой или его общей тестовой конфигурации.
Внедри `ReportFixtureInstaller` в класс теста средствами принятой в проекте интеграции Spring с тестовым фреймворком.

## Использование в тестах

Фрагменты показывают тела отдельных кейсов; `calculator` и `reportApi` обозначают проверяемое вычисление и хелпер внешней границы приложения.
В тесте вычислений инфраструктура не нужна:

```kotlin
// Given
val fixture = ReportFixture.onThreshold()
// When
val actual = calculator.calculate(fixture.orders, fixture.minimumAmount)
// Then
assertEquals(fixture.expectedTotal, actual)
```

В тесте с инфраструктурой используй расширение установщика:

```kotlin
// Given
val fixture = reportFixtureInstaller.setupOnThreshold()
// When
val actual = reportApi.getTotal()
// Then
assertEquals(fixture.expectedTotal, actual)
```

Если расширения для готового варианта ещё нет, в подготовке явно вызови фабрику и `reportFixtureInstaller.install(fixture)`.
Проверяемое действие и утверждения остаются в кейсе.
