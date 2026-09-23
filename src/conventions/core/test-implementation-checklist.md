---
keywords:
  - tests
  - checklist
---

# Чек-лист реализации тестов

- Is every changed test backed by the current explicit request or supplied requirements, an unambiguously recorded earlier explicit implementation-detail request, or a mechanical compile adaptation without a new observation?
- Использует ли каждый test-case method literal-секции `Given`, `When` и `Then`, с отдельными `And when` и `Then` для каждого observation endpoint?
- For each literal, enum member, constant, code, id, date, name, fixture constant, or preset: does the case or public contract require that exact variant?
- Is fixture setup minimal, shared state reused where suitable, setup-returned ids preferred, and shared state cleaned only by the shared reset layer?
- Do tests assert observable outcomes without internal calls, wiring, or control flow except for a specifically requested implementation-detail assertion?
- Нужен ли каждый fake, stub или mock, поскольку ни existing production component, ни component required selected design не воспроизводит поведение безопасно в пределах test budgets?
- Не привёл ли test double к введению или обобщению production interface?
- Are in-process class or object mocks limited to behavior that is hard or expensive to reproduce with a real dependency, typically infrastructure failures, or the smallest mechanism for a specifically requested internal-interaction test, and otherwise absent for normal behavior?
- Проверяются ли interactions только на external-system boundaries и только для outgoing requests или messages, кроме специально запрошенного internal-interaction test?
- Are low-level setup and observation helpers absent from test classes, scoped `*TestApi` helpers used, and cross-scope setup placed in `*FixturePresets`?
- Остаётся ли каждый `*TestApi` в одном aggregate/resource scope, stateful verification — в его `verify...`, а `*Assertions` — stateless над domain values caller?
- Проверяются ли observations разных scopes отдельно без assertion-specific data holder?
- Are expected values bound in Given and are new test methods appended to the class?
