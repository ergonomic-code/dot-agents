---
keywords:
  - http-api
  - tests
---

# HTTP API test rules

- For HTTP boundary tests and `*HttpApi` changes, design public typed `*HttpApi` methods to mirror the controller contract by parameters and result type.
- Keep HTTP boundary tests as thin scenario scripts over `*HttpApi` and do not call transport clients directly from tests.
- Keep transport checks, schema validation, and body decoding inside `*HttpApi`.
- For status checks on the project error response body type, use semantic project assertions instead of raw status field comparisons.
- Do not introduce extra test-layer transport DTOs when the controller contract already defines the request or response shape.

## Changed response contracts

- A changed typed `*HttpApi` success path must match its governing target endpoint and response shape.
- Its helper, route, DTO, schema, and decoded type must belong to the same contract version.
- New production contract surface must be limited to the compile-only shape required by the selected case.
- A changed-response test must assert a property that distinguishes the target shape; status, pagination, or decoding an earlier DTO is insufficient.
- Raw JSON assertions are limited to transport or member-absence properties that the typed contract cannot represent.
