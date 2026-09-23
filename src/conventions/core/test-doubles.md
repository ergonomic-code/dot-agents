---
keywords:
  - tests
  - doubles
---

# Test doubles

- Plan tests against existing production components or selected-design components with existing project test infrastructure whenever that safely executes the behavior within test budgets.
- Use a fake, stub, or mock only when neither can reproduce the behavior safely within those budgets; pending implementation and easier setup, control, or observation are insufficient.
- Prefer an existing project double over creating a new one.
- Do not introduce or generalize a production interface solely to substitute a test double.
- Когда нужен class-level double, явно собери target dependency graph из real dependencies и замени только dependency с симулируемым поведением.
- Use in-process class or object mocks only for behavior that is hard or expensive to reproduce with a real dependency, typically infrastructure failures, or the smallest mechanism for a specifically requested internal-interaction test under `./test-design.md`; otherwise omit them for normal behavior.
- Except for that requested test, verify interactions only at external-system boundaries and only for outgoing requests or messages.
- Do not use mocks or spies to observe calls between internal classes or objects except for that specifically requested test.
