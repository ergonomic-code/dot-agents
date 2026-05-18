# Test implementation checklist

- For each literal, enum member, constant, code, id, date, or name: does the case or public contract name it?
- For each named fixture constant or preset: is that exact named variant required?
- If no, replace it with a role helper, factory, or fixture.
- Is fixture setup minimal?
- Does each new or changed `*TestApi` stay inside one aggregate/resource scope?
- Is each cross-scope setup helper implemented in `*FixturePresets`?
- Are expected values bound in `Given` and reused?
- Are exact literals absent from `Then`?
- Are new test case methods added to the end of the class?
