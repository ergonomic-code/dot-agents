# Feature artifact lifecycle

Use this rule for skills that can write default artifact-phase outputs into a feature workdir.
A feature-aware skill may still be used without a feature directory when explicit paths, a non-feature default output container, or inline output are available.

## Skill bindings

Keep only these bindings in the skill or its local references:
- artifact phase code;
- default feature-dir output path or output container;
- optional non-feature default output container;
- optional `progress.md` checklist item;
- optional human-readable artifact title;
- optional artifact phase `010` bootstrap allowance.
Keep task-specific logic, content rules, and validations in the skill.
Use `feature-artifact-phases.md` for artifact phase semantics and standard phase meanings.

## Shared lifecycle

- If the user gave an explicit output path or output directory, keep it.
- Otherwise resolve the active feature directory and active implementation stage via `feature-workdir.md`.
- Treat an artifact as implementation-stage-scoped only when the user invokes the skill for an active stage, a selected progress stage, or one approved implementation slice.
- Use the implementation stage for titles and `progress.md` sync, not for default output directories.
- Do not treat artifact phase code `020` or `030` alone as an implementation-stage selector.
- Treat `010-feature-brief.md`, root `progress.md`, current status, target design, and shared artifacts as feature-wide.
- If an implementation-stage-scoped artifact would overwrite an existing root artifact for another stage, ask for an explicit output path instead of creating a stage directory.
- If the artifact is implementation-stage-scoped, the active feature directory is resolved, and no active implementation stage is resolved, ask for the stage.
- If the active feature directory is resolved and the skill defines a default feature-dir output path or output container, use that binding.
- If no active feature directory is resolved and the skill explicitly allows artifact phase `010` bootstrap, it may create the feature directory before resolving the default output path.
- If no active feature directory is resolved and the skill defines a non-feature default output container, use it.
- If no output path is resolved and the skill can return the result inline, return it inline instead of forcing feature-dir flow.
- Otherwise ask only for the missing feature directory, implementation stage, or output path.

## Human-readable document title

- Use this only when the skill defines a human-readable artifact title and needs a document title for a rendered artifact.
- If `<active-feature-dir>/010-feature-brief.md` exists, read its first level-1 heading and use its text as `<feature-title>`.
- If the artifact is implementation-stage-scoped, derive the active stage label as `Этап <feature-code>/<stage-code>: <stage-name>` from root `progress.md`.
- If `<feature-title>` and the active stage label are both available, use `<feature-title> — <active-stage-label> — <artifact-title>`.
- Otherwise, if only `<feature-title>` is available, use `<feature-title> — <artifact-title>`.
- Otherwise use `<artifact-title>`.

## Write and sync

- If an output path is resolved, write the artifact before any overview-file sync.
- If the skill binds a `progress.md` checklist item, the active feature directory is resolved, an output path is resolved, and `<feature-dir>/progress.md` exists, check the matching flat item when it is present.
- If no matching flat item exists, propose the flat item to add and get user approval before creating it.
- When checking that item, append exactly one Markdown link to the written artifact unless the item already links it.
- Use the path relative to `progress.md` and the artifact file name as the link text.
- If no output path is resolved, do not update `progress.md`.
