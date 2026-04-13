# HTTP API test rules

- For HTTP boundary tests and `*HttpApi` changes, design public typed `*HttpApi` methods to mirror the controller contract by parameters and result type.
- Keep HTTP boundary tests as thin scenario scripts over `*HttpApi` and do not call transport clients directly from tests.
- Keep transport checks, schema validation, and body decoding inside `*HttpApi`.
- Do not introduce extra test-layer transport DTOs when the controller contract already defines the request or response shape.
