---
keywords:
  - tests
---

# Доменная оболочка над HTTP-дублёром

Кейсу нужно определить поведение внешней зависимости на языке домена.
Хелпер переводит доменные параметры в сопоставление HTTP-запроса и нужный ответ.

## Именованная функция настройки

Одна функция полностью задаёт нужное взаимодействие.

### Пример 1. Поиск внешнего аккаунта

```kotlin
fun WireMock.stubAccountLookup(number: String, accountId: String) {
    register(get(urlPathEqualTo("/accounts/lookup"))
        .withQueryParam("number", equalTo(number))
        .willReturn(okJson("""{"id":"$accountId"}""")))
}
```

### Пример 2. Привязка внешнего устройства

```kotlin
fun WireMock.stubDeviceBinding(accountId: String, serial: String, deviceId: String) {
    register(post(urlPathEqualTo("/devices"))
        .withRequestBody(equalToJson("""{"account":"$accountId","serial":"$serial"}"""))
        .willReturn(okJson("""{"id":"$deviceId"}""")))
}
```

## Объект запроса с вариантами ответа

Сначала задаётся ожидаемый запрос, затем выбирается успешный, ошибочный или задержанный ответ.

### Пример 1. Чтение календарей

```kotlin
inner class OnGetCalendars(private val token: String) {
    private fun request() = get(urlEqualTo("/calendar/list"))
        .withHeader("Authorization", equalTo("Bearer $token"))

    fun returnsCalendars(calendars: List<Calendar>) {
        server.stubFor(request().willReturn(okJson(toJson(calendars))))
    }
    fun returnsForbidden() { server.stubFor(request().willReturn(forbidden())) }
}
```

### Пример 2. Отправка уведомления

```kotlin
inner class OnSend(private val notification: Notification) {
    private fun request() = post(urlEqualTo("/messages"))
        .withRequestBody(equalToJson(toJson(notification)))

    fun returnsCreated(id: String) {
        server.stubFor(request().willReturn(created().withBody("""{"id":"$id"}""")))
    }
    fun returnsError() { server.stubFor(request().willReturn(serverError())) }
}
```

## Границы применения

Настройка ответа не доказывает, что SUT выполнил ожидаемый запрос.
Чтение журнала обращений или проверка остаются отдельными методами того же хелпера; деление на SetupApi и VerificationApi не требуется.

[К каталогу](../test-patterns.md).
