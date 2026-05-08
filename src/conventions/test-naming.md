# Test naming

Read this file before scanning existing tests for naming examples when the task asks to name, rename, or align a test class, case, method, or `@DisplayName`.
Use surrounding tests only after these rules to preserve local mechanics, imports, annotations, and report style.

## Human names

- Put human-readable class and case text into `@DisplayName` when the test framework supports it.
- For existing Kotlin test files, keep the existing class and file name unless the user explicitly asks to rename technical identifiers.
- Name class `@DisplayName` by the behavior container, feature, operation, or API method under test.
- Name case `@DisplayName` as a specification of observable behavior or result property.
- Use business, end-user, and public-contract language.
- Avoid technical terms and implementation details.
- For data-driven tests, name the case by the common invariant and put the varying input axis into the parameterized test display name.

## Technical method names

- For new or newly aligned JUnit case methods, use `test_<slug>` instead of Kotlin backticked names.
- Build `<slug>` as a lowercase ASCII `snake_case` summary of `2`-`5` words.
- If method names collide, extend the slug without changing display text.

## Formal case mapping

- Use this section when coding from formal case artifacts, aligning existing tests to formal case names, or preserving already formal test anchors.
- For existing tests without a formal artifact, first recover `SUT`, `Check`, and optional `Variant` from explicit anchors, source references, enclosing group names, or verified behavior.
- After recovery, treat recovered `SUT`, `Check`, and `Variant` as source headers for this section.
- If formal mapping applies and `SUT` or `Check` cannot be recovered confidently, stop and report the missing anchor.
- For formal case artifacts, write class `@DisplayName` from raw `SUT` text without `SUT:`.
- Copy `Check` and optional `Variant` header text verbatim after removing only the keyword prefix, one separator colon, and surrounding whitespace.
- Do not paraphrase, normalize, translate, shorten, re-punctuate, or inflect `Check` or `Variant` text in display names.
- If `Variant` is absent, set method `@DisplayName` to `<check>`.
- If `Variant` is present, set method `@DisplayName` to `<check> :: <variant>`.
- Use `@Nested` only when the existing file already groups related cases this way.
- Use the exact separator ` :: `.
- If the source `Check` or `Variant` already contains `::`, stop and report ambiguity.
- If `Variant` is absent, summarize the check in `<slug>`.
- If `Variant` is present, summarize the check and variant in `<slug>`.
