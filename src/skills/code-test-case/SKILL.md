---
name: code-test-case
description: Convert cases written in `formal-requirements-format-v0.1` in `full` mode into Kotlin JUnit 5 test code. Use when the input is a Gherkin-like artifact with `Feature`, `Rule`, `Scenario`, `Given`, `When`, `Then`, and `And`, and you either need new Kotlin tests or need to update an existing `*Test.kt` file to match the described cases without losing the surrounding test code.
---

# Code Test Case

Read `../../artifacts/formal-requirements-format-v0.1/ARTIFACT.md`.
Read `../../artifacts/formal-requirements-format-v0.1/references/mode-full.md`.
Read `../../artifacts/formal-requirements-format-v0.1/references/source-reference.md`.
Read `../../conventions/tests.md`.

Accept one `formal-requirements-format-v0.1` artifact in `full` mode and an optional existing Kotlin JUnit 5 test file.
Ignore one optional source reference line immediately under each `Scenario` per `../../artifacts/formal-requirements-format-v0.1/references/source-reference.md`.
Default to coding exactly one test case, where one `Scenario` is one test case.
If the user did not explicitly select several scenarios, all scenarios, or a named multi-case set, code only the explicitly selected `Scenario`; if none is selected, code the first not-yet-implemented `Scenario` in source order, or the first `Scenario` if implementation status is unknown.
Do not treat a feature directory, artifact file, progress checklist, or pending-case list as an explicit request to code multiple test cases.
Before coding, resolve selected scenarios and verify each selected `Scenario` has `Given` / `When` / `Then` steps.
If any selected `Scenario` lacks them, stop and report that `short` mode cannot be converted into test code.
Before editing code, map scenario data roles to helpers, factories, or fixtures; keep exact literals, enum members, constants, codes, ids, dates, and names in the test body only when named by the case or public contract.
Inspect available fixture APIs for generic role helpers before choosing named constants or presets.
Use generate mode when no `*.kt` test file is given. Use update mode when the user points to one or explicitly asks to update existing tests.

Map one selected `Feature` to one class and one selected `Scenario` to one `@Test` method. Keep source order.
In update mode, bind one artifact feature to one existing Kotlin test class instead of creating or renaming another class.
If several features must be applied to several existing test files, apply the skill sequentially, one feature and one Kotlin test file per run.
If update mode input contains zero or multiple `Feature`s for one existing Kotlin test file, stop and report that update mode accepts exactly one feature per run.

## Generate

- Build one Kotlin class per selected feature and one test method per selected scenario.
- Return only Kotlin code.
- Implement bodies fully unless the user explicitly asked for skeletons or placeholders.
- Apply the loaded test conventions in generated test code too, including fixture/helper extraction and test-data abstraction rules.

## Update

- Read the existing file first and treat it as the baseline for package, imports, class/file name, constructor, fields, superclass, helpers, nested declarations, and working test code.
- Treat the existing Kotlin file as the container for exactly one artifact `Feature`.
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
- Use `@Nested` classes for multi-scenario rules when this keeps method display names shorter and matches the existing file style.
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

- Do not use Kotlin backticked test method names.
- Always put human-readable case text into method `@DisplayName`.
- Copy `Rule` and `Scenario` header text verbatim after removing only the keyword prefix, one separator colon, and surrounding whitespace.
- Do not paraphrase, normalize, translate, shorten, re-punctuate, or inflect `Rule` or `Scenario` text in display names.
- For one-scenario rules, set method `@DisplayName` to `<rule> :: <scenario>` unless the scenario text only repeats the rule.
- For multi-scenario rules with `@Nested`, put the rule text into nested class `@DisplayName` and the scenario text into method `@DisplayName`.
- Use the exact separator ` :: `. If the source `Rule` or `Scenario` already contains `::`, stop and report ambiguity.
- Name test methods as `test_<slug>`.
- Build `<slug>` as a lowercase ASCII `snake_case` summary of `2`-`5` words.
- For one-scenario rules, summarize the rule in `<slug>`.
- For multi-scenario rules, summarize the scenario in `<slug>`.
- If two generated method names collide, extend the slug without changing display text.

## Output Discipline

- Keep new or newly aligned cases strict even if they fail against current production code.
- Do not weaken assertions only to keep tests green unless the user explicitly asked for that.
- In update mode, do not replace implemented bodies with placeholder comments.
- In production code, allow only DTO adjustments needed for test compilation.
- Do not change production business logic, control flow, persistence, external integrations, endpoint contracts, or validation rules under this skill.
- Keep DTO adjustments compile-oriented and minimal: field/constructor/signature alignment only, without semantic behavior changes.
- If tests require non-DTO production changes to compile or pass, stop and report the blocker instead of changing production code.
- By default, after implementing a new or aligned case, the test should compile. The test may still fail for any reason until production behavior is aligned.

Before finishing, read `../../conventions/test-implementation-checklist.md`, fix any failed item, and check: default scope produced exactly one scenario unless the user explicitly requested more, one class per selected feature, one method per selected scenario, class `@DisplayName` stripped of `Feature:`, methods are named `test_<slug>`, display names copy `Rule` and `Scenario` text verbatim, new or aligned tests compile, generate mode returns only Kotlin, and update mode accepts exactly one feature per run and preserves the existing container code while editing in place.
