---
keywords:
  - tests
---

# Минимальный и заполненный варианты объекта

Случайное заполнение необязательных полей затрудняет проверку поведения с их отсутствием.
Пара именованных фабрик даёт объект только с обязательными полями и объект с заполненными необязательными полями.

## Пара фабрик с разными дефолтами

Смысл варианта задаётся дефолтами; при необходимости отдельное поле всё равно можно переопределить.

### Пример 1. Карточка клиента

```kotlin
fun aMinimalCard(
    name: String = aName(),
    email: String? = null,
    address: String? = null,
) = ClientCard(name, email, address)

fun aFullCard(
    name: String = aName(),
    email: String? = anEmail(),
    address: String? = anAddress(),
) = aMinimalCard(name, email, address)
```

### Пример 2. Публикация с вложениями

```kotlin
fun aPostRq(
    title: String = aPostTitle(),
    image: FileContent? = null,
    file: FileContent? = null,
) = PostRq(title, image, file)

fun aFullPostRq(
    title: String = aPostTitle(),
    image: FileContent? = anImage(),
    file: FileContent? = anAttachment(),
) = PostRq(title, image, file)
```

## Границы применения

«Полный» означает заполнение предусмотренных этой фабрикой необязательных полей, а не создание всех мыслимых связей объекта.
Делегирование между фабриками и прямой вызов конструктора не меняют этого контракта.

[К каталогу](../test-patterns.md).
