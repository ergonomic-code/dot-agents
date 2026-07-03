# Production Code Development

In this mode, the primary task is changing production behavior.

Make only the minimal changes required for the requested behavior.

If the request is a direct behavior change and is not explicitly scoped to making one selected red case green, implement the behavior fully.
Do not return fake, placeholder, temporary, or test-shaped data as a substitute for the requested behavior.

## Existing Code Protection

Existing production code means any callable, class, endpoint, operation, repository, DTO, persistence mapping, or behavior that existed before the current slice.
New code inserted into an existing call path is part of that existing path.

Do not fake, bypass, special-case, or degrade existing production behavior to satisfy the selected test or request.
If the selected test or failing caller already targets an existing callable and the fix requires a new input, extend that callable and propagate the argument through the existing call path.
Do not add sibling overloads, wrapper methods, helper entry points, default arguments, or compatibility shims only to avoid updating affected call sites.
If required propagation crosses the current slice boundary or would require changing test semantics, stop and report the blocker.

## Selected Red Case Greening

Placeholder production behavior is allowed only when an explicit red-case workflow is making one selected failing case green.
The placeholder must live only inside newly introduced production code that has no previous implementation and is the intended new behavior surface for the selected case.
The placeholder must not replace, bypass, or preserve compatibility for existing production behavior.
Keep placeholder behavior deterministic and local to the new code.
It may derive fake return data from available parameters and constants owned by the current slice.
Do not add scenario branches such as `if`, `when`, or equivalent test-shaped dispatch only to satisfy individual examples.
Report any placeholder explicitly in the result.

## Test Changes

Test changes are allowed only when a production API change makes existing tests fail to compile.
In that case, update only the affected call sites without changing test semantics.

If the task cannot be completed without changing test semantics, stop and ask what to do.

Constraints:

- Do not add, remove, weaken, or strengthen test cases.
- Do not change the meaning of `Given`, `When`, or `Then` steps.
