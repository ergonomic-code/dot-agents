# Production-code context

Read:

- `../conventions/ergonomic-approach-rules.md`;
- `../conventions/process/dev-task-boundaries.md`;
- `../conventions/artifact-reuse.md`.

For development work, read `../conventions/process/production-code-development.md`.
For refactoring work, read `../conventions/process/production-code-refactoring.md`.
When changing resource acquisition, use, cleanup, or ownership, read `../conventions/resource-lifetimes.md`.
When changing production data types, read `../conventions/data-structure-budgets.md`.
When changing subprograms, read `../conventions/subprogram-complexity-budgets.md`.
When changing components or their dependencies, read `../conventions/component-dependency-budgets.md`.
When production values or types would otherwise hide meaning, unit, range, or nullability, read `../conventions/semantic-value-types.md`.
When changing Kotlin, read `../conventions/kotlin-implementation.md`.
When adding a newer version of an HTTP API operation, read `../conventions/http-api-versioning.md`.
Before finalizing production-code changes, apply `../conventions/ergonomic-approach-checklist.md` and `../conventions/artifact-reuse-checklist.md` to the final diff.
For Kotlin changes, also apply `../conventions/kotlin-implementation-checklist.md`.
Fix every failed applicable item.
