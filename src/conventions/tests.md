# Tests conventions

## Fixture and helper structure

- Extract all fixture code from test case classes into helpers such as `*ObjectMother`, `*FixturePresets`, `*TestApi`, `*HttpApi`, `*Assertions`.
  Even if the current code contains helpers in the same file.
- Keep test case class files focused on test cases.
  Do not keep fixture setup or helper functions in the same file, including top-level helpers.
- Each test case must set up its own fixture.
- If fixture setup code duplication exceeds 3 lines, it may be extracted into helpers.
- In fixture setup specify only data relevant to the test-case.
- If data in the fixture is related, derive it instead of copying.

## Assertions and naming

- Use Kotest inspectors (`forAll`/`forOne`/`forNone`) to verify that collection elements match a property.
  See: https://kotest.io/docs/assertions/inspectors.html
- Avoid using `shouldBe <boolean const>` in verification.
  Prefer more specific assertions such as `shouldContain <substr>`, `shouldBeAfter <instant>`, etc.
- In verification block, including GWT-style `Then`, do not use magic constants for expected values.
  Do not put expected literals in `Then`.
  Bind each business value once in `Given` and reuse it in setup, request, and assertions.
  If exact value is not the point, assert a property.
  If an expected value is derived, compute it in `Given`.
  If a literal is unavoidable, declare it in `Given` with a short rationale comment.
- Avoid technical terms or implementations details in tests names.
  Prefer business and end user language.
- Try to name tests as specification of SUT's behavior or result property.

## Data and determinism

- In test prefer `!!` to null handling.
- Do not use non-deterministic randomness.
  Use faker or data factories built on top of it.
- Do not use constants in tests, if specific value does not matter for the test-case.

## APIs and ordering

- For fixture insertions prefer `*TestApi`s over `*HttpApi`s.
- Always add new test case methods to the end of the class.

## Waiting

- Do not use `Thread.sleep` to wait for events or async completion.
- Use Kotest `eventually` instead.
  See: https://kotest.io/docs/assertions/eventually.html
