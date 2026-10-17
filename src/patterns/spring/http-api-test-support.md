# Общая инфраструктура тестов HTTP API

Код для копирования в тестовую инфраструктуру в проектах на Kotlin и Spring Framework 7.

## Проверка тела запроса

Доменный API запрашивает валидацию тела запроса через `ensureBodyMatchesSchema`; интерцептор проверяет уже сериализованные байты перед отправкой.
Без отметки запрос отправляется без проверки, что позволяет тестировать отклонение невалидного тела сервером.
Использован тип `com.networknt.schema.Schema`; адаптируй его к версии валидатора проекта.

```kotlin
import com.networknt.schema.Schema
import org.springframework.http.HttpRequest
import org.springframework.http.client.ClientHttpRequestExecution
import org.springframework.http.client.ClientHttpRequestInterceptor
import org.springframework.http.client.ClientHttpResponse
import org.springframework.test.web.servlet.client.RestTestClient

private const val REQUEST_BODY_SCHEMA_ATTRIBUTE = "tests.requestBodySchema"

fun <S : RestTestClient.RequestHeadersSpec<*>> S.ensureBodyMatchesSchema(schema: Schema): S =
    apply { attribute(REQUEST_BODY_SCHEMA_ATTRIBUTE, schema) }

class RequestBodySchemaValidationInterceptor(
    private val assertMatchesSchema: (String, Schema) -> Unit,
) : ClientHttpRequestInterceptor {
    override fun intercept(
        request: HttpRequest,
        body: ByteArray,
        execution: ClientHttpRequestExecution,
    ): ClientHttpResponse {
        val schema = request.attributes[REQUEST_BODY_SCHEMA_ATTRIBUTE] as? Schema
        if (schema != null) {
            val charset = request.headers.contentType?.charset ?: Charsets.UTF_8
            try {
                assertMatchesSchema(body.toString(charset), schema)
            } catch (failure: AssertionError) {
                throw AssertionError(
                    "${request.method} ${request.uri}: request body schema mismatch",
                    failure,
                )
            }
        }
        return execution.execute(request, body)
    }
}
```

В конструктор передаётся адаптер `(json: String, schema: Schema) -> Unit`: он возвращает `Unit` при успехе и бросает `AssertionError` при несоответствии.
Если валидатор возвращает нарушения, адаптер проверяет, что их список пуст.
Регистрация интерцептора и использование в доменном API показаны в [примере обвязки](test-client-sessions.md).

При переносе проверь три случая: корректное тело отправляется; невалидное блокируется до вызова транспорта; схема не переносится на следующий запрос без отметки.

## Проверка и декодирование ответа

Общий хелпер сначала проверяет схему, затем декодирует тело через конвертеры транспорта.
Повторное чтение сохранённого ответа не отправляет новый HTTP-запрос.

```kotlin
import com.networknt.schema.Schema
import org.springframework.test.web.servlet.client.RestTestClient
import org.springframework.test.web.servlet.client.expectBody

inline fun <reified T : Any> RestTestClient.ResponseSpec.getBodyMatchingSchema(
    schema: Schema,
): T {
    val result = expectBody().returnResult()
    val bytes = result.responseBody ?: throw AssertionError("Expected response body")
    val charset = result.responseHeaders.contentType?.charset ?: Charsets.UTF_8
    assertJsonMatchesSchema(bytes.toString(charset), schema)
    return expectBody<T>().returnResult().responseBody
        ?: throw AssertionError("Expected decoded response body")
}
```

`assertJsonMatchesSchema` подключи к проектному валидатору с тем же контрактом, что у адаптера интерцептора.

## Результат вызова и `toHttpOutcome`

`*ForOutcome` доменного API делегирует этому хелперу, передавая статус и схему успеха и разрешённые ошибки.
`HttpOutcome` сохраняет типизированное тело и фактический статус; `ExpectedHttpError` задаёт пару статуса и кода ошибки приложения.

```kotlin
import com.networknt.schema.Schema
import org.springframework.http.HttpStatusCode
import org.springframework.test.web.servlet.client.RestTestClient

sealed interface HttpOutcome<out S, out E> {
    val status: HttpStatusCode

    data class Success<S>(
        val body: S,
        override val status: HttpStatusCode,
    ) : HttpOutcome<S, Nothing>

    data class ExpectedError<E>(
        val body: E,
        override val status: HttpStatusCode,
    ) : HttpOutcome<Nothing, E>
}

data class ExpectedHttpError(val status: Int, val errorCode: String?)

inline fun <reified S : Any> RestTestClient.ResponseSpec.toHttpOutcome(
    successStatus: HttpStatusCode,
    successBodySchema: Schema,
    expectedErrors: Set<ExpectedHttpError>,
): HttpOutcome<S, ApiError> {
    val result = expectBody().returnResult()
    if (result.status == successStatus) {
        return HttpOutcome.Success(getBodyMatchingSchema<S>(successBodySchema), result.status)
    }

    val error = getBodyMatchingSchema<ApiError>(errorResponseSchema)
    error shouldHaveStatus result.status
    val actualError = ExpectedHttpError(result.status.value(), error.errorCode)
    if (actualError !in expectedErrors) {
        throw AssertionError("Unexpected error response: $actualError")
    }
    return HttpOutcome.ExpectedError(error, result.status)
}
```

`ApiError`, `errorResponseSchema` и `shouldHaveStatus` подключи к общему контракту ошибок приложения.
`shouldHaveStatus` — семантическая проверка согласованности статуса в теле ошибки с HTTP-статусом ответа.
Вместо прямого вызова маппера здесь используется общий `getBodyMatchingSchema`, декодирующий через настроенные конвертеры.
