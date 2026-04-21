---
name: code-test-case
description: Convert cases written in `formal-requirements-format-v0.1` in `full` mode into Kotlin JUnit 5 test code. Use when the input is a Gherkin-like artifact with `Feature`, `Rule`, `Scenario`, `Given`, `When`, `Then`, and `And`, and you either need new Kotlin tests or need to update an existing `*Test.kt` file to match the described cases without losing the surrounding test code.
---

# Code Test Case

Read `../../artifacts/formal-requirements-format-v0.1/ARTIFACT.md`.
Read `../../artifacts/formal-requirements-format-v0.1/references/mode-full.md`.
Read `../../conventions/tests.md`. 

Accept one `formal-requirements-format-v0.1` artifact in `full` mode and an optional existing Kotlin JUnit 5 test file.
If any `Scenario` has no `Given` / `When` / `Then` steps, stop and report that `short` mode cannot be converted into test code.
Use generate mode when no `*.kt` test file is given. Use update mode when the user points to one or explicitly asks to update existing tests.

Map one `Feature` to one class and one `Scenario` to one `@Test` method. Keep source order. In update mode, bind the artifact feature to the existing class instead of creating or renaming another class.

## Generate

- Build one Kotlin class per feature and one test method per scenario.
- Return only Kotlin code.
- Implement bodies fully unless the user explicitly asked for skeletons or placeholders.
- Apply the loaded test conventions in generated test code too, including fixture/helper extraction and test-data abstraction rules.

## Update

- Read the existing file first and treat it as the baseline for package, imports, class/file name, constructor, fields, superclass, helpers, nested declarations, and working test code.
- Match scenarios to existing methods by current `@DisplayName`, method name, Russian backticked name, and verified behavior.
- Preserve matched bodies and adapt minimally.
- Create a new method only when no existing implementation clearly matches.
- Remove a method only on explicit strict sync or when it is an obsolete managed variant of the same artifact feature.
- If mapping is ambiguous, stop and report it instead of deleting code or replacing bodies with placeholders.
- Keep unrelated declarations intact. Edit in place.

## Rendering

- Import `org.junit.jupiter.api.DisplayName` and `org.junit.jupiter.api.Test`.
- Write class `@DisplayName` from the raw feature text without `Feature:`.
- Resolve class names from code symbols when possible. Use `UpperCamelCase`.
- For non-API features use `<SUT>Test`.
- For features starting with `Метод API`, resolve the handler by HTTP method and path. If it delegates to one `xxxOp`, use `XxxApiTest`; otherwise use the handler method name as `XxxApiTest`. If resolution is ambiguous, stop.
- In update mode, keep the existing class and file name unless the user explicitly asked to rename them.
- Use one blank line between methods.
- Preserve existing fixtures, assertions, helpers, and supporting code in update mode.
- If the user explicitly asked for placeholders or skeletons, use only:

```kotlin
{
    // Given
    // When
    // Then
}
```

## Method Names

- Prefer a Kotlin backticked method name over method `@DisplayName`.
- Add method `@DisplayName` only when the artifact-based backticked name would not compile, typically because of length or invalid identifier form. Then keep a shorter compilable method name derived from the same wording.
- For one-scenario rules, use the `Rule` text as the method name unless the `Scenario` adds material wording needed for clarity or uniqueness.
- For multi-scenario rules, use the exact form `<rule> :: <scenario>`.
- Keep the `Rule` fragment identical across methods of one multi-scenario rule and keep the `Scenario` fragment as close as possible to the source scenario text.
- Use the exact separator ` :: `. If the source `Rule` or `Scenario` already contains `::`, stop and report ambiguity.
- Remove only wrappers like `Feature:`, `Rule:`, and `Scenario:`.
- If two generated backticked names still collide, extend the source scenario wording instead of translating or changing style.

## Rule Constants

- Do not create rule constants for naming.
- Add a private companion object only when fallback method `@DisplayName` needs shared rule constants.
- If used, keep the rule text itself as both constant name and value.
- Add `@Suppress("ConstPropertyName")` only when such constants exist.

## Output Discipline

- Keep new or newly aligned cases strict even if they fail against current production code.
- Do not weaken assertions only to keep tests green unless the user explicitly asked for that.
- In update mode, do not replace implemented bodies with placeholder comments.
- In production code, allow only DTO adjustments needed for test compilation.
- Do not change production business logic, control flow, persistence, external integrations, endpoint contracts, or validation rules under this skill.
- Keep DTO adjustments compile-oriented and minimal: field/constructor/signature alignment only, without semantic behavior changes.
- If tests require non-DTO production changes to compile or pass, stop and report the blocker instead of changing production code.
- By default, after implementing a new or aligned case, the test should compile. The test may still fail for any reason until production behavior is aligned.

Before finishing, check: the input artifact is `full` mode, one class per feature, one method per scenario, class `@DisplayName` stripped of `Feature:`, multi-scenario methods use `<rule> :: <scenario>`, fallback method `@DisplayName` appears only when needed, new or aligned tests compile, generate mode returns only Kotlin, and update mode preserves the existing container code while editing in place.
