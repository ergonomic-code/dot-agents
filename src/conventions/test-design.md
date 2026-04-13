# Test design

## Test kinds

- Classify tests by architectural boundary.
- Use three primary kinds: `boundary`, `component`, `pure computation`.
- `API test` may be used as an alias for `boundary test`.
- `unit test` may be used as an alias for `pure computation test`.

## Boundary tests

- A boundary test exercises the system through an external entry point.
- The entry point may use any transport or trigger mechanism.
- A boundary test case must stay a thin scenario script.
- A boundary test case must describe actions and outcomes in business or end-user terms.
- A boundary test case must not contain low-level request construction, response parsing, or transport boilerplate.
- A boundary test case must call the entry point through a typed boundary helper such as `*HttpApi`.
- A boundary test case may verify transport-level details only when they are part of the scenario contract under test.

## Component tests

- A component test calls one application component directly.
- A component is defined by the project architecture, not by a language framework or DI container.
- In the Ergonomic Approach, a component is typically a resource, an operation, or a port.
- A component test may use fixture helpers for setup and observation.
- A component test should verify the behavior of the selected component, not the surrounding transport.

## Pure computation tests

- A pure computation test exercises only deterministic computation.
- A pure computation test must not depend on IO, network, database, time, scheduler, or DI container behavior.
- Prefer property-based tests for pure computation when the behavior is naturally specified by properties.
- Use example-based tests when a small set of examples states the behavior more clearly.

## Test-layer helpers

- `*HttpApi` is a typed helper for boundary tests that hides transport details from test cases.
- `*TestApi` is a typed helper for fixture setup and observation.
- `*FixturePresets` materialize reused or complex test state.
- `*Assertions` hold reusable domain assertions.
- `*ForError` is used for error-path verification.
- `*ForResponse` is used only for successful response payload verification.

## Fixture and helper structure

- Extract all fixture code from test case classes into helpers such as `*ObjectMother`, `*FixturePresets`, `*TestApi`, `*HttpApi`, `*Assertions`.
  Even if the current code contains helpers in the same file.
- Keep test case class files focused on test cases.
  Do not keep fixture setup or helper functions in the same file, including top-level helpers.

## Invariants

- Test cases must stay decoupled from internal implementation details.
- Boundary tests must not bypass the external entry point.
- Component tests must not drift into external transport concerns.
- Pure computation tests must not drift into component or boundary setup.
