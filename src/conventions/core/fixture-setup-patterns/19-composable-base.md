---
keywords:
  - tests
---

# Составной базовый слой

> 🚧 WIP: организация составного базового слоя ещё не устоялась.

Общее окружение хочется собирать из более узких частей и подключать к тесту короткой декларацией.
Механизм композиции ещё не устоялся; окончательная форма архитектуры пока не определена.

## Составные аннотации

Одна аннотация добавляет возможности к уже существующему набору.

### Пример 1. Окружение с БД

```kotlin
@Target(AnnotationTarget.CLASS)
@Retention(AnnotationRetention.RUNTIME)
@MariotteRuntimeTest
@Sql("classpath:db/reset-data.sql")
@Import(DbTestConfig::class)
annotation class MariotteDbTest
```

### Пример 2. API поверх окружения БД

```kotlin
@Target(AnnotationTarget.CLASS)
@Retention(AnnotationRetention.RUNTIME)
@MariotteDbTest
@SpringBootTest(classes = [HotelsApp::class], webEnvironment = SpringBootTest.WebEnvironment.MOCK)
@Import(ApiSessionsFactoryTestConf::class)
annotation class MariotteApiTest
```

## Общая фикстура как примесь к базовому классу

Один интерфейс с обработчиками жизненного цикла добавляет доменный фон разным типам тестов.

### Пример 1. Компонентный тест

```kotlin
interface CatalogSharedFixture {
    val dbInitializer: DbInitializer
    @BeforeEach
    fun setupCatalog() { dbInitializer.execute("db/catalog-fixture.sql") }
}

class CountItemsTest : ComponentTest(), CatalogSharedFixture
```

### Пример 2. Граничное окружение с тем же фоном

```kotlin
abstract class CatalogApiTest : ApplicationTest(), CatalogSharedFixture {
    protected fun loginAsEditor(): ApiSession = apiSessions.login(EDITOR)
}

class ListItemsTest : CatalogApiTest()
```

## Границы применения

WIP относится к организации и композиции базового слоя, а не к самому факту общего жизненного цикла.
Пока не закреплены единая форма графа общих фикстур и правила совмещения их обработчиков.
Базовый слой входит в инфраструктуру тестов и не должен зависеть от конкретных кейсов.

[К каталогу](../test-patterns.md).
