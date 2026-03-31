# Project baseline

## Brevity

Be **maximally laconic** in chat and generated artifacts.
Prefer shorter wording and fewer sections.
Omit explanations unless they change correctness.

## Loading order

- Use resolved framework values from the host context.
- If an activated skill provides its own loading instructions, follow the skill first.
- Load this file.
- Before the first substantive response and before task triage, read `roles.md`.
- Resolve the active role from `roles.md` and the current user request.
- Before the first substantive response and before task triage, read the selected role file at `roles/<role>.md`.
- Treat the project `AGENTS.md` as the project integration layer.
- If project `AGENTS.md` declares `## Local contexts`, use that section as the single source of project-local context files and their loading conditions.
- Load only the local context files relevant to the current task.
- Prefer per-entry loading conditions in `## Local contexts` over separate project-specific loading-order sections.
- If `<framework-config-path>` is set and the file exists, read it as YAML.
  Use the value of the `artifact_language` field to determine the natural language for user-facing artifacts (comments, commit messages, documentation).
  Default to Russian (`ru`) when the configuration file or the field is absent.
