---
keywords:
  - tests
---

# Паттерны реализации тестов

Паттерны описывают способы реализации инфраструктуры подготовки фикстур и организации кейсов.
Выбирай подходящий вариант по ответственности компонента и задаче подготовки.
Примеры сокращены: импорты и несущественные определения опущены; проектные хелперы не являются API библиотек.
Не вводи дополнительные классы только для воспроизведения формы примера.

## Инфраструктура подготовки фикстур

- [Фабрика с переопределяемыми дефолтами](fixture-setup-patterns/01-overridable-defaults.md).
- [Доменный генератор поверх универсального](fixture-setup-patterns/02-domain-generators.md).
- [Минимальный и заполненный варианты объекта](fixture-setup-patterns/03-minimal-and-full.md).
- [Коллекция через фабрику одного элемента](fixture-setup-patterns/04-collections.md).
- [Воспроизводимые случайные данные и время](fixture-setup-patterns/05-repeatable-generation.md).
- [Связанный граф до установки](fixture-setup-patterns/06-in-memory-graph.md).
- [Именованные варианты фрагмента](fixture-setup-patterns/07-named-fragments.md).
- [Согласованные входные и ожидаемые данные](fixture-setup-patterns/08-inputs-and-expectations.md).
- [Отдельные фрагмент и инсталлер](fixture-setup-patterns/09-fixture-and-installer.md).
- [Возврат фактически установленного состояния](fixture-setup-patterns/10-installed-values.md).
- [Именованная подготовка ситуации](fixture-setup-patterns/11-named-setup.md).
- [TestApi одного ресурса](fixture-setup-patterns/12-resource-test-api.md).
- [Точечная установка служебного состояния через SQL](fixture-setup-patterns/13-targeted-sql.md).
- [Доменная оболочка над HTTP-дублёром](fixture-setup-patterns/15-http-double.md).
- [Согласованная установка локального и внешнего состояния](fixture-setup-patterns/16-local-and-external-state.md).
- [Восстановление общего фона перед кейсом](fixture-setup-patterns/17-restore-background.md).
- [Разные сроки жизни окружения и данных](fixture-setup-patterns/18-separate-lifetimes.md).
- [Составной базовый слой](fixture-setup-patterns/19-composable-base.md) — WIP.
- [Подготовленное начальное состояние БД](fixture-setup-patterns/20-database-baseline.md).
- [Готовая зависимость с резервным запуском контейнера](fixture-setup-patterns/21-provided-dependency.md).
- [Специальный SUT через действующий Spring-контекст](fixture-setup-patterns/22-spring-managed-sut.md).

## Кодирование кейсов

- [Прямая композиция подготовки в кейсе](test-case-patterns/14-direct-composition.md).
