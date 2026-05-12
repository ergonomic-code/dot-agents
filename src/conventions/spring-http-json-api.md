# Spring HTTP JSON API

## Error responses

- Apply `../patterns/http-json-api/error-response-body-format.md`.
- For new Spring 6+ error bodies, use `org.springframework.http.ProblemDetail`.
- Add contract-specific extra fields through `ProblemDetail` properties or a subclass.
- If project context defines a custom or legacy error body type, use that type instead of `ProblemDetail`.
- Do not change an existing error body shape only to match this convention unless requested.
