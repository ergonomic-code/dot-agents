# Spring context

Load only the entries matching the requested or planned Spring work:

- Spring JDBC access or row mapping: `../conventions/spring/spring-jdbc.md`;
- Spring-managed dependency wiring: `../conventions/spring/spring-dependency-injection.md`;
- Spring bean registration: `../conventions/spring/spring-beans.md`;
- Kotlin Spring bean access or registration: `../conventions/spring/kotlin-beans.md`;
- Spring HTTP JSON API error handling or error-body contracts: `../conventions/spring/spring-http-json-api.md` and `../patterns/http-json-api/error-response-body-format.md`;
- Spring infrastructure in tests: `../conventions/spring/test-doubles.md`.

For Spring HTTP test clients, read `../conventions/spring/http-api-tests.md`.
Before finalizing applicable Spring test changes, apply `../conventions/spring/checklist.md`.

Project-specific Spring MVC handler rules remain project-local context and are loaded through project `AGENTS.md` when declared there.
