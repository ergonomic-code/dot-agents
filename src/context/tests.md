# Test context

Read:

- `../conventions/ergonomic-design-budgets.md`;
- `../conventions/ergonomic-approach-rules.md`;
- `../conventions/process/dev-task-boundaries.md`;
- `../conventions/test-design.md`;
- `../conventions/test-doubles.md`;
- `../conventions/test-fixture-architecture.md`;
- `../conventions/test-container-selection.md`;
- `../conventions/test-naming.md`;
- `../conventions/test-implementation.md`.

When naming, renaming, or aligning a test class, case, method, or `@DisplayName`, also read `../artifacts/verification-check-format-v0.1/references/feature-naming.md` before selecting a class `@DisplayName`.
For test development, read `../conventions/process/tests-development.md`.
For test refactoring, read `../conventions/process/tests-refactoring.md`.
When tests or test support cross an HTTP boundary, also read `../conventions/http-api-test-design.md` and `../conventions/http-api-test-rules.md`.
When they cover HTTP JSON API error responses, also read `../patterns/http-json-api/error-response-body-format.md`.
Before finalizing test changes, apply `../conventions/ergonomic-approach-checklist.md` and `../conventions/test-implementation-checklist.md` to the final diff.
For HTTP-boundary test changes, also apply `../conventions/http-api-test-checklist.md`.
Fix every failed applicable item.
