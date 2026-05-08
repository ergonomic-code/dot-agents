---
name: code-test-case
description: Convert cases written in `verification-check-format-v0.1` in `full` mode into Kotlin JUnit test code. Use when the input is a verification check artifact with `SUT`, `Check`, optional `Variant`, `Given`, `When`, `Then`, and `And`, and you either need new Kotlin tests or need to update an existing `*Test.kt` file to match it without losing the surrounding test code.
---

# Code Test Case

Read `../../artifacts/verification-check-format-v0.1/ARTIFACT.md`.
Read `../../artifacts/verification-check-format-v0.1/references/mode-full.md`.
Read `../../artifacts/verification-check-format-v0.1/references/source-reference.md`.
Read `../../conventions/tests.md`.
Read `../../conventions/test-naming.md`.

Accept one `verification-check-format-v0.1` artifact in `full` mode and an optional existing Kotlin JUnit 5 test file.
Ignore one optional source reference line immediately under each `Check` or after its `Variant` per `../../artifacts/verification-check-format-v0.1/references/source-reference.md`.
Default to coding exactly one test case, where one full `Check` block is one test case.
If the user did not explicitly select several checks, all checks, or a named multi-case set, code only the explicitly selected `Check`; if none is selected, code the first not-yet-implemented `Check` in source order, or the first `Check` if implementation status is unknown.
Do not treat a feature directory, artifact file, progress checklist, or pending-case list as an explicit request to code multiple test cases.
Before coding, resolve selected checks and verify each selected `Check` has `Given` / `When` / `Then` steps.
If any selected `Check` lacks them, stop and report that `short` mode cannot be converted into test code.
Before editing code, map check data roles to helpers, factories, or fixtures; keep exact literals, enum members, constants, codes, ids, dates, and names in the test body only when named by the case or public contract.
Inspect available fixture APIs for generic role helpers before choosing named constants or presets.
Use generate mode when no `*.kt` test file is given.
Use update mode when the user points to one or explicitly asks to update existing tests.
Before choosing or announcing the target Kotlin test class, read `../../conventions/test-container-selection.md`.
Then scan existing sibling `*Test.kt` files for operation-level and variant-specific containers.
If the selected check is specific to one polymorphic input or output variant and a matching variant-specific test class exists, use that class even when the `SUT` names the shared operation or endpoint.

Map one selected `SUT` to one class and one selected `Check` block to one `@Test` method.
Keep source order.
In update mode, bind one artifact `SUT` to one existing Kotlin test class instead of creating or renaming another class.
If several SUTs must be applied to several existing test files, apply the skill sequentially, one SUT and one Kotlin test file per run.
If update mode input contains zero or multiple `SUT`s for one existing Kotlin test file, stop and report that update mode accepts exactly one SUT per run.

## Generate

- Build one Kotlin class per selected SUT and one test method per selected check block.
- Return only Kotlin code.
- Implement bodies fully unless the user explicitly asked for skeletons or placeholders.
- Apply the loaded test conventions in generated test code too, including fixture/helper extraction and test-data abstraction rules.

## Update

- Read the existing file first and treat it as the baseline for package, imports, class/file name, constructor, fields, superclass, helpers, nested declarations, and working test code.
- Treat the existing Kotlin file as the container for exactly one artifact `SUT`.
- Match checks to existing methods by current `@DisplayName`, method name, Russian backticked name, and verified behavior.
- Preserve matched bodies and adapt minimally.
- Create a new method only when no existing implementation clearly matches.
- Remove a method only on explicit strict sync or when it is an obsolete managed variant of the same artifact SUT.
- If mapping is ambiguous, stop and report it instead of deleting code or replacing bodies with placeholders.
- Keep unrelated declarations intact. Edit in place.

## Rendering

- Import `org.junit.jupiter.api.DisplayName` and `org.junit.jupiter.api.Test`.
- Apply `../../conventions/test-naming.md` for class `@DisplayName`, method `@DisplayName`, and `test_<slug>` names.
- Resolve class names from code symbols when possible. Use `UpperCamelCase`.
- For non-API SUTs use `<SUT>Test`.
- For SUTs starting with `Метод API`, resolve the handler by HTTP method and path. If it delegates to one `xxxOp`, use `XxxApiTest`; otherwise use the handler method name as `XxxApiTest`. If resolution is ambiguous, stop.
- In update mode, keep the existing class and file name unless the user explicitly asked to rename them.
- Use one blank line between methods.
- Use `@Nested` classes only when this matches the existing file style and keeps repeated check or variant names shorter.
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

Follow `../../conventions/test-naming.md`.
For this skill, use the formal case mapping rules.

## Output Discipline

- Keep new or newly aligned cases strict even if they fail against current production code.
- Do not weaken assertions only to keep tests green unless the user explicitly asked for that.
- In update mode, do not replace implemented bodies with placeholder comments.
- In production code, allow only DTO adjustments needed for test compilation.
- Do not edit any non-DTO production artifact under this skill unless the user explicitly requested broader production-code changes.
- This ban includes business logic, control flow, persistence, external integrations, endpoint contracts, validation rules, migrations, configuration, generated/static API docs, controllers, services, repositories, and clients.
- Keep DTO adjustments compile-oriented and minimal: field/constructor/signature alignment only, without semantic behavior changes.
- If tests require non-DTO production changes to compile or pass, stop and report the blocker instead of changing production code.
- By default, after implementing a new or aligned case, the test should compile. The test may still fail for any reason until production behavior is aligned.

Before finishing, read `../../conventions/test-implementation-checklist.md`, fix any failed item, and check: default scope produced exactly one check unless the user explicitly requested more, one class per selected SUT, one method per selected check, naming follows `../../conventions/test-naming.md`, new or aligned tests compile, generate mode returns only Kotlin, and update mode accepts exactly one SUT per run and preserves the existing container code while editing in place.
