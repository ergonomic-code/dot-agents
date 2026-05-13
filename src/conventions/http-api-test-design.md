# HTTP API test design

## Scope

- These rules apply to HTTP boundary tests and `*HttpApi` helpers.

## Public contract

- A public typed `*HttpApi` method must mirror the controller contract by using the same logical parameters and the same result type.
- Treat parameters required from current clients as required public typed `*HttpApi` parameters even when the controller keeps backend defaults for compatibility.
- Do not give default argument values to such current-client parameters.
- Do not introduce extra test-layer `*Request` or `*Response` DTOs when the controller transport contract already defines the shape.

## Per-operation pattern

- Each operation must have one canonical `*ForResponse` request builder.
- `*ForResponse` must build the HTTP request and return a response spec.
- A typed success method must delegate to `*ForResponse`, check the expected status, validate the schema, and decode the body into the controller type.
- Use `*ForError` for expected negative cases.
- Use `*ForOutcome` when either success or an expected error is legitimate and the result should stay typed instead of throwing on an expected error.

## Builders and overloads

- Typed overloads must delegate to the canonical request builder.
- For invalid or raw transport values, add an escape hatch to `*ForResponse` instead of ad-hoc helper methods for each case.
- If a scenario depends on omitting a parameter entirely, add a raw or relaxed overload that can truly omit the key instead of injecting a default.
- Keep compatibility omissions in explicit legacy, raw, or relaxed paths and cover them with separate compatibility tests.
- When one case needs a raw value, expose it only on the narrowest required path and do not propagate it to unrelated typed success methods.

## Encapsulation

- Keep status checks, header checks, request schema validation, response schema validation, and body decoding inside `*HttpApi`.
- Tests must not call `WebTestClient` or `RestTestClient` directly.
- Boundary tests must stay thin scenario scripts over `*HttpApi`, not a place for HTTP plumbing.
- For status checks on the project error response body type, use an existing semantic project assertion for that type.
  If none exists and the check is reusable or contract-level, add one to project-local test assertions instead of comparing raw status fields in tests.

## Implementation rules

- Inside `*HttpApi`, prefer simple URI templates over `uri { uriBuilder -> ... }` when the path is static.
- Extract repeated authorization and client setup into shared DSL or helper code.
- Use `ParameterizedTypeReference<T>` or a project helper built on top of it for generic decoding.
- If the project uses a custom `JsonMapper`/`ObjectMapper`, align the client codecs with it.
