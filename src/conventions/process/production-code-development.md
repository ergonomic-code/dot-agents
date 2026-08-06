# Production Code Development

In this mode, the primary task is changing production behavior.

Make only the minimal changes required for the requested behavior.

Implement the requested behavior fully within the selected scope.
A constant implementation is complete when its result is contract-correct for every input and state in the selected behavior class and does not degrade behavior outside that class.
Later cases may require generalizing that implementation.
Do not return fake, placeholder, temporary, or test-shaped data as a substitute for the requested behavior.

## Existing Code Protection

Existing production code means any callable, class, endpoint, operation, repository, DTO, persistence mapping, or behavior that existed before the current slice.
New code inserted into an existing call path is part of that existing path.

Do not fake, bypass, special-case, or degrade existing production behavior to satisfy the selected test or request.
Do not classify such a contract-complete constant implementation as fake or temporary only because later behavior classes will require more paths.
If the selected test or failing caller already targets an existing callable and the fix requires a new input, extend that callable and propagate the argument through the existing call path.
Do not add sibling overloads, wrapper methods, helper entry points, default arguments, or compatibility shims only to avoid updating affected call sites.
If required propagation crosses the current slice boundary or would require changing test semantics, stop and report the blocker.

## Test Changes

Test changes are allowed only when a production API change makes existing tests fail to compile.
In that case, update only the affected call sites without changing test semantics.

If the task cannot be completed without changing test semantics, stop and ask what to do.

Constraints:

- Do not add, remove, weaken, or strengthen test cases.
- Do not change the meaning of `Given`, `When`, or `Then` steps.
