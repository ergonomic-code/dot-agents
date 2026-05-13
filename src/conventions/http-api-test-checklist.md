# HTTP API test checklist

- Do all changed HTTP boundary tests avoid direct calls to `WebTestClient` and `RestTestClient`?
- Does each changed `*HttpApi` operation keep one canonical `*ForResponse` request builder that typed overloads delegate to?
- Do public typed `*HttpApi` methods mirror the controller contract by parameters and result type?
- Do current-client parameters stay required in public typed `*HttpApi` methods without default argument values?
- Are compatibility omissions isolated in explicit legacy, raw, or relaxed paths with separate compatibility tests?
- Did each helper signature change touch only paths required by the selected case?
- Do transport checks, schema validation, and body decoding stay inside `*HttpApi`?
- Do status checks on the project error response body type use semantic project assertions instead of raw status field comparisons?
- Were extra test-layer `*Request` or `*Response` DTOs avoided when the controller contract already defines the transport shape?
