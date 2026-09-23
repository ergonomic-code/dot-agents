---
keywords:
  - tests
  - implementation
---

# Test implementation

## Test case body

- In every new or changed test-case method, split the body with literal `Given`, `When`, and `Then` comments, adapting only the language comment syntax.
- Put setup under Given, the action under When, and verification under Then.
- In command tests with a public observation API, put the target command under `When` and the observation operation under `And when`.
- If command-returned data must be checked before observation, use `When`, `Then`, `And when`, `Then`.
- If observing the result requires several endpoint calls, render each under its own `And when` followed by `Then`.

## Fixture setup

- Each test case must explicitly establish its required fixture.
- Establishing a fixture may reuse shared setup state instead of creating new DB data.
- Do not add per-test cleanup for shared fixture state; use or extend the shared fixture setup/reset layer.
- Before adding cleanup or DB fixture data, inspect the selected test container's setup/reset path and shared state.
- Reuse semantically suitable shared fixture state when the entity identity is not the behavior under test.
- If fixture setup code duplication exceeds 3 lines, it may be extracted into helpers.
- In fixture setup specify only data relevant to the test-case; derive related data instead of copying it.
- Prefer values returned by fixture setup over extra observation calls when they identify created data.
- Do not broaden fixture data or add visibility-only fields only to make an incidental observation path work.

## Assertions and data

- Do not put expected literals in Then; bind each business value once in Given and reuse it in setup, request, and assertions.
- Do not extract a self-evident expected literal used only once into a Given variable.
- If exact value is not the point, assert a property; if derived, compute it in Given.
- If a literal is unavoidable, declare it in Given with a short rationale comment.
- In test-case bodies, name expected-value variables by the expected meaning or checked property, not `expected*`; `expected*` names are allowed in helpers.
- Exact input values include literals, enum members, constants, codes, ids, dates, and names.
- Use exact input values only when the case or public contract names them; otherwise encode the data role in a helper, factory, or fixture.
- Prefer generic role helpers over incidental named samples.

## Coverage

- For each changed or added operation and computation, cover each normal and realistically reachable path with at least one case, excluding paths for unexpected and practically impossible failures.
- Prefer a unit test when verification needs no infrastructure or I/O, otherwise a boundary test; use a component test only for a material reduction in size or time or to stay on standard test infrastructure.

## Determinism and ordering

- Do not use non-deterministic randomness; use faker or data factories built on top of it.
- Do not use fixed sleep to await an asynchronous result.
- For class-based tests, always add new test case methods to the end of the class.
