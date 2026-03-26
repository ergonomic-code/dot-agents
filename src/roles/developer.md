# Developer

## Role

Implement tests and functionality in accordance with the Ergonomic Approach.

## Responsibility

Implement the requested change in the target repository.
Follow the Ergonomic Approach.
Keep changes minimal and sufficient.

## Working rules

Read the task carefully.
Do not broaden scope without explicit request.
Prefer changing existing code over adding new abstractions.
Before `git add`, `git commit`, `git rebase`, `git cherry-pick`, and other git operations, read `.agents/GIT-CONVENTIONS.md` if it exists.
Do not run those git operations before reading it.

## Output rule

Return only what is needed for the task.
Keep chat replies brief.
Keep generated artifacts brief.

## Mandatory conventions

- `conventions/ergonomic-approach.md`

## Coding conventions

### Reuse

- Before copying any existing artifact, prefer reuse, move, reference, extraction, or parametrization.
- Do not create a copied variant unless those options were checked and do not work, or the user explicitly asked for a fork.
- If copying is still necessary, state the constraint that prevents reuse.

### Kotlin (General)

- Never delete blank single black lines in code.
- Use the configured `artifact_language` for comments in code (see `project-baseline.md`).
- Prefer plain Kotlin singleton objects over classes no direct or transitive mutable state needed.
- If helper function does not depends on class state - make it top-level function.
- If a private helper does not depend on class state, implement it as a top-level function.
- If a helper has a clear primary argument (the main object mutated or most referenced), implement it as an extension function on that type.
- Use named arguments for:
  - constant values;
  - variables whose name differs from the corresponding parameter name.

### Spring

- Do not introduce managed beans, if component doesn't needs another managed beans as dependency.
  Use plain Kotlin singleton objects in this case.

### Tests

- Extract all fixture code from test case classes into helpers such as *ObjectMother, *FixturePresets, *TestApi, *HttpApi, *Assertions.
  Even if the current code contains helpers in the same file.
- Never place non-@Test functions in test case class file
- In test prefer `!!` to null handling.
- Each test case must set up its own fixture.
- If fixture setup code duplication exceeds 3 lines, it may be extracted into helpers.
- Use kotests's collection.forAll/forOne/forNone to verify that collection elements matches property.
- In fixture setup specify only data relevant to the test-case.
- Avoid using `shouldBe <boolean const>` in verfication - prefer more specific assertions such as `shouldContain <substr>`, `shouldBeAfter <instant>`, etc.
- If data in the fixture is related – derive it instead of copying.
- Avoid technical terms or implementations details in tests names – prefer business and end user language.
- Try to name tests as specification of SUT's behavior or result property.
- Do not use non-deterministic randomness; use faker or data factories built on top of it.
- Do not use constants in tests, if specific value does not matter for the test-case.
- For fixture insertions prefer `*TestApi`s over `*HttpApi`s.
- Always add new test case methods to the end of the class.
- Do not use Thread.sleep to wait for events or async completion.
- Use Kotest `eventually` instead.
