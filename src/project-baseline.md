# Project baseline

## Brevity

Be **maximally laconic** in chat and generated artifacts.
Prefer shorter wording and fewer sections.
Omit explanations unless they change correctness.

## Loading order

- Use resolved framework values from the host context.
- Load this file.
- Before the first substantive response and before task triage, read `roles.md`.
- Resolve the active role from `roles.md` and the current user request.
- Before the first substantive response and before task triage, read the selected role file at `roles/<role>.md`.
- If `<framework-config-path>` is set and the file exists, read it as YAML.
  Use the value of the `artifact_language` field to determine the natural language for user-facing artifacts (comments, commit messages, documentation).
  Default to Russian (`ru`) when the configuration file or the field is absent.
