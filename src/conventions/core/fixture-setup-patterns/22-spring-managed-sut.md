---
keywords:
  - tests
---

# Специальный SUT через действующий Spring-контекст

Для отдельного сценария нужен экземпляр SUT с особой зависимостью, но с контейнерной обработкой Spring.
Хелпер регистрирует bean definition с фабрикой экземпляра и получает SUT обратно из контекста.

## Временный bean definition с supplier

Хелпер сохраняет имена зарегистрированных бинов и освобождает их после кейса.

```kotlin
class DynamicBeans(context: ConfigurableApplicationContext) : AutoCloseable {
    private val factory = context.beanFactory as DefaultListableBeanFactory
    private val names = mutableListOf<String>()

    fun <T : Any> register(name: String, type: Class<T>, supplier: () -> T): T {
        check(!factory.containsBean(name))
        factory.registerBeanDefinition(name, GenericBeanDefinition().apply {
            setBeanClass(type)
            setInstanceSupplier(supplier)
        })
        names += name
        return factory.getBean(name, type)
    }

    inline fun <reified T : Any> register(name: String, noinline supplier: () -> T): T =
        register(name, T::class.java, supplier)

    override fun close() {
        names.asReversed().forEach { name ->
            factory.destroySingleton(name)
            factory.removeBeanDefinition(name)
        }
        names.clear()
    }
}
```

Пример рассчитан на последовательный жизненный цикл; при конкурентной регистрации операции хелпера нужно синхронизировать.

### Пример 1. Подмена отправителя на блокирующий дублёр

```kotlin
val sut = dynamicBeans.register("resenderUnderTest") {
    OutboxResender(
        publisher = context,
        sender = blockingSender,
        outbox = context.getBean<OutboxDao>(),
    )
}
// register вызывает getBean после регистрации definition:
// тест получает экземпляр, обработанный контейнером.
```

### Пример 2. Тот же механизм с ошибкой отправки

```kotlin
val sut = dynamicBeans.register("failingResenderUnderTest") {
    OutboxResender(
        publisher = context,
        sender = failingSender,
        outbox = context.getBean<OutboxDao>(),
    )
}

@AfterEach
fun releaseDynamicBeans() { dynamicBeans.close() }
```

## Границы применения

Регистрация включает supplier, затем getBean; простой вызов конструктора вне контекста не равноценен этому пути.
Хелпер должен запрещать случайное перекрытие существующего бина и удалять временные определения вместе с экземплярами.
Эта техника относится к подготовке SUT; она не требует пересоздания всего контекста для каждого кейса.

[К каталогу](../test-patterns.md).
