# Project baseline

## Brevity

Be **maximally laconic** in chat and generated artifacts.
Prefer shorter wording and fewer sections.
Omit explanations unless they change correctness.

## Context

- Use resolved framework values from the host context.
- If an activated skill defines loading instructions, follow the skill first.
- Resolve the active role from the current user request.
- Before the first substantive response and before task triage, read `framework_checkout_root/src/roles/<role>.md`.
- When the task may create files or depends on feature-local context, apply `framework_checkout_root/src/conventions/feature-workdir.md`.
- Apply `framework_checkout_root/src/conventions/feature-stage-skill.md` when a skill writes default stage outputs into a feature workdir.
- Treat `feature-workdir.md` as the single source of truth for active feature directory resolution and default placement of new task files.
- Treat project `AGENTS.md` as the project integration layer.
- If project `AGENTS.md` declares `## Local contexts`, use that section as the source of project-local context files.
- Load only task-relevant local context files.
- Prefer per-entry conditions in `## Local contexts` over separate project-specific loading-order rules.
- If `<framework-config-path>` is set and exists and was not loaded earlier, read it as YAML.
- Use `artifact_language` for comments and human-facing artifacts. Default to `ru` when the config or field is absent.
