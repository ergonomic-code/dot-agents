---
name: code-test-case
description: Convert cases written in `verification-check-format-v0.1` in `full` mode into Kotlin JUnit test code. Use when the input is a verification check artifact with `Feature`, `Rule`, `Example`, `Given`, `When`, `Then`, and `And`.
---

# Code Test Case

Read `../../conventions/code-implementation.md`.
Read `../../artifacts/verification-check-format-v0.1/ARTIFACT.md`.
Read `../../artifacts/verification-check-format-v0.1/references/mode-full.md`.
Read `../../artifacts/verification-check-format-v0.1/references/full-mode-checklist.md`.
Read `../../artifacts/verification-check-format-v0.1/references/source-reference.md`.
Read `../../conventions/tests.md`.
Read `references/response-contract-guard.md`.

Accept one `verification-check-format-v0.1` artifact in `full` mode, and an optional existing Kotlin JUnit 5 test file.
Ignore one optional source reference line immediately under each selected `Example` per `../../artifacts/verification-check-format-v0.1/references/source-reference.md`.
Default to coding exactly one test case, where one full `Example` block is one test case.
If the user did not explicitly select several examples, all examples, or a named multi-case set, code only the explicitly selected `Example`.
Before coding the first such case, check whether a test already matches it by display name, method name, Russian backticked name, or verified behavior.
Before announcing a plan, choosing a target test class, scanning fixtures, or editing code, resolve selected examples and run input preflight.
Input preflight must verify that each selected example is valid `verification-check-format-v0.1` full mode, including `Given` / `When` / `Then` and `Rule` obligation form.
If any selected `Rule` lacks a full `Example` with `Given` / `When` / `Then`, stop and report that `short` mode cannot be converted into test code.
If full-mode input places a source reference under `Rule` instead of under the matching `Example`, stop and report the invalid artifact shape.
If a selected example violates format but is repairable without changing behavior, stop and show the issue, the proposed corrected case header, and these choices: keep source wording as-is, use the proposed wording, or provide replacement wording.
If a selected example cannot be repaired without inventing behavior, stop and ask for corrected case text.
For HTTP API examples, before choosing or changing `*HttpApi` helpers, DTOs, schemas, or success assertions, read `030-api-new.adoc` or `030-api-new-ir.json` when present.
If such API artifact exists, use it as the target endpoint and response contract for the selected case.
Before editing code, map case data roles to helpers, factories, or fixtures; keep exact literals, enum members, constants, codes, ids, dates, and names in the test body only when named by the case or public contract.
If setup returns the required identifier or reference, use it directly; do not add a public read API call just to discover it.
Do not add production repositories, DAOs, services, clients, application contexts, or DI lookups to test case classes for setup or observation.
Put that access behind scoped `*TestApi` or `*FixturePresets`.
Inspect available fixture APIs for generic role helpers before choosing named constants or presets.
Before announcing a plan or editing code, if the test needs new or changed fixture helpers, check `../../conventions/test-fixture-architecture.md`:
name each `*TestApi` scope, keep cross-scope creation/linking in `*FixturePresets`, and create missing sibling `*TestApi` helpers instead of expanding an existing one.
Use generate mode when no `*.kt` test file is given.
Use update mode when the user points to one or explicitly asks to update existing tests.
Before choosing or announcing the target Kotlin test class or test action, read `../../conventions/test-container-selection.md`.
Infer the test kind from the explicit target class, explicit `Feature`, explicit target surface, and sibling test style.
For a component test, resolve the concrete component symbol and planned `When` receiver before editing.
If the component symbol or direct call shape cannot be resolved, stop instead of substituting a boundary client, controller, `*Api`, `*HttpApi`, or `*TestApi`.
Then scan existing sibling `*Test.kt` files for operation-level and variant-specific containers.
If the selected example is specific to one polymorphic input or output variant and a matching variant-specific test class exists, use that class even when the `Feature` names the shared operation or endpoint.
Before editing, compare selected `Rule` and `Example` anchors with the candidate class name and display name; if the anchors are narrower and sibling patterns support a narrower class, use or create that class instead.
Before announcing a plan or adding fixture cleanup, trace the candidate test class setup/reset path: superclass hooks, test extensions, and reset/init helpers they call.
If that path already resets the relevant state, rely on it.

Map one selected `Feature` to one class and one selected `Example` block to one `@Test` method.
Keep source order.
In update mode, bind one artifact `Feature` to one existing Kotlin test class instead of creating or renaming another class.
If several features must be applied to several existing test files, apply the skill sequentially, one `Feature` and one Kotlin test file per run.
If update mode input contains zero or multiple `Feature`s for one existing Kotlin test file, stop and report that update mode accepts exactly one `Feature` per run.

## Generate

- Build one Kotlin class per selected `Feature` and one test method per selected `Example` block.
- Return only Kotlin code.
- Implement bodies fully unless the user explicitly asked for skeletons or placeholders.
- Apply the loaded test conventions in generated test code too, including fixture/helper extraction and test-data abstraction rules.

## Update

- Read the existing file first and treat it as the baseline for package, imports, class/file name, constructor, fields, superclass, helpers, nested declarations, and working test code.
- Treat the existing Kotlin file as the container for exactly one artifact `Feature`.
- Match examples to existing methods by current `@DisplayName`, method name, Russian backticked name, and verified behavior.
- Preserve matched bodies and adapt minimally.
- Create a new method only when no existing implementation clearly matches.
- Remove a method only on explicit strict sync or when it is an obsolete managed example of the same artifact `Feature`.
- If mapping is ambiguous, stop and report it instead of deleting code or replacing bodies with placeholders.
- Keep unrelated declarations intact. Edit in place.

## Rendering

- Import `org.junit.jupiter.api.DisplayName` and `org.junit.jupiter.api.Test`.
- Apply `../../conventions/test-naming.md` for class `@DisplayName`, method `@DisplayName`, and `test_<slug>` names.
- Resolve class names from code symbols when possible. Use `UpperCamelCase`.
- For component tests, name the class from the resolved component symbol when available; otherwise for non-API features use `<Feature>Test`.
- For features starting with `Метод API`, resolve the handler by HTTP method and path. If it delegates to one `xxxOp`, use `XxxApiTest`; otherwise use the handler method name as `XxxApiTest`. If resolution is ambiguous, stop.
- In update mode, keep the existing class and file name unless the user explicitly asked to rename them.
- Use one blank line between methods.
- Use `@Nested` classes only when this matches the existing file style and keeps repeated rule or example names shorter.
- Preserve existing fixtures, assertions, helpers, and supporting code in update mode.
- Render every generated or updated test method body with `// Given`, `// When`, and `// Then` section comments.
- Extract any three or more consecutive assertions that verify one correspondence between two object groups into a named domain assertion.
- For read-after-write command tests with public observation, render the observation operation under `// And when`.
- If command-returned data must be checked before observation, render `// When`, `// Then`, `// And when`, `// Then`.
- If several observation endpoint calls are required, render each observation operation under its own `// And when` and place its assertions in the following `// Then`.
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
- In production code, allow only compile-only surface needed by the selected test.
- Keep production additions to required symbols, signatures, types, constructors, and fields used by the selected test.
- Do not add production fields, parameters, enum values, or types not used by the selected test.
- Put `TODO` inside newly added production method bodies unless the body is a trivial constructor, accessor, or data holder.
- Do not add production behavior, control flow, persistence, external integrations, endpoint contracts, validation rules, migrations, configuration, generated/static API docs, controllers, services, repositories, or clients.
- If tests require production behavior to compile or pass, stop and report the blocker instead of changing production behavior.
- By default, after implementing a new or aligned case, the test should compile. The test may still fail for any reason until production behavior is aligned.

Before finishing, read `../../conventions/test-implementation-checklist.md`, fix any failed item, and check: default scope produced exactly one example unless the user explicitly requested more, one class per selected `Feature`, one method per selected `Example`, fixture helper boundaries follow `../../conventions/test-fixture-architecture.md`, naming follows `../../conventions/test-naming.md`, new structured resources or schemas reuse or extract shared definitions instead of duplicating equivalent definitions, new or aligned tests compile, generate mode returns only Kotlin, and update mode accepts exactly one `Feature` per run and preserves the existing container code while editing in place.
