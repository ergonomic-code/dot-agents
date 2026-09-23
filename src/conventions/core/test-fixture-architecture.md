---
keywords:
  - tests
  - fixture-architecture
---

# Test fixture architecture

## Helper boundaries

- `*TestApi` is scoped to one aggregate, resource, or external system.
- If setup or observation needs another aggregate/resource, create or use its own `*TestApi`.
- `*TestApi` may contain reusable single-scope production calls for setup and observation.
- `*TestApi` may expose `verify...` methods that obtain and assert state within its scope.
- Put low-level single-scope setup and observation helpers in the scoped `*TestApi`, not in test classes.
- `*Assertions` are stateless and operate only on domain values supplied by the caller.
- `*Assertions` must not depend on `*TestApi` or production dependencies to obtain state.
- `*TestApi` must not orchestrate writes across multiple aggregates/resources.
- Cross-aggregate/resource setup belongs in `*FixturePresets`.
- `*FixturePresets` may compose multiple `*TestApi`, `*ObjectMother`, and `Mock*Server`.
- Model complex setup as a declarative `*Fixture`; materialize it through `*FixturePresets`.
- Do not introduce fixture aggregator components only to simplify injection.

## Boundary check

- Before designing a new helper method, inspect existing scoped helpers and their usages.
- Reuse a generic setup method when the selected behavior does not distinguish the concrete data subtype.
- Name a scoped helper by its action or observed state without repeating its owner scope or exposing storage topology that the selected behavior does not distinguish.
- Before adding or changing a `*TestApi`, name its aggregate/resource scope.
- If a helper method needs data from another scope, move that lookup to that scope's `*TestApi`.
- If a helper method creates, links, binds, or updates objects from multiple scopes, move it to `*FixturePresets`.
- Method shapes like `createXForY`, `addXToY`, `bindXToY`, or `attachXToY` are `*FixturePresets` unless `X` and `Y` are inside the same aggregate/resource.
- A `*TestApi` constructor depending on repositories, clients, or APIs from several scopes is a boundary violation.
- If no `*TestApi` exists for the other scope, create it instead of expanding the current one.
- Do not combine observations from multiple scopes into an assertion-specific data holder; keep them as separate calls to the scoped `*TestApi.verify...` methods.

## Test case usage

- Test-case setup and observation must access production repositories, DAOs, services, clients and other compoents and stateful actions only through a scoped `*TestApi`.
- Do not inject those production dependencies into a test class for setup or observation.
- When planning such access, name the existing `*TestApi` or include creation of a scoped `*TestApi`; mention the production dependency only as its implementation detail.
- Use direct `*TestApi` calls only for simple setup or observation.
- Use `*FixturePresets` when setup creates a related graph, spans multiple aggregates/resources, configures stubs, or is reused.
- Inject only the fixture helpers required by the test class.
