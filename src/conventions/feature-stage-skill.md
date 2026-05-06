# Feature stage skill

Use this rule for skills that can write default stage outputs into a feature workdir.
A feature-stage skill may still be used without a feature directory when explicit paths, a non-feature default output container, or inline output are available.

## Skill bindings

Keep only these bindings in the skill or its local references:
- stage code;
- default feature-dir output path or output container;
- optional non-feature default output container;
- optional `progress.md` checklist item;
- optional stage `010` bootstrap allowance.
Keep task-specific logic, content rules, and validations in the skill.

## Shared lifecycle

- If the user gave an explicit output path or output directory, keep it.
- Otherwise resolve the active feature directory via `feature-workdir.md`.
- If the active feature directory is resolved and the skill defines a default feature-dir output path or output container, use that binding.
- If no active feature directory is resolved and the skill explicitly allows stage `010` bootstrap, it may create the feature directory before resolving the default stage output.
- If no active feature directory is resolved and the skill defines a non-feature default output container, use it.
- If no output path is resolved and the skill can return the result inline, return it inline instead of forcing feature-dir flow.
- Otherwise ask only for the missing feature directory or output path.

## Write and sync

- If an output path is resolved, write the artifact before any overview-file sync.
- If the skill binds a `progress.md` checklist item, the active feature directory is resolved, an output path is resolved, and `<feature-dir>/progress.md` exists, check that item when it is present, including when nested, and append exactly one Markdown link to the written artifact using the path relative to `progress.md` and the artifact file name as the link text.
- If no output path is resolved, do not update `progress.md`.
