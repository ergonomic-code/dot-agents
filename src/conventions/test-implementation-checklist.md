# Test implementation checklist

- For each literal, enum member, constant, code, id, date, or name: does the case or public contract name it?
- For each named fixture constant or preset: is that exact named variant required?
- If no, replace it with a role helper, factory, or fixture.
- Is fixture setup minimal?
- Are expected values bound in `Given` and reused?
- Are exact literals absent from `Then`?
