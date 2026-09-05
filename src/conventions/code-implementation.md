# Code implementation

## Reuse

- Prefer changing existing code over adding new abstractions.
- Before copying any existing artifact, prefer reuse, move, reference, extraction, or parametrization.
- For structured artifacts that support references or imports, reuse or extract shared definitions instead of duplicating equivalent definitions.
- Do not create a copied variant unless those options were checked and do not work, or the user explicitly asked for a fork.
- If copying is still necessary, state the constraint that prevents reuse.

## Resource lifetimes

- Unless an API explicitly transfers ownership, keep the complete acquire-use-cleanup lifecycle of a resource in one method.
- That method must clean up through `finally`, or delegate the complete lifecycle, including acquisition and cleanup, to a scoped helper.
- Callees inside the lifecycle may use the resource but must not clean it up.

## Kotlin

- Preserve existing blank separator lines in code.
- Prefer `val` for fields, local values, parameters, configuration values, fixtures, and lifecycle values.
- In Kotlin function declarations, omit an explicit `: Unit` return type only when Kotlin would still infer `Unit`.
- Never make a field, local value, parameter, configuration value, fixture value, or lifecycle value nullable unless absence is real behavior.
- Do not encode delayed initialization, fixture setup, runtime startup, optional wiring, or convenience construction as nullable when a constructor, factory, provider, local `val`, explicit boundary check, or narrower scope can expose the value as non-null.
- Treat default argument values in production callables as behavior, not compile, source/API compatibility, or call-site propagation fixes.
- Add or change a default argument only when current client usage shows that more than half of clients intentionally pass the same value, that value is explicit target behavior for omitted calls, and omission is safe.
- Omission is safe only when forgetting to pass the argument cannot cause unexpected side effects or hide a required behavior choice.
- Otherwise pass the argument explicitly at every affected call site.
- If explicit propagation crosses the current task boundary, stop and report it instead of adding a default.
- Use the configured `artifact_language` for comments in code.
- Prefer Kotlin operator syntax over direct `operator fun` calls.
- Prefer Kotlin reified or extension APIs over equivalent Java `Class<T>` overloads where available.
- Prefer functional style for functionally pure transformations: immutable data, pure functions, and declarative `map`/`filter`-style transformations where they keep code clear.
- Use Kotlin expression bodies only when the complete represented behavior is fast and safe and is either functionally pure or limited to fast, safe ambient reads such as current time or environment variables.
- Treat work deferred through lambdas, sequences, streams, futures, or similar lazy values as represented behavior; use a block body when any represented work performs other I/O, changes observable state, may block, or owns a resource lifecycle.
- Prefer plain Kotlin singleton objects over classes when no direct or transitive mutable state is needed.
- If a helper does not depend on class state, implement it as a top-level function.
- Avoid public top-level values and properties.
- If a value has an obvious owning type, place it on that type or its `companion object`.
- If a helper has a clear primary argument, implement it as an extension function on that type.
- Use named arguments for constant values and variables whose name differs from the corresponding parameter name.
- Do not leave fully qualified names at Kotlin use sites; use imports or import aliases instead.
- Do not change wildcard imports as import-style cleanup, including wildcard imports introduced by the target diff, unless the user asks for it, local lint fails, or local configuration forbids them.

## HTTP API versions

- When adding a newer version of an existing HTTP API operation, keep Kotlin identifiers for the current operation unversioned and rename the previous operation's Kotlin wrappers to versioned identifiers.
