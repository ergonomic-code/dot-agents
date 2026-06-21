# Технические якоря к [010-feature-brief.md](./010-feature-brief.md)

## Базовый workflow-каркас

- `target` [feature-workdir.md](../../src/conventions/feature-workdir.md:44) - runtime-правило задаёт общий каркас `progress.md` через level-2 workflow phases.
- `target` [feature-workdir.md](../../src/conventions/feature-workdir.md:45) - базовая последовательность уже зафиксирована как `Прояснение требований` -> `Понимание текущего устройства реализации` -> `Выбор принципиального направления решения` -> `Предварительный рефакторинг` -> `Реализация`; это главный кодовый якорь для обсуждения универсального потока и его специализаций.
- `target` [progress-template.md](../../src/references/progress-template.md:12) - шаблон `progress.md` материализует первые три обязательные фазы как отдельные разделы и тем самым подтверждает текущий базовый workflow в installable payload.
- `related` [progress-template.md](../../src/references/progress-template.md:27) - тот же шаблон уже держит `Предварительный рефакторинг` и `Реализация` как отдельные поздние фазы, что важно для выделения refactor-work и feature-implementation поверх общего каркаса.

## Feature-flow специализация

- `target` [feature-workdir.md](../../src/conventions/feature-workdir.md:46) - feature-flow закрепляет, что подготовительный рефакторинг ведётся под фазой `Предварительный рефакторинг`.
- `target` [feature-workdir.md](../../src/conventions/feature-workdir.md:47) - feature-flow закрепляет, что TDD-инкременты ведутся под фазой `Реализация`.
- `target` [feature-workdir.md](../../src/conventions/feature-workdir.md:51) - refactor-часть feature-flow имеет отдельную форму записи `Рефакторинг: <краткий инкремент>`.
- `target` [feature-workdir.md](../../src/conventions/feature-workdir.md:52) - implementation-часть feature-flow имеет отдельную форму записи как тестируемое поведение.
- `related` [choose-next-tdd-increment/SKILL.md](../../src/skills/choose-next-tdd-increment/SKILL.md:17) - skill выбора следующего инкремента требует рядом с brief ещё и `code anchors`, `principle-level solution`, branch changes и `progress`, то есть работает уже внутри специализированного feature/TDD-потока, а не универсальной задачи вообще.
- `related` [choose-next-tdd-increment/SKILL.md](../../src/skills/choose-next-tdd-increment/SKILL.md:54) - выбранный инкремент вставляется именно в `## Реализация`, что подтверждает привязку skill к feature-специализации.
- `related` [design-test-case/SKILL.md](../../src/skills/design-test-case/SKILL.md:48) - проектирование тест-кейса после записи артефакта обновляет `progress.md` под `## Реализация` или stage heading; это ещё один runtime-якорь feature-flow как специализированного сценария.

## Отдельный refactor-flow

- `target` [task-boundaries.md](../../src/conventions/task-boundaries.md:9) - framework различает structural refactoring и behavior change как разные coding slices.
- `target` [task-boundaries.md](../../src/conventions/task-boundaries.md:15) - крупный preparatory refactoring должен выполняться отдельным refactor-only slice до зависимых behavior slices; это прямой якорь для критерия про самостоятельный refactor-flow и его встраивание перед feature-реализацией.
- `related` [refactor-case/SKILL.md](../../src/skills/refactor-case/SKILL.md:18) - отдельный skill `refactor-case` оформляет рефакторинг как самостоятельный режим работы после green-case.
- `related` [refactor-case/SKILL.md](../../src/skills/refactor-case/SKILL.md:24) - внутри skill итерация явно классифицируется как ровно один `refactor mode`, что подтверждает отдельный тип потока, а не просто шаг внутри общего coding-сценария.
- `related` [refactor-case/SKILL.md](../../src/skills/refactor-case/SKILL.md:47) - ограничения skill запрещают смешивать production и test refactor в одной итерации и удерживают рефакторинг как самостоятельную рамку.
