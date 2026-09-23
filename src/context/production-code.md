# Production-code context

Read:

- `../conventions/core/ergonomic-approach-rules.md`;
- `../conventions/core/process/dev-task-boundaries.md`;
- `../conventions/core/artifact-reuse.md`.

For development work, read `../conventions/core/process/production-code-development.md`.
For refactoring work, read `../conventions/core/process/production-code-refactoring.md`.
When changing resource acquisition, use, cleanup, or ownership, read `../conventions/core/resource-lifetimes.md`.
When production values or types would otherwise hide meaning, unit, range, or nullability, read `../conventions/core/semantic-value-types.md`.
Before finalizing production-code changes, apply `../conventions/core/artifact-reuse-checklist.md` to the final diff.
Fix every failed applicable item.
Apply applicable items from `../conventions/core/ergonomic-approach-checklist.md` to the final diff.
