# Task boundaries

- Treat explicit phase, stop, pause, test-only, production-only, refactor-only, and behavior-only instructions as hard boundaries.
- Do not cross hard boundaries to satisfy TDD, autonomy, self-check, test-green pressure, or a larger plan.
- If a hard boundary conflicts with making tests pass, compiling the whole target, or completing the larger plan, stop and report the blocker.

## Change mode

- In one coding slice, either refactor code or change behavior.
- Refactoring may change structure only and must preserve externally observable behavior.
- Behavior changes must preserve structure and avoid refactoring.
- If the requested behavior cannot be changed without structural change, stop and ask to split the work.

## Write set

- In one coding slice, change either tests or production code.
- If the request needs both tests and production code, execute only the current or first explicit slice, then stop and report the next slice.
- Test-only slices may adjust API DTO shape only as needed for test compilation.
- Do not edit non-DTO production code to make a test-only slice pass.
- If test-only changes require production behavior, stop with the failing tests and blocker.
- Production-only slices must not edit tests, fixtures, test data, assertions, or test build configuration.
