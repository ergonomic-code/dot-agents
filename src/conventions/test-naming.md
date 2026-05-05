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

- For formal case artifacts, write class `@DisplayName` from raw `Feature` text without `Feature:`.
- Copy `Rule` and `Scenario` header text verbatim after removing only the keyword prefix, one separator colon, and surrounding whitespace.
- Do not paraphrase, normalize, translate, shorten, re-punctuate, or inflect `Rule` or `Scenario` text in display names.
- For one-scenario rules, set method `@DisplayName` to `<rule> :: <scenario>` unless the scenario text only repeats the rule.
- For multi-scenario rules with `@Nested`, put the rule text into nested class `@DisplayName` and the scenario text into method `@DisplayName`.
- Use the exact separator ` :: `.
- If the source `Rule` or `Scenario` already contains `::`, stop and report ambiguity.
- For one-scenario rules, summarize the rule in `<slug>`.
- For multi-scenario rules, summarize the scenario in `<slug>`.
