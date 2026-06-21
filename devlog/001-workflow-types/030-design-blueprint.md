# Принципиальное решение

## Контекст

Фреймворк сейчас использует feature-flow как фактический базовый workflow.
Это видно в `feature-workdir.md`, `feature-stage-skill.md`, `feature-artifact-phases.md`, `progress-template.md` и feature-oriented runtime skills.
Текущая структура уже содержит общий каркас работы: прояснить целевое состояние, понять текущее устройство, выбрать принципиальное направление, подготовиться при необходимости и выполнить работу.
Но этот каркас выражен через feature terminology и поэтому плохо описывает задачи, которые не являются пользовательской фичей.
Целевое состояние требует явного универсального `Task` flow и набора специализированных work flows поверх него.
Рефакторинг должен быть доступен и как самостоятельный поток, и как предварительная фаза feature-flow.
Bug fix не становится отдельным top-level flow.
Он остаётся специализированным случаем feature-flow с defect input, reproducer/reproduction/localization в current-state phase и обычно уже выбранным red case.
Для bug fix current-state phase может включать limited preliminary refactoring, если текущая структура мешает написать репродьюсер эргономично.
Нетиповые задачи используют универсальный `Task` flow, пока evidence, output и change boundary не докажут необходимость специализации.

Ключевой driver решения: сделать workflow terminology нейтральной к feature, а feature оставить только одной специализацией.
Второй driver: не плодить параллельные правила для одних и тех же фаз.
Третий driver: сохранить существующую flat progress mechanics, artifact phases и stage mechanics, но переназвать их вокруг task/workflow model.

## Выбранный подход

Выбран полный переход к task/workflow-neutral API.
Нужно переименовать `feature-*` framework surface в нейтральные `task-*` или `workflow-*` правила и затем выразить feature, refactor и bug-fix поведение как специализации.
Это больше change set, чем минимальная правка, но он убирает главный архитектурный перекос: feature перестаёт быть неявным базовым workflow.

### Базовая модель

Ввести общий workflow model:
- `Task flow` задаёт обязательные фазы: target state, current state, solution direction, execution.
- `Task flow` допускает optional preparation phase между solution direction и execution.
- `Specialized flow` расширяет `Task flow` только когда тип работы уже понятен.
- `Feature flow` уточняет preparation как preliminary refactoring и execution как TDD implementation.
- `Refactor flow` описывает самостоятельный structural-change workflow без behavior changes.
- `Bug fix` остаётся specialization внутри feature-flow, а не отдельным top-level flow.

Specialized flow может уточнять допустимые activities внутри базовых фаз, не создавая новую top-level phase.
Для bug fix это означает, что current-state phase содержит writing reproducer, reproduction и localization.
Та же фаза может содержать узкий refactor-for-reproducer, если без него репродьюсер нельзя написать эргономично.

Базовая модель должна быть одним источником правды для phase order и смысла фаз.
Directory resolution, artifact lifecycle, progress sync и stage mechanics должны ссылаться на неё, а не повторять workflow semantics локально.

### Переименование framework API

Переименовать runtime conventions и references так, чтобы их имена не закрепляли feature как базовый сценарий:
- `feature-workdir.md` -> task/workflow workdir convention.
- `feature-stage-skill.md` -> task/workflow artifact lifecycle convention.
- `feature-artifact-phases.md` -> task/workflow artifact phases convention.
- `progress-template.md` -> task/workflow progress template или template с явно универсальным базовым блоком и feature specialization block.

Skills должны загружать новые нейтральные convention paths.
Backward-compatible wrapper для старых `feature-*` convention filenames не нужен.
Переход внутри framework payload выполняется как breaking rename.
Нельзя оставлять два равноправных источника правды с разной терминологией.

### Progress model

`progress.md` остаётся flat checklist with level-2 workflow phases.
Универсальная задача использует базовые фазы:
- `Прояснение целевого состояния`;
- `Понимание текущего состояния`;
- `Выбор принципиального направления решения`;
- `Подготовка`, если нужна;
- `Выполнение`.

Feature-flow специализирует:
- `Подготовка` как `Предварительный рефакторинг`;
- `Выполнение` как `Реализация`.

Refactor-flow остаётся специализацией `Task flow` и переиспользует базовые фазы.
Refactor-specific rules уточняют activities, progress wording и verification внутри этих фаз, но не создают отдельную top-level phase model.
Structural work не маскируется под feature implementation.
Если refactor является prerequisite для feature behavior, он остаётся в feature-flow под `Предварительный рефакторинг`.
Bug-fix specialization не ждёт отдельной фазы `Предварительный рефакторинг`, чтобы написать репродьюсер.
Если для репродьюсера нужен structural cleanup, он оформляется как limited current-state activity и не подменяет полноценную preliminary refactoring phase.

### Artifact model

Artifact phase codes остаются независимыми от implementation stages.
Но их description должен быть task-neutral:
- `010` means target-state and requirement preparation.
- `020` means current-state analysis.
- `030` means solution direction and implementation design.

Feature-specific artifact names вроде `010-feature-brief.md` можно сохранить только как specialization output.
Для универсальных задач нужен task-neutral equivalent.
Universal task requirement artifact называется `010-task-brief.md`.
Это имя должно использоваться consistently by init/bootstrap skills and artifact lifecycle rules.

### Skill impact

Feature-specific skills remain feature-specific when their job is truly feature/TDD work.
Examples: `choose-next-tdd-increment`, `design-feature-test-cases`, `fix-red-case`.
Shared artifact-writing skills should depend on task-neutral lifecycle rules rather than feature-only lifecycle rules.
Context-fix and framework-fix skills should route ambiguous work to universal `Task flow` before selecting feature/refactor implementation mechanics.

The implementation should avoid broad behavioral changes to skills in the same slice as path renames.
First make naming and loading order coherent.
Then specialize skill behavior where current text still says feature when it means any task.

## Этапы

Реализация должна идти инкрементально.
После каждого этапа framework должен оставаться рабочим и применимым к новым задачам.
Нельзя делать промежуточное состояние, в котором старый feature-flow уже сломан, а новый task/workflow-neutral flow ещё не подключён.

1. Add standalone refactor flow.
   Этап добавляет самостоятельный structural-change workflow без behavior changes.
   Feature-flow продолжает работать по старым правилам.
2. Clean feature-flow preliminary refactoring through refactor flow.
   Этап убирает локальные дублирующие правила предварительного рефакторинга из feature-flow и ссылает его на refactor mechanics.
   Feature-flow всё ещё остаётся самостоятельным рабочим workflow.
3. Add base `Task flow` without breaking existing paths.
   Этап вводит общий conceptual source of truth для target state, current state, solution direction, optional preparation и execution.
   Существующие `feature-*` conventions и новый refactor-flow остаются рабочими напрямую.
4. Make feature-flow specialize `Task flow`.
   Этап привязывает feature-flow к базовым фазам.
   Preparation специализируется как preliminary refactoring, execution как TDD implementation.
5. Make refactor-flow specialize `Task flow`.
   Этап привязывает refactor-flow к тем же базовым фазам.
   Execution уточняется как structural change without behavior change.
6. Rename shared `feature-*` framework API to task/workflow-neutral paths and update references.
   Этап выполняется только после того, как feature-flow и refactor-flow уже выражены через `Task flow`.
   Rename становится mechanical cleanup, а не одновременной semantic migration.
7. Validate by searching old feature-as-base terminology and checking representative runtime skill loading paths.
   Этап проверяет, что старые имена не остались владельцами общей mechanics.
   Feature-specific terminology допускается только там, где речь действительно о feature-flow.

## Приложение: отброшенные варианты

### Минимальный вариант

Суть: переименовать только отдельные фразы и добавить несколько правил про universal task flow без изменения framework API.
Плюс: меньше риск и меньше файлов в diff.
Минус: `feature-*` слой остался бы фактическим центром workflow, а universal task flow был бы добавкой поверх старой модели.
Причина отказа: этот вариант не устраняет архитектурный перекос из brief.

### Системный вариант без полного rename

Суть: ввести общий `Task flow` source of truth, но оставить `feature-workdir.md` и related filenames как владельцев mechanics.
Плюс: хороший баланс между SSOT и малым churn.
Минус: имена framework API продолжили бы говорить, что базовая mechanics принадлежит feature-flow.
Причина отказа: пользователь выбрал полный переход к task/workflow-neutral API.
