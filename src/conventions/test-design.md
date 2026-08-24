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
- The `When` action receiver must be the selected component instance or a thin local wrapper that invokes only it.
- Logged-in clients, `*Api`, `*HttpApi`, controllers, and `*TestApi` are not component-test actions.
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
- `*Assertions` are stateless reusable assertions over domain values supplied by the caller.
- `*Assertions` must not fetch state or depend on `*TestApi`, repositories, services, clients, or other stateful helpers.
- Put reusable single-scope verification that must obtain state in a `verify...` method of that scope's `*TestApi`.
- If three or more consecutive assertions verify one correspondence between two object groups already available to the test, extract them into a named domain assertion.
- Helper methods such as `*ForResponse` and `*ForError` may be used inside typed boundary helpers to separate reusable operation-level verification paths from test cases.

## Observation

- Verify behavior through the same architectural boundary as the test kind.
- Boundary-test actions still use boundary helpers.
- Boundary-test observation may use typed `*TestApi` helpers to fetch required data.
- For observation-only reads, `*TestApi` may call controller methods directly; if not practical, call operation methods; otherwise call resource methods.
- Do not verify boundary-test outcomes by reading database state directly.
- Direct database reads are allowed only to verify async work scheduling when no standard observation API exists.

## Fixture and helper structure

- Extract all fixture code from test case classes into helpers such as `*ObjectMother`, `*FixturePresets`, `*TestApi`, `*HttpApi`, `*Assertions`.
  Even if the current code contains helpers in the same file.
- Keep test case class files focused on test cases.
  Do not keep fixture setup or helper functions in the same file, including top-level helpers.

## Invariants

- Create or change persistent coverage only for behavior or a contract required by the current explicit user request or the task brief, or for a specifically requested implementation detail as defined below.
- During a non-test step, change an existing test or test helper only as mechanically required to keep existing behavior checks compiling and passing; add no new observation or assertion.
- A `todo.md` item, solution or implementation design, implementation step, or verification instruction does not by itself create a test obligation.
- Do not test an implementation detail unless the user explicitly requests that specific test in the current conversation or an earlier explicit user request for it is unambiguously recorded in the task brief.
- Agent-authored `todo.md`, solution, implementation-design, or test-case text is not evidence of that exception.
- Except for a specifically requested implementation-detail assertion, test cases must verify observable outcomes and stay decoupled from internal implementation details; do not assert calls between internal components, dependency wiring, or control flow.
- Boundary tests must not bypass the external entry point.
- Component tests must not drift into external transport concerns.
- Pure computation tests must not drift into component or boundary setup.
