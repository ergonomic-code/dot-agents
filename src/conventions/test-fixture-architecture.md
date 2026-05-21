# Test fixture architecture

## Helper boundaries

- `*TestApi` is scoped to one aggregate, resource, or external system.
- If setup or observation needs another aggregate/resource, create or use its own `*TestApi`.
- `*TestApi` may contain reusable single-scope production calls for setup and observation.
- Put low-level single-scope setup and observation helpers in the scoped `*TestApi`, not in test classes.
- `*TestApi` must not orchestrate writes across multiple aggregates/resources.
- Cross-aggregate/resource setup belongs in `*FixturePresets`.
- `*FixturePresets` may compose multiple `*TestApi`, production calls, `*ObjectMother`, and `Mock*Server`.
- Model complex setup as a declarative `*Fixture`; materialize it through `*FixturePresets`.
- Do not introduce fixture aggregator components only to simplify injection.

## Boundary check

- Before adding or changing a `*TestApi`, name its aggregate/resource scope.
- If a helper method needs data from another scope, move that lookup to that scope's `*TestApi`.
- If a helper method creates, links, binds, or updates objects from multiple scopes, move it to `*FixturePresets`.
- Method shapes like `createXForY`, `addXToY`, `bindXToY`, or `attachXToY` are `*FixturePresets` unless `X` and `Y` are inside the same aggregate/resource.
- A `*TestApi` constructor depending on repositories, clients, or APIs from several scopes is a boundary violation.
- If no `*TestApi` exists for the other scope, create it instead of expanding the current one.

## Test case usage

- Use direct `*TestApi` calls only for simple setup or observation.
- Use `*FixturePresets` when setup creates a related graph, spans multiple aggregates/resources, configures stubs, or is reused.
- Inject only the fixture helpers required by the test class.
