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

- Use implementation stages only for a staged feature directory.
- If the user gave a path inside `stage-<stage-code>`, a stage directory, or a file path inside a stage directory, use that active implementation stage.
- Otherwise, if the current working directory is `stage-<stage-code>` or any descendant of it inside the active feature directory, use that stage ancestor.
- Otherwise, if the current user request names a standalone `stage-<stage-code>`, `этап <stage-code>`, or `<feature-code>/<stage-code>` while the active feature directory is known, use that active implementation stage.
- Otherwise, if a selected root `progress.md` entry is nested under `Этап <feature-code>/<stage-code>:`, use that stage.
- Otherwise leave the active implementation stage unresolved.

## Use active feature directory

- Treat `progress.md` in the feature directory root as the standard feature-directory overview file.
- Use `progress.md` for the current feature checklist and work status.
- Keep feature-wide artifacts in the feature directory root.
- Standard root artifacts are `010-feature-brief.md` and `progress.md`.
- Root may also contain current status, target design, or shared artifacts not bound to one implementation stage.
- Use `feature-artifact-phases.md` for artifact-phase-coded file names such as `010-*`, `020-*`, and `030-*`.
- By default, keep the feature directory flat.
- Create `stage-<stage-code>/` directories only when the user explicitly asked for staged layout during initialization, explicitly asked to split the feature, or explicitly approved adding stages after a proposal grounded in the feature brief.
- For staged implementation, use `stage-<stage-code>/` directories, where `<stage-code>` is an exactly two-digit implementation-stage code.
- Each `stage-<stage-code>/` contains artifacts for exactly that implementation slice.
- Skills that write default artifact-phase outputs use `feature-stage-skill.md` for write and overview-file sync.
- Unless the user gave another path, create feature-wide task files in the active feature directory root.
- Unless the user gave another path, create implementation-stage task files in the active `stage-<stage-code>/`.
- If a task is implementation-stage-specific and no active stage can be resolved, ask for the stage or first convert the feature directory to staged layout.
- If a skill has a default `./tmp` output directory, treat it as `<active-feature-dir>/tmp` when the active feature directory is resolved.
- In flat `progress.md`, group implementation cases under `Реализация` by `SUT: <название>`.
- In staged `progress.md`, group implementation cases under `Реализация` by `Этап <feature-code>/<stage-code>: <название>`, then by `SUT: <название>`.
- Under each SUT item, list cases; under each case, use `Красный тест` for the red step and `Зелёный тест` for the green step.
- When all child items under a case, SUT, or stage are done, mark that parent item done too.

## Implementation stages

- Use implementation stages only when one feature needs several implementation slices.
- Use `<feature-code>` as the three-digit feature id from the feature directory.
- Use `<stage-code>` as an exactly two-digit implementation-stage code.
- Use `<feature-code>/<stage-code>` as the canonical feature-stage identifier, for example `014/01`.
- Use the canonical feature-stage identifier in `Этапы реализации`, staged `progress.md`, and user-facing status updates about a specific implementation stage.
- Add `Этапы реализации` to root `010-feature-brief.md` only when the user explicitly asked for staged layout or explicitly approved adding stages.
- Each behavior stage changes no more than one externally visible endpoint or API surface.
- Put large preparatory refactoring into its own refactor-only stage before dependent behavior stages.
- Keep cross-stage status and target design in root, not in stage directories.
- Stage names state the boundary or outcome, not the internal implementation plan.

## Convert flat feature directory to staged

- Use this workflow when asked to split a feature directory into stages or when the user explicitly approves a proposal to add stages because the feature scope contains several implementation slices.
- Preserve root `010-feature-brief.md`, `progress.md`, and feature-wide shared artifacts in root.
- Derive stages only from explicit user intent, feature artifacts, and existing progress.
- Create one `stage-<stage-code>/` per endpoint/API-surface behavior slice and one per large preparatory refactor.
- Move only stage-local artifacts to the matching `stage-<stage-code>/`; leave shared artifacts in root.
- Update root `010-feature-brief.md` with `Этапы реализации` and root `progress.md` with stage groups and links.
- If an artifact can belong to several stages, keep it in root or ask.
- Do not edit product code during layout conversion.
