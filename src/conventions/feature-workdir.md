# Feature workdir

Use this rule when the task may create files or depends on feature-local context.

## Resolve active feature directory

- If the user gave an explicit output path, feature directory, or a file path inside a feature directory, use that feature directory.
- Otherwise, if the current working directory is `devlog/<feature-id>-<feature-slug>` or any descendant of it, and `<feature-id>` is exactly three digits, use that feature directory ancestor.
- Otherwise, inspect the current user request for a standalone three-digit feature id matching `(?<!\d)\d{3}(?!\d)`.
- Ignore four-digit numbers.
- If the request contains `xxx`, search recursively under repository-root `./devlog` for directories whose basename starts with `<feature-id>-` or equals `<feature-id>`.
- Otherwise, match that id only against direct subdirectories of repository-root `./devlog` whose basename starts with `<feature-id>-` or equals `<feature-id>`.
- If exactly one directory matches, auto-bind to it.
- If none or more than one directory matches, do not guess.

## Create feature directory for artifact phase 010

- Use this rule only when a skill is creating its default artifact-phase `010` artifact and no active feature directory was resolved.
- If the user already gave an explicit output path or feature directory, do not create another feature directory.
- Require a three-digit feature id and a feature slug.
- If either is missing, ask only for the missing part and stop.
- Create `./devlog/<feature-id>-<feature-slug>` and use it as the active feature directory.
- If the creating skill defines default bootstrap files for a new feature directory, create them in the same step.

## Resolve active implementation stage

- Use implementation stages only when root `progress.md` has stage headings or the user names a stage explicitly.
- Otherwise, if the current user request names a standalone `stage-<stage-code>`, `этап <stage-code>`, or `<feature-code>/<stage-code>` while the active feature directory is known, use that active implementation stage.
- Otherwise, if a selected root `progress.md` section is or is under `### Этап <feature-code>/<stage-code>: <название>`, use that stage.
- Otherwise leave the active implementation stage unresolved.

## Use active feature directory

- Treat `progress.md` in the feature directory root as the standard feature-directory overview file.
- Use `progress.md` for the current feature checklist and work status.
- Standard root artifacts are `010-feature-brief.md` and `progress.md`.
- Keep feature artifacts in the feature directory root unless the user gave an explicit output path.
- Use `feature-artifact-phases.md` for artifact-phase-coded file names such as `010-*`, `020-*`, and `030-*`.
- Keep the feature directory flat.
- Skills that write default artifact-phase outputs use `feature-stage-skill.md` for write and overview-file sync.
- Unless the user gave another path, create task files in the active feature directory root.
- If a task is implementation-stage-specific and no active stage can be resolved, ask for the stage.
- If a skill has a default `./tmp` output directory, treat it as `<active-feature-dir>/tmp` when the active feature directory is resolved.
- In `progress.md`, use level-2 headings for workflow phases and level-3 headings for implementation stages or phase-local subdivisions.
- Use this level-2 workflow order: `Прояснение требований`, `Понимание текущего устройства реализации`, `Выбор принципиального направления решения`, `Предварительный рефакторинг`, `Реализация`.
- Track refactor-only preparation under `Предварительный рефакторинг`.
- Track TDD increments under `Реализация`.
- Keep todo lists short.
- Do not nest checklist items to model phases, stages, or features.
- Use nested checklist items only for the temporary TDD child items below one tested-behavior parent.
- In `Предварительный рефакторинг`, write refactor work as flat items named `Рефакторинг: <краткий инкремент>`.
- In `Реализация`, add each TDD increment as one parent item named by the tested behavior.
- When adding a TDD increment, add child items `красный кейс` and `зелёный кейс`.
- After coding the red case, mark only `красный кейс` done.
- After the case is green, remove both child items and mark the parent behavior item done.

## Implementation stages

- Use implementation stages only when one feature needs several implementation slices.
- Use `<feature-code>` as the three-digit feature id from the feature directory.
- Use `<stage-code>` as an exactly two-digit implementation-stage code.
- Use `<feature-code>/<stage-code>` as the canonical feature-stage identifier, for example `014/01`.
- Use `### Этап <feature-code>/<stage-code>: <название>` in root `progress.md`.
- Use the canonical feature-stage identifier in user-facing status updates about a specific implementation stage.
- Keep implementation-stage breakdown out of root `010-feature-brief.md`.
- Each behavior stage changes no more than one externally visible endpoint or API surface.
- Put large preparatory refactoring into its own refactor-only stage before dependent behavior stages.
- Stage names state the boundary or outcome, not the internal implementation plan.

## Add implementation stages

- Use this workflow when asked to split feature implementation into stages or when the user explicitly approves a proposal to add stages because the feature scope contains several implementation slices.
- Derive stages only from explicit user intent, feature artifacts, and existing progress.
- Add one `### Этап <feature-code>/<stage-code>: <название>` heading per endpoint/API-surface behavior slice and one per large preparatory refactor.
- Keep artifacts in root unless the user gives explicit paths.
- If one root artifact would ambiguously mix several stages, ask for an explicit artifact path or split the content by headings inside the artifact.
- Do not edit product code while changing progress layout.
