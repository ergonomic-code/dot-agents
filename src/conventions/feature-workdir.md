# Feature workdir

Use this rule when the task may create files or depends on feature-local context.

## Resolve active feature directory

- If the user gave an explicit output path, feature directory, or a file path inside a feature directory, use that feature directory.
- Otherwise, if the current working directory is `devlog/<feature-id>-<feature-slug>` and `<feature-id>` is exactly three digits, use it.
- Otherwise, inspect the current user request for a standalone three-digit feature id matching `(?<!\d)\d{3}(?!\d)`.
- Ignore four-digit numbers.
- If the request contains `xxx`, search recursively under repository-root `./devlog` for directories whose basename starts with `<feature-id>-` or equals `<feature-id>`.
- Otherwise, match that id only against direct subdirectories of repository-root `./devlog` whose basename starts with `<feature-id>-` or equals `<feature-id>`.
- If exactly one directory matches, auto-bind to it.
- If none or more than one directory matches, do not guess.

## Create feature directory for stage 010

- Use this rule only when a skill is creating its default stage `010` artifact and no active feature directory was resolved.
- If the user already gave an explicit output path or feature directory, do not create another feature directory.
- Require a three-digit feature id and a feature slug.
- If either is missing, ask only for the missing part and stop.
- Create `./devlog/<feature-id>-<feature-slug>` and use it as the active feature directory.
- If the creating skill defines default bootstrap files for a new feature directory, create them in the same step.

## Use active feature directory

- Treat `progress.md` in the feature directory root as the standard feature-directory overview file.
- Use `progress.md` for the current feature-stage checklist and work status.
- Skills that write default stage outputs use `feature-stage-skill.md` for write and overview-file sync.
- Unless the user gave another path, create new task files in the active feature directory.
- If a skill has a default `./tmp` output directory, treat it as `<active-feature-dir>/tmp` when the active feature directory is resolved.
- In `progress.md`, group implementation cases under `Реализация` by `SUT: <название>`.
- Under each SUT item, list cases; under each case, use `Красный тест` for the red step and `Зелёный тест` for the green step.
- When all child items under a case or SUT are done, mark that parent item done too.

## Feature stage codes

- Use the file name prefix as the feature stage code inside the feature workdir.
- `010` means requirements preparation.
- Standard `010` artifacts are `010-feature-brief.md` and other `010-*` requirement files.
- `020` means current code analysis.
- Standard `020` artifacts are `020-api-current.md`, `020-test-cases-current.md`, `020-sut-acceptance-criteria-current.adoc`, `020-model-current.md`, `020-persistence-current.md`, and `020-schema.md`.
- `030` means implementation design.
- Standard `030` artifacts are `030-api-new.adoc`, `030-test-cases-new.adoc`, `030-model-new.md`, `030-persistence-new.md`, and `030-schema.md`.
- If a skill defines a default file name in the feature workdir, prefix it with the matching stage code unless the user gave an explicit path.
- If more than one stage is plausible, use the earliest stage that still matches the artifact purpose.
