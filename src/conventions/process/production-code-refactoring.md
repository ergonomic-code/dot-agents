# Production Code Refactoring

In this mode, the task is changing the structure, shape, or names of production code without changing behavior.

Test changes are allowed only when a production API refactor makes existing tests fail to compile.
In that case, update only the affected call sites without changing test semantics.

If the task cannot be completed without changing production behavior or test semantics, stop and ask what to do.

Constraints:

- Do not change production behavior.
- Do not add, remove, weaken, or strengthen test cases.
- Do not change the meaning of `Given`, `When`, or `Then` steps.
