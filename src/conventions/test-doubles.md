# Test doubles

Before choosing test dependencies:

- Prefer existing real components and project test infrastructure.
- If a dependency cannot be real, prefer an existing project fake, fixture, or external-system stub.
- Do not use in-process class or object mocks for normal success-path behavior.
- Avoiding context, persistence, or infrastructure setup is not an error-path reason.
- Use class or object mocks only for error paths that are hard or expensive to trigger through real objects.
- If adding a mock anyway, state why the real component, project fake, fixture, or external stub does not fit.
