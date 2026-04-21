# Test implementation

## Fixture setup

- Each test case must set up its own fixture.
- If fixture setup code duplication exceeds 3 lines, it may be extracted into helpers.
- In fixture setup specify only data relevant to the test-case.
- If data in the fixture is related, derive it instead of copying.

## Assertions

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

## Test naming

- Avoid technical terms or implementations details in tests names.
  Prefer business and end user language.
- Try to name tests as specification of SUT's behavior or result property.

## Test data

- In test prefer `!!` to null handling.
- Do not use constants in tests, if specific value does not matter for the test-case.
- Represent non-essential test inputs by their role, not by an incidental sample value.
- Prefer semantic helpers, factories, or fixtures that encode the role of the value instead of picking a concrete enum member, code, id, date, or name in the test body.
- Keep a concrete value only when the rule, scenario, or public contract depends on that exact value.

## Determinism

- Do not use non-deterministic randomness.
  Use faker or data factories built on top of it.

## Test class ordering

- Always add new test case methods to the end of the class.
- Do not insert a new test case into the middle of an existing class, even if it seems thematically closer there.

## Waiting

- Do not use `Thread.sleep` to wait for events or async completion.
- Use Kotest `eventually` instead.
  See: https://kotest.io/docs/assertions/eventually.html
