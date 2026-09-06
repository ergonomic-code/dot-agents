# Production-code context

Read:

- `../conventions/ergonomic-approach-rules.md`;
- `../conventions/process/dev-task-boundaries.md`;
- `../conventions/artifact-reuse.md`.

For development work, read `../conventions/process/production-code-development.md`.
For refactoring work, read `../conventions/process/production-code-refactoring.md`.
When changing resource acquisition, use, cleanup, or ownership, read `../conventions/resource-lifetimes.md`.
When production values or types would otherwise hide meaning, unit, range, or nullability, read `../conventions/semantic-value-types.md`.
When changing Kotlin, read `../conventions/kotlin-implementation.md`.
Before finalizing production-code changes, apply `../conventions/ergonomic-approach-checklist.md` and `../conventions/artifact-reuse-checklist.md` to the final diff.
For Kotlin changes, also apply `../conventions/kotlin-implementation-checklist.md`.
Fix every failed applicable item.
