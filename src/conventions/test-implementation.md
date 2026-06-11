# Test implementation

## Test case body

- In every new or changed test-case method, split the body with `// Given`, `// When`, and `// Then` comments.
- Put setup under `Given`, the action under `When`, and verification under `Then`.
- In command tests with a public observation API, prefer two public API actions: put the target command under `// When` and the observation operation under `// And when`.
- If command-returned data must be checked before observation, use `// When`, `// Then`, `// And when`, `// Then`.
- If observing the result requires several endpoint calls, render each observation endpoint under its own `// And when` followed by its own `// Then`.

## Fixture setup

- Each test case must set up its own fixture.
- Do not add per-test cleanup for shared fixture state.
  Use or extend the shared fixture setup/reset layer.
- Before adding cleanup for shared fixture state, inspect the selected test container's setup/reset path, including superclasses, test extensions, and called reset/init helpers.
- If that path already resets the state, rely on it.
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

## Test data

- In test prefer `!!` to null handling.
- Exact input values include literals, enum members, constants, codes, ids, dates, and names.
- Use exact input values only when the case or public contract names them.
- Treat named fixture constants and presets as exact input values.
- Otherwise encode the data role in a helper, factory, or fixture.
- Prefer generic role helpers over incidental named samples.

## Test doubles

Follow `./test-doubles.md`.

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
