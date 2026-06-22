# Test naming

Read this file before scanning existing tests for naming examples when the task asks to name, rename, or align a test class, case, method, or `@DisplayName`.
Use surrounding tests only after these rules to preserve local mechanics, imports, annotations, and report style.

## Human names

- Put human-readable class and case text into `@DisplayName` when the test framework supports it.
- Write only display text in the configured `artifact_language`: class and case `@DisplayName`, plus parameterized test display name text.
- Keep class, file, and method identifiers, including Kotlin backticked method names and `test_<slug>`, in the repository's technical naming style unless the user explicitly asks to rename identifiers outside `@DisplayName`.
- For existing Kotlin test files, keep the existing class and file name unless the user explicitly asks to rename technical identifiers.
- Name class `@DisplayName` by the behavior container, feature, operation, or API method under test.
- For endpoint test classes from `Feature` starting with `Метод API`, name class `@DisplayName` as `Метод API <человеческое название метода> (<HTTP method> <path>)`.
- For component tests, class `@DisplayName` may name the behavior surface instead of the component symbol when the target component is resolved elsewhere.
- Name case `@DisplayName` as a specification of observable behavior or result property.
- For Russian case names, use `должен` or `должна`.
- Put any input or state condition either before the obligation or after the required output.
- Use business, end-user, and public-contract language when it expresses the obligation precisely.
- For technical contract obligations, keep the technical term needed to name the behavior.
- Avoid incidental implementation details.
- For data-driven tests, name the case by the common invariant and put the varying input axis into the parameterized test display name.

## Technical method names

- For new or newly aligned JUnit case methods, use `test_<slug>` instead of Kotlin backticked names.
- Build `<slug>` as a lowercase ASCII `snake_case` summary of `2`-`5` words.
- If method names collide, extend the slug without changing display text.

## Formal case mapping

- Use this section when coding from formal case artifacts, aligning existing tests to formal case names, or preserving already formal test anchors.
- For existing tests without a formal artifact, first recover `Feature`, `Rule`, and optional named `Example` from explicit anchors, source references, enclosing group names, or verified behavior.
- After recovery, treat recovered `Feature`, `Rule`, and `Example` as source headers for this section.
- If formal mapping applies and `Feature` or `Rule` cannot be recovered confidently, stop and report the missing anchor.
- For formal case artifacts, write class `@DisplayName` from raw `Feature` text without `Feature:`.
- Copy `Rule` and optional named `Example` header text verbatim after removing only the keyword prefix, one separator colon, and surrounding whitespace.
- Do not paraphrase, normalize, translate, shorten, re-punctuate, or inflect `Rule` or `Example` text in display names.
- If `Example` is unnamed, absent, or empty, set method `@DisplayName` to `<rule>`.
- If `Example` is named, set method `@DisplayName` to `<rule> :: <example>`.
- Use `@Nested` only when the existing file already groups related cases this way.
- Use the exact separator ` :: `.
- If the source `Rule` or named `Example` already contains `::`, stop and report ambiguity.
- If `Example` is unnamed, absent, or empty, summarize the rule in `<slug>`.
- If `Example` is named, summarize the rule and example in `<slug>`.
