# Test implementation checklist

- Does each new or changed test-case method use `// Given`, `// When`, and `// Then` sections?
- If a case observes the result through several endpoints, does each observation use its own `// And when` and following `// Then`?
- Does each new or changed JUnit test class and test-case method put its human name in `@DisplayName` when supported?
- For each literal, enum member, constant, code, id, date, or name: does the case or public contract name it?
- For each named fixture constant or preset: is that exact named variant required?
- If no, replace it with a role helper, factory, or fixture.
- Is fixture setup minimal?
- Does the test use setup-returned values instead of extra observation calls that require broader fixture data?
- Are there no public read calls used only to discover setup-created ids or refs?
- Is shared fixture state cleaned only by the shared setup/reset layer?
- Are in-process mocks absent except for hard or expensive error simulation?
- Are low-level setup and observation helpers absent from test classes?
- Are production dependencies and DI lookups absent from test classes for setup or observation?
- Does each new or changed `*TestApi` stay inside one aggregate/resource scope?
- Is each cross-scope setup helper implemented in `*FixturePresets`?
- Are expected values bound in `Given` and reused?
- Are exact literals absent from `Then`?
- Are new test case methods added to the end of the class?
