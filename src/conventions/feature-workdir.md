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

- Treat `index.md` and `progress.md` in the feature directory root as the standard feature-directory overview files.
- Use `index.md` for a short directory index with relative links to feature artifacts.
- Use `progress.md` for the current feature-stage checklist and work status.
- If the active feature directory is resolved and `<feature-dir>/index.md` exists, read it before substantial work.
- If a skill creates default artifacts in the active feature directory and `<feature-dir>/index.md` exists, update `index.md` in the same step with concise relative links to the new files or directories.
- If the skill defines a more specific indexing rule, follow that rule for row granularity and wording.
- Unless the user gave another path, create new task files in the active feature directory.
- If a skill has a default `./tmp` output directory, treat it as `<active-feature-dir>/tmp` when the active feature directory is resolved.

## Feature stage codes

- Use the file name prefix as the feature stage code inside the feature workdir.
- `010` means requirements preparation.
- `020` means mapping requirements to production code, analyzing the current implementation, and listing current test cases.
- `030` means optional preliminary-refactoring review and follow-up fixes produced from that analysis.
- `040` means test-case refresh.
- `050` means implementation design.
- `060` means test-case implementation.
- If a skill defines a default file name in the feature workdir, prefix it with the matching stage code unless the user gave an explicit path.
- If more than one stage is plausible, use the earliest stage that still matches the artifact purpose.
