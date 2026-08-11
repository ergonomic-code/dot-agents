# Test doubles

Before choosing test dependencies:

- Prefer existing real components and project test infrastructure.
- If a dependency cannot be real, prefer an existing project fake, fixture, or external-system stub.
- Use in-process class or object mocks only to simulate behavior that is hard or expensive to reproduce with a real dependency, typically infrastructure failures.
- Do not use them for normal behavior.
- Verify interactions only at external-system boundaries and only to assert the correctness of outgoing requests or messages.
- Do not use mocks or spies to observe calls between internal classes or objects.
- Do not use Spring bean override mechanisms such as `@MockBean`, `@SpyBean`, `@MockitoBean`, or `@MockitoSpyBean`.
- When a class-level double is required, construct the target dependency graph explicitly from real dependencies in the existing application context and substitute only the dependency whose behavior must be simulated.
- If the target requires framework proxies, register the explicitly constructed graph through existing test infrastructure in the same application context without overriding its beans.
