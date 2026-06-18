# Code implementation

## Loading

- If the task adds or changes production values, parameters, fields, DTOs, API contracts, repository methods, or persistence bindings whose primitive type would hide meaning, unit, range, or nullability, load `./semantic-value-types.md`.
- If the project repository uses Spring, load `./spring.md`.
- If the task changes or adds production database schema migrations, or production persistence changes require a schema change, load `./db-schema-migrations.md`.
- If the task changes or adds a database-backed read, changes a query-mapped type, or changes ordering, filtering, pagination, result limiting, deduplication, or existence checks of database-backed data, load `./db-query-shaping.md` and `./db-read-model-boundaries.md`.
- If the task changes or adds a persistence-backed class, constructor, factory, repository mapping, serializer, or persistence adapter, load `./persistence-models.md`.
- If the task changes or adds a production operation, operation helper, or workflow method that reads, calculates, writes, or returns domain data, load `./operations-design.md`.
- If the task changes or adds a DOP, production component dependency shape, or operation-resource wiring, load `./ergonomic-architecture.md` and `./ergonomic-component-structure.md`.

## Reuse

- Prefer changing existing code over adding new abstractions.
- Before copying any existing artifact, prefer reuse, move, reference, extraction, or parametrization.
- For structured artifacts that support references or imports, reuse or extract shared definitions instead of duplicating equivalent definitions.
- Do not create a copied variant unless those options were checked and do not work, or the user explicitly asked for a fork.
- If copying is still necessary, state the constraint that prevents reuse.

## Kotlin

- Preserve existing blank separator lines in code.
- Never make a property nullable unless it is actually nullable in the domain.
- Treat default argument values in production callables as behavior, not compile, source/API compatibility, or call-site propagation fixes.
- Add or change a default argument only when current client usage shows that more than half of clients intentionally pass the same value, that value is explicit target behavior for omitted calls, and omission is safe.
- Omission is safe only when forgetting to pass the argument cannot cause unexpected side effects or hide a required behavior choice.
- Otherwise pass the argument explicitly at every affected call site.
- If explicit propagation crosses the current task boundary, stop and report it instead of adding a default.
- Use the configured `artifact_language` for comments in code.
- Prefer Kotlin operator syntax over direct `operator fun` calls.
- Prefer Kotlin reified or extension APIs over equivalent Java `Class<T>` overloads where available.
- Prefer functional style: immutable data, pure functions, and declarative `map`/`filter`-style transformations where they keep code clear.
- Prefer plain Kotlin singleton objects over classes when no direct or transitive mutable state is needed.
- If a helper does not depend on class state, implement it as a top-level function.
- Avoid public top-level values and properties.
- If a value has an obvious owning type, place it on that type or its `companion object`.
- If a helper has a clear primary argument, implement it as an extension function on that type.
- Use named arguments for constant values and variables whose name differs from the corresponding parameter name.
- Do not change wildcard imports as import-style cleanup, including wildcard imports introduced by the target diff, unless the user asks for it, local lint fails, or local configuration forbids them.

## HTTP API versions

- When adding a newer version of an existing HTTP API operation, keep Kotlin identifiers for the current operation unversioned and rename the previous operation's Kotlin wrappers to versioned identifiers.
