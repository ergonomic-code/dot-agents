---
keywords:
  - tests
  - naming
---

# Test naming

Use surrounding tests when a rule below requires a repository pattern and otherwise only after these rules to preserve local mechanics, imports, annotations, and report style.

## Containers

- Choose the technical container name only after resolving the test kind and SUT.
- For an HTTP boundary, use the exact class name of the single application operation invoked by the selected endpoint as `<OperationName>`; when it invokes zero or several operations, use its handler method name with the first character uppercased and the rest unchanged.
  Name the container `<OperationName>ApiTest`.
- For another boundary, derive the container name from its external operation identifier and the repository's established boundary pattern; stop when no unambiguous pattern exists.
- For a component SUT recorded as `<ClassName>`, choose or create `<ClassName>Test`.
- For a component SUT recorded as `<ClassName>.<methodName>`, choose or create `<ClassName>_<camelCasedMethodName>`.
- Name a class-based unit container `<TargetClassName>Test`.
- Name a top-level pure function container `<PascalCasedFunctionName>Test`.
- For a variant-qualified SUT, reuse only a unique existing container matching the selected test kind, unqualified SUT, and exact variant, preserving its actual file and nesting and skipping container/path derivation below; stop if several match, or apply the kind rule to the unqualified SUT if none match.
- Resolve the code owner of the SUT uniquely: the referenced class or function for component and unit tests, and the code entry point matching the external operation identifier for boundary tests.
- Put a new container in the code owner's module, corresponding test source set, and package; use the repository's established test source set for the selected kind when the module has more than one, and stop when it is not unique.
- If the derived container already exists at that location, add the case to it; otherwise create its matching file there.

## Human names

- Put human-readable class and case text into `@DisplayName` when the test framework supports it.
- Write only display text in the configured `artifact_language`: class and case `@DisplayName`, plus parameterized test display name text.
- Keep class, file, and method identifiers in the repository's technical naming style, except for new formal case methods mapped below or explicitly requested renames.
- For existing Kotlin test files, keep the existing class and file name unless the user explicitly asks to rename technical identifiers.
- Name class `@DisplayName` from the matching verification-check `Feature` when available.
- Otherwise name it by the behavior container, feature, operation, or API method and append the SUT reference according to the loaded feature-naming rules.
- For component tests, the human-readable part may name the behavior surface when the parenthesized SUT reference identifies the resolved component.
- Name case `@DisplayName` as a continuation of the class `@DisplayName` that starts with a lowercase letter and specifies observable behavior or a result property.
- For Russian case names, use `должен` or `должна`.
- Put any input or state condition either before the obligation or after the required output.
- Use business, end-user, and public-contract language when it expresses the obligation precisely.
- For technical contract obligations, keep the technical term needed to name the behavior.
- Avoid incidental implementation details.
- For data-driven tests, name the case by the common invariant and put the varying input axis into the parameterized test display name.

## Technical method names

- For case methods, use `test_<slug>`.
- Outside formal mapping, build `<slug>` as a lowercase ASCII `snake_case` summary of `2`-`5` words.
- stop when such method name already exists.

## Formal case mapping

- Use this section when coding from formal case artifacts, aligning existing tests to formal case names, or preserving already formal test anchors.
- For existing tests without a formal artifact, first recover `Feature`, `Rule`, and optional named `Example` from explicit anchors, source references, enclosing group names, or verified behavior.
- After recovery, treat recovered `Feature`, `Rule`, and `Example` as source headers for this section.
- If formal mapping applies and `Feature` or `Rule` cannot be recovered confidently, stop and report the missing anchor.
- If `Rule` does not start with a lowercase letter, stop and report that it cannot be copied verbatim into a conforming case `@DisplayName`.
- For formal case artifacts, write class `@DisplayName` from raw `Feature` text without `Feature:`.
- Copy `Rule` header text verbatim after removing only the keyword prefix, one separator colon, and surrounding whitespace.
- For a non-parameterized, non-property named `Example`, copy its header text by the same rule.
- Do not paraphrase, normalize, translate, shorten, re-punctuate, or inflect `Rule` or `Example` text in display names.
- For an eligible parameterized set, set method `@DisplayName` to `<rule>` and use each exact named `Example` header as its invocation display name.
- For a property form, set method `@DisplayName` to `<rule>` and treat its named `Example` only as generated-input-domain metadata.
- If `Example` is unnamed, absent, or empty, set method `@DisplayName` to `<rule>`.
- If a non-parameterized, non-property `Example` is named, set method `@DisplayName` to `<rule> :: <example>`.
- Use `@Nested` only when the existing file already groups related cases this way.
- Use the exact separator ` :: `.
- If the source `Rule` or named `Example` already contains `::`, stop and report ambiguity.
- For `strengthen` or `extend-parameterized`, preserve the recorded method identifier instead of deriving a new name.
