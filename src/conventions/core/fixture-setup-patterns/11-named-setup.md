---
keywords:
  - tests
---

# Именованная подготовка ситуации

Часто повторяющаяся подготовка получает доменное имя.
Кейс передаёт существенные параметры и получает установленную фикстуру.

## Обёртка над фабрикой и инсталлером

Обёртка связывает построение и установку, не вводя ещё один обязательный класс.

### Пример 1. Все состояния подписки

```kotlin
fun MemberFixtureInstaller.setupAllStates(owner: Owner, now: Instant): List<MemberFixture> {
    val fixtures = MemberFixture.allStates(owner, now)
    return install(fixtures)
}
```

### Пример 2. Активные и ожидающие участники с оборудованием

```kotlin
fun MemberFixtureInstaller.setupMembersWithEquipment(
    owner: Owner, count: Int, now: Instant,
): List<MemberFixture> {
    val fixtures = MemberFixture.activeAndPendingWithEquipment(owner, count, now)
    return install(fixtures)
}
```

## Ранняя форма: процедурная подготовка

Ситуация создаётся несколькими последовательными вызовами.
При переработке такой подготовки выделяй описание фрагмента и инсталлер.

### Пример 1. Публикация с отправленным уведомлением

```kotlin
fun createPostWithSentNotification(request: PostRq): Post {
    val post = posts.create(request)
    notifications.save(aNotification(postId = post.id))
    notifications.markCompleted(post.id)
    return post
}
```

### Пример 2. Регистрация с извлечением токена

```kotlin
fun registerAndGetToken(request: RegisterRq): String {
    accounts.register(request)
    return emailSender.messagesTo(request.email).last().confirmationToken
}
```

## Границы применения

Многоресурсная последовательность относится к установщику, а не к TestApi.
При оформлении процедурной подготовки как фрагмента выделяй отдельный класс его описания.

[К каталогу](../test-patterns.md).
