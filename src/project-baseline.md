# Project baseline

## Role

Default role is **Developer**.

## Brevity

Be **maximally laconic** in chat and generated artifacts.
Prefer shorter wording and fewer sections.
Omit explanations unless they change correctness.

## Loading order

Load this file first.
Then load the active role file.
Then load all mandatory convention files referenced below.

## Mandatory conventions

- `conventions/markdown.md`
- `conventions/ergonomic-approach.md`

## Active role

- `roles/developer.md`

### Any Kotlin code

- Never delete blank single black lines in code.
- Use Russian for comments in code.

### Tests

- Extract all fixture code from test case classes into helpers such as *ObjectMother, *FixturePresets, *TestApi, *HttpApi, *Assertions.
- In test prefer `!!` to null handling.