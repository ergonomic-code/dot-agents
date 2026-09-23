# Context routing

Classify the requested and planned work by every applicable dimension below.
Load every matching topical index; dimensions are independent, not alternatives.
Do not infer production-code work from a test's implementation language or from any request category other than the actual requested or planned work.
Reevaluate all dimensions when the work scope or planned write set changes.
All topical paths below are relative to `framework_checkout_root/src/context/`.

Load matching indexes in this order:

1. `markup.md` for writing or revising Markdown or AsciiDoc.
2. `production-code.md` for planning, adding, changing, refactoring, or reviewing production code.
3. `tests.md` for planning, adding, changing, refactoring, aligning, or reviewing tests, test helpers, or test-facing adapters.
4. `database.md` when the work touches database schema, queries, transactions, persistence mappings, or database-backed reads or writes.
5. `http-api.md` when the work touches an HTTP operation, HTTP contract, boundary test, or typed HTTP test helper.
6. `architecture.md` when the work concerns architecture, operations, data or component shape, or abstraction boundaries.
7. `kotlin.md` when the applicable work touches Kotlin production code or Kotlin tests.
8. `spring.md` when the applicable work touches Spring APIs or Spring infrastructure.
9. `junit.md` when the applicable tests use JUnit.
10. `kotest.md` when the applicable tests use Kotest.

Classify the actual requested or planned work, including compile-required supporting changes, confirmed dependencies, and explicitly named target stack.
Do not load an index merely because another repository part contains that technology.
For a mixed project, classify the changed module and write set.
