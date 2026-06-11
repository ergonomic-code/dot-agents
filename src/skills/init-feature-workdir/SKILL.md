---
name: init-feature-workdir
description: Create a new feature workdir under `devlog/NNN-slug` with `010-feature-brief.md` and `progress.md` from local templates. Use when the user asks to create, initialize, or bootstrap a feature directory, feature workdir, or devlog entry and provides, or must be asked for, a three-digit feature id and slug.
---

# Init Feature Workdir

Read `framework_checkout_root/src/conventions/feature-workdir.md`.
Read `./references/feature-brief-template.md` and `./references/progress-template.md`.

## Workflow

- Resolve only an explicit user argument in form `NNN-slug`, `NNN slug`, or `devlog/NNN-slug`.
- Require `<feature-id>` as exactly three digits and `<feature-slug>` as one user-provided path segment.
- Do not derive the slug from a title or requirements text.
- If id or slug is missing, ask only for the missing part and stop.
- If the slug contains a path separator or escapes `./devlog`, ask for a corrected slug and stop.
- Use target directory `./devlog/<feature-id>-<feature-slug>`.
- If the target directory already exists, stop and report that no files were changed.
- Create only the target directory, `010-feature-brief.md`, `progress.md`, and, when staged layout is explicit, the required `stage-<stage-code>/` directories.
- Copy the fenced file templates from the local references.
- Create a flat feature directory by default.
- If the user explicitly requests staged layout or lists implementation slices, adapt the copied `010-feature-brief.md` and `progress.md` to the staged layout from `feature-workdir.md`, using stage directories `stage-<stage-code>` and feature-stage identifiers `<feature-code>/<stage-code>`.
- Keep placeholders unless the user explicitly provided exact values.
- Do not inspect product code, infer requirements, or create extra files.
- Verify that the directory and both files exist.

## Output

Report the created directory and files.
If stopped, report the blocking reason and exact missing or conflicting input.
