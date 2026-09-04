# Context routing

Classify the requested and planned work by every applicable dimension below.
Load every matching topical index; dimensions are independent, not alternatives.
Do not infer production-code work from the active role or from a test's implementation language.
Reevaluate all dimensions when the work scope or planned write set changes.

Load matching indexes in this order:

1. `markup.md` for writing or revising Markdown or AsciiDoc.
2. `production-code.md` for planning, adding, changing, refactoring, or reviewing production code.
3. `tests.md` for planning, adding, changing, refactoring, aligning, or reviewing tests, test helpers, or test-facing adapters.
4. `database.md` when the work touches database schema, queries, transactions, persistence mappings, or database-backed reads or writes.
5. `spring.md` when the applicable work touches a Spring project or Spring APIs.
6. `architecture.md` when the work concerns architecture, operations, data or component shape, or abstraction boundaries.

Classify the actual requested or planned work, including compile-required supporting changes, but do not load an index merely because the repository contains that kind of artifact.
