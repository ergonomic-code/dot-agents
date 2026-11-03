---
keywords:
  - tests
---

# TestApi одного ресурса

TestApi скрывает устройство подготовки и наблюдения одного ресурса.
Кейс и инсталлер работают с его API, не зная, как ресурс хранит состояние.

## Подготовка и наблюдение в одном API

Разделение на SetupApi и VerificationApi не требуется.
Один TestApi может изменять состояние, читать его и проверять.

### Пример 1. Управление участниками

```kotlin
class MembersTestApi(private val members: MembersRepo) {
    fun save(member: Member) { members.save(member) }

    fun setRoles(id: Int, roles: Set<Role>) {
        val member = members.findById(id) ?: error("Участник не найден")
        members.save(member.copy(roles = roles))
    }
}
```

### Пример 2. Создание и чтение публикации

```kotlin
class PostsTestApi(private val posts: PostsRepo) {
    fun create(request: PostRq): Post = posts.create(Post.of(request))
    fun get(id: UUID): PostView? = posts.get(PostRef.to(id))
    fun verifyTitle(id: UUID, expected: String) {
        get(id)?.title shouldBe expected
    }
}
```

## Границы применения

TestApi, объединяющий несколько ресурсов, нарушает границу ответственности.
Его нельзя предъявлять как равноправный вариант этого паттерна.
Оркестрация нескольких TestApi относится к установщику.
Граница определяется ресурсом, а не общим префиксом классов или удобством внедрения зависимостей.

[К каталогу](../test-patterns.md).
