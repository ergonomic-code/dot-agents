# HTTP API test checklist

- Do all changed HTTP boundary tests avoid direct calls to `WebTestClient` and `RestTestClient`?
- Does each changed `*HttpApi` operation keep one canonical `*ForResponse` request builder that typed overloads delegate to?
- Do public typed `*HttpApi` methods mirror the controller contract by parameters and result type?
- Do transport checks, schema validation, and body decoding stay inside `*HttpApi`?
- Were extra test-layer `*Request` or `*Response` DTOs avoided when the controller contract already defines the transport shape?
