# Пример тестовой HTTP-обвязки на Kotlin и Spring

Кейс вызывает доменную операцию и получает типизированный результат, а обвязка выполняет HTTP-запрос, проверяет контракт и разбирает ответ.
Пример соединяет `ApiSession`, специализированную сессию, `ApiSessionsFactory` и `UserProfileApi` на одной операции обновления профиля.
Он рассчитан на Spring Framework 7, Jackson 3 и Bearer-авторизацию.

Код размещается в тестовой инфраструктуре приложения; фрагменты предполагают один пакет.
Скопируй туда [общую инфраструктуру HTTP-тестов](http-api-test-support.md): интерцептор, хелперы проверки схем и типы результата.
Точки адаптации к приложению: DTO `UpdateProfile`, `UserProfile`, `ApiError` с полем `errorCode: String?`, маршрут операции, схемы `ProfileSchemas.updateRequest`, `ProfileSchemas.profile`, `ProfileSchemas.error` и операция входа.
`assertJsonMatchesSchema(json, schema)` — адаптер к выбранному валидатору: возвращает `Unit` либо бросает `AssertionError`.

## Настройка транспорта

Конвертеры используют настройки сериализации приложения; интерцептор проверяет то тело, которое они действительно отправят.
`webApplicationContext` — контекст тестируемого приложения, `jsonMapper` — его настроенный маппер.
Этот фрагмент выполняется в общей тестовой конфигурации.

```kotlin
import org.springframework.http.converter.json.JacksonJsonHttpMessageConverter
import org.springframework.test.web.servlet.client.RestTestClient

val restClient = RestTestClient.bindToApplicationContext(webApplicationContext)
    // остальные настройки тестового клиента проекта
    .requestInterceptor(RequestBodySchemaValidationInterceptor(::assertJsonMatchesSchema))
    .build()
```

## Сессии и фабрика

Сессия хранит транспорт и авторизацию; фабрика получает токен через операцию входа приложения.
`asApi` меняет только представление сессии и сохраняет её транспорт и токен.

```kotlin
import org.springframework.test.web.servlet.client.RestTestClient

interface ApiSession {
    val restClient: RestTestClient
    val auth: String?
}

class UserApiSession(
    override val restClient: RestTestClient,
    override val auth: String?,
) : ApiSession

fun <T : ApiSession> ApiSession.asApi(
    create: (RestTestClient, String?) -> T,
): T = create(restClient, auth)

class ApiSessionsFactory(
    private val restClient: RestTestClient,
    private val authenticate: (String, String) -> String,
) {
    fun login(login: String, password: String): ApiSession =
        session(authenticate(login, password))

    fun anonymous(): ApiSession = session(null)

    private fun session(auth: String?): ApiSession = object : ApiSession {
        override val restClient = this@ApiSessionsFactory.restClient
        override val auth = auth
    }
}
```

В общей конфигурации создай `ApiSessionsFactory(restClient, ::authenticate)`.
Здесь `authenticate` получает логин и пароль и возвращает токен; передай метод API входа, который выполняет запрос и проверяет его ответ.

## Доменный API и варианты результата

Все пути используют один построитель запроса `updateProfileForResponse`.
Метод успеха возвращает профиль; `*ForError` — ожидаемую ошибку; `*ForOutcome` — типизированный выбор между успехом и явно разрешёнными ошибками.
`*ForResponse` также доступен кейсам, проверяющим сам HTTP-контракт.

```kotlin
import org.springframework.http.HttpStatus
import org.springframework.http.HttpStatusCode
import org.springframework.test.web.servlet.client.RestTestClient

val UserApiSession.profileApi: UserProfileApi
    get() = UserProfileApi(this)

class UserProfileApi(private val session: ApiSession) {
    
    fun updateProfile(request: UpdateProfile): UserProfile =
        updateProfileForResponse(request)
            .expectStatus().isOk
            .getBodyMatchingSchema(ProfileSchemas.profile)

    fun updateProfileForError(
        request: UpdateProfile,
        expectedStatus: HttpStatusCode,
    ): ApiError = updateProfileForResponse(request)
        .expectStatus().isEqualTo(expectedStatus)
        .getBodyMatchingSchema(ProfileSchemas.error)

    fun updateProfileForOutcome(
        request: UpdateProfile,
        expectedErrors: Set<ExpectedHttpError>,
    ): HttpOutcome<UserProfile, ApiError> =
        updateProfileForResponse(request).toHttpOutcome(
            successStatus = HttpStatus.OK,
            successBodySchema = ProfileSchemas.profile,
            expectedErrors = expectedErrors,
        )

    fun updateProfileForResponse(body: Any): RestTestClient.ResponseSpec {
        val request = session.restClient.put().uri("/users/me/profile")
            .headers { headers -> session.auth?.let { headers.setBearerAuth(it) } }
            .body(body)
        if (body is UpdateProfile) {
            request.ensureBodyMatchesSchema(ProfileSchemas.updateRequest)
        }
        return request.exchange()
    }

}
```

`*ForError` проверяет ожидаемый HTTP-статус и схему, затем возвращает типизированную ошибку; её доменные свойства проверяет кейс семантическими проверками проекта.
`*ForOutcome` делегирует общему `toHttpOutcome`: тот проверяет схему выбранной ветки, согласованность статуса ошибки и вхождение ошибки в разрешённое сценарием множество.
Построитель проверяет схему запроса только для `body is UpdateProfile`; остальные тела отправляет без проверки, позволяя тестировать невалидный JSON.

Свойство расширения `UserApiSession.profileApi` создаёт API для сессии без добавления поля в её класс; тот же класс API может обслуживать другие специализированные сессии.

## Вызовы из кейсов

Каждый фрагмент ниже иллюстрирует отдельный сценарий.
`request` и `expectedError` задаются его фикстурами и контрактом; ожидаемая ошибка содержит HTTP-статус и код ошибки.

```kotlin
val user = apiSessionsFactory.login(login, password).asApi(::UserApiSession)
val profile = user.profileApi.updateProfile(request)
// Здесь — проверки доменных данных профиля.

val anonymous = apiSessionsFactory.anonymous().asApi(::UserApiSession)
val error = anonymous.profileApi.updateProfileForError(request, HttpStatus.UNAUTHORIZED)
// Здесь — семантическая проверка ожидаемого кода и данных ошибки.

// Кейс на отклонение синтаксически невалидного JSON:
user.profileApi.updateProfileForResponse("{")
    .expectStatus().isBadRequest

// Кейс, где успех и конкретная ошибка допустимы, например при конкуренции:
val outcome = user.profileApi.updateProfileForOutcome(request, setOf(expectedError))

// Вызов пользовательского API с исходной авторизацией администратора:
val admin = apiSessionsFactory.login(adminLogin, adminPassword)
val userView = admin.asApi(::UserApiSession)
```

Для `outcome` кейс проверяет доменные данные выбранной ветки; сам API уже проверил статус, схему и допустимость ошибки.
Выбор `UserApiSession` не выдаёт пользователю новых прав: сервер получает токен исходной сессии.
