---
keywords:
  - tests
  - doubles
---

# Test doubles

Before choosing test dependencies:

- Plan tests against existing production components or the production components to be implemented by the selected design, together with existing project test infrastructure, whenever that setup can execute the selected behavior safely within the applicable test budgets.
- Use a fake, stub, or mock only when neither an existing production component nor one required by the selected design can reproduce the selected behavior safely within the applicable test budgets; pending implementation and easier setup, control, or observation are not sufficient.
- Prefer an existing project double over creating a new one after that condition is met.
- Do not introduce or generalize a production interface solely to substitute a test double.
- Use in-process class or object mocks only to simulate behavior that is hard or expensive to reproduce with a real dependency, typically infrastructure failures, or as the smallest mechanism for a specific internal-interaction test explicitly requested by the user under `./test-design.md`.
- Do not use them for normal behavior or unrequested internal interactions.
- Except for such a specifically requested internal-interaction test, verify interactions only at external-system boundaries and only to assert the correctness of outgoing requests or messages.
- Do not use mocks or spies to observe calls between internal classes or objects except for such a specifically requested test.
- Do not use Spring bean override mechanisms such as `@MockBean`, `@SpyBean`, `@MockitoBean`, or `@MockitoSpyBean`.
- When a class-level double is required, construct the target dependency graph explicitly from real dependencies in the existing application context and substitute only the dependency whose behavior must be simulated.
- Resolve real production collaborators used only to construct that graph locally through an inherited `getBean<T>()`; do not inject them or the application context into the test class constructor or fields.
- If the shared test superclass lacks this helper, add a protected `getBean<T>()` there that delegates to its existing application context.
- If the target requires framework proxies, register the explicitly constructed graph through existing test infrastructure in the same application context without overriding its beans.
