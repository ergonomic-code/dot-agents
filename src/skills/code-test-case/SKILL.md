---
name: code-test-case
description: Convert cases written in `verification-check-format-v0.1` in `full` mode into Kotlin JUnit test code and, for repository-backed use, verify whether the selected test is expected red or already green. Use when the input is a verification check artifact with `Feature`, `Rule`, `Example`, `Given`, `When`, `Then`, and `And`.
---

# Code Test Case

Read `../../conventions/code-implementation.md`.
Read `../../artifacts/verification-check-format-v0.1/ARTIFACT.md`.
Read `../../artifacts/verification-check-format-v0.1/references/mode-full.md`.
Read `../../artifacts/verification-check-format-v0.1/references/full-mode-checklist.md`.
Read `../../artifacts/verification-check-format-v0.1/references/source-reference.md`.
Read `../../conventions/tests.md`.
Read `references/response-contract-guard.md`.

Accept one `verification-check-format-v0.1` artifact in `full` mode, and an optional existing Kotlin JUnit 5 test file or explicit target path for a new test file.
Ignore one optional source reference line immediately under each selected `Example` per `../../artifacts/verification-check-format-v0.1/references/source-reference.md`.
Default to coding exactly one test case, where one full `Example` block is one test case.
Exception: when one `Rule` has a complete finite set of named `Example`s differing only by one input-or-context axis and its expected outcome, code that set as one parameterized test.
Otherwise, if the user did not explicitly select several examples, all examples, or a named multi-case set, code only the explicitly selected `Example`.
Before coding the first such case, check whether a test already matches it by display name, method name, Russian backticked name, or verified behavior.
Before announcing a plan, choosing a target test class, scanning fixtures, or editing code, resolve selected examples and run input preflight.
Input preflight must verify that each selected example is valid `verification-check-format-v0.1` full mode, including `Given` / `When` / `Then` and `Rule` obligation form.
If a selected `Feature` is provisional and lacks its parenthesized SUT reference, stop before choosing a target or coding and report that `$align-required-design` must materialize it.
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
Use update mode when the resolved target `*.kt` test file exists.
Use generate mode otherwise.
Before choosing or announcing the target Kotlin test class or test action, read `../../conventions/test-container-selection.md`.
Infer the test kind from the explicit target class, explicit `Feature`, explicit target surface, and sibling test style.
For a component test, resolve the concrete component symbol and planned `When` receiver before editing.
If the component symbol or direct call shape cannot be resolved, stop instead of substituting a boundary client, controller, `*Api`, `*HttpApi`, or `*TestApi`.
Then scan existing sibling `*Test.kt` files for operation-level and variant-specific containers.
If the selected example is specific to one polymorphic input or output variant and a matching variant-specific test class exists, use that class even when the `Feature` names the shared operation or endpoint.
Before editing, compare selected `Rule` and `Example` anchors with the candidate class name and display name; if the anchors are narrower and sibling patterns support a narrower class, use or create that class instead.
Before announcing a plan or adding fixture cleanup, trace the candidate test class setup/reset path: superclass hooks, test extensions, and reset/init helpers they call.
If that path already resets the relevant state, rely on it.

Map one selected `Feature` to one class.
Map one selected `Example` block to one `@Test` method, or one eligible parameterized set to one `@ParameterizedTest` method.
For a parameterized set, make each argument row carry the exact named `Example` header for the invocation display name, the varying axis, and the expected outcome.
Keep source order.
In update mode, bind one artifact `Feature` to one existing Kotlin test class instead of creating or renaming another class.
If several features must be applied to several existing test files, apply the skill sequentially, one `Feature` and one Kotlin test file per run.
If update mode input contains zero or multiple `Feature`s for one existing Kotlin test file, stop and report that update mode accepts exactly one `Feature` per run.

## Generate

- Build one Kotlin class per selected `Feature` and one test method per selected `Example` block or eligible parameterized set.
- By default, return only Kotlin code.
- When an invoking workflow supplies an explicit target path and requires repository changes, write the generated test to that path and return the path to the caller.
- Keep other test-support and compile-only production edits within the write set granted by the invoking workflow and this skill's Output Discipline.
- Implement bodies fully unless the user explicitly asked for skeletons or placeholders.
- Apply the loaded test conventions in generated test code too, including fixture/helper extraction and test-data abstraction rules.

## Update

- Read the existing file first and treat it as the baseline for package, imports, class/file name, constructor, fields, superclass, helpers, nested declarations, and working test code.
- Treat the existing Kotlin file as the container for exactly one artifact `Feature`.
- Match examples to existing methods by current `@DisplayName`, method name, Russian backticked name, and verified behavior.
- For an eligible parameterized set, match all member examples together, consolidate matching managed methods into one `@ParameterizedTest`, and treat superseded methods as obsolete managed examples of the same artifact `Feature`.
- Preserve matched bodies and adapt minimally.
- Create a new method only when no existing implementation clearly matches.
- Remove a method only on explicit strict sync or when it is an obsolete managed example of the same artifact `Feature`.
- If mapping is ambiguous, stop and report it instead of deleting code or replacing bodies with placeholders.
- Keep unrelated declarations intact. Edit in place.

## Rendering

- Import `org.junit.jupiter.api.DisplayName`.
- Import `org.junit.jupiter.api.Test` when rendering an ordinary test.
- For an eligible parameterized set, import `org.junit.jupiter.params.ParameterizedTest` and the narrowest suitable argument source used by local tests.
- Configure `@ParameterizedTest` to use the carried exact `Example` header as the invocation display name.
- Apply `../../conventions/test-naming.md` for class `@DisplayName`, method `@DisplayName`, and `test_<slug>` names.
- Resolve class names from code symbols when possible. Use `UpperCamelCase`.
- For component tests, name the class from the resolved component symbol when available; otherwise for non-API features use `<Feature>Test`.
- For features starting with `Метод API`, resolve the handler by HTTP method and path. If it delegates to one `xxxOp`, use `XxxApiTest`; otherwise use the handler method name as `XxxApiTest`. If resolution is ambiguous, stop.
- In update mode, keep the existing class and file name unless the user explicitly asked to rename them.
- Use one blank line between methods.
- Use `@Nested` classes only when this matches the existing file style and keeps repeated rule or example names shorter.
- Preserve existing fixtures, assertions, helpers, and supporting code in update mode.
- Render every generated or updated test method body with `// Given`, `// When`, and `// Then` section comments.
- Extract three or more consecutive assertions that verify one correspondence into a named domain assertion only when it is stateless and receives the already observed domain values.
- If reusable verification must obtain state, put it in a `verify...` method of the scoped `*TestApi`; for several scopes, call each scoped verification separately instead of creating a cross-scope assertion data holder.
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

## Behavior State Verification

For repository-backed generate or update mode, after coding or confirming alignment of the selected case:

1. Resolve the narrowest command that compiles the selected test.
2. Compile the selected test.
3. Execute the exact selected test case.
4. Compare the observed result with the selected `Rule` and `Then`.

Return `status: complete` with exactly one outcome:

- `outcome: expected-red` only when the test compiled, executed, and failed because the selected behavior is missing;
- `outcome: already-green` when the selected case passes.

Return `status: pending` only when execution evidence is incomplete or a verified transient environmental failure can be retried without file changes.
Return `status: blocked` for a compilation failure, fixture failure, unrelated assertion, non-transient environmental failure, or any other failure not attributable to the selected missing behavior.
Report the compilation command, execution command, exact executed case, observed result, and its connection to the selected behavior.
Do not weaken or otherwise edit the test to manufacture expected red.
This verification does not apply to standalone generate mode without a repository target path; return only Kotlin code and do not claim a behavior state.

## Output Discipline

- Keep new or newly aligned cases strict even if they fail against current production code.
- Do not weaken assertions only to keep tests green unless the user explicitly asked for that.
- In update mode, do not replace implemented bodies with placeholder comments.
- In production code, allow only compile-only surface needed by the selected test.
- Before adding compile-only production surface, verify that the selected component symbol and direct call shape remain the test's system under test (SUT).
- Do not add a sibling overload, method, class, or helper as a substitute for an existing SUT only to pass a new test input.
- If the selected case needs a new input for an existing SUT, add or propagate that input through the existing call path only when this is compile-only; otherwise stop and report the blocker.
- Keep production additions to required symbols, signatures, types, constructors, and fields used by the selected test.
- Do not add production fields, parameters, enum values, or types not used by the selected test.
- Put `TODO` inside newly added production method bodies unless the body is a trivial constructor, accessor, or data holder.
- Do not add production behavior, control flow, persistence, external integrations, endpoint contracts, validation rules, migrations, configuration, generated/static API docs, controllers, services, repositories, or clients.
- If tests require production behavior to compile or pass, stop and report the blocker instead of changing production behavior.
- For repository-backed generate or update mode, do not finish before completing Behavior State Verification.

Before finishing an HTTP API success case, determine whether a response schema exists.
When it exists, inspect the typed `*HttpApi` success method used by the case and verify that it validates that schema before decoding the body.
Treat missing schema validation as incomplete and fix it.
When invoked by a workflow, report the schema path and validating helper, or explicitly report that no response schema exists.

Before finishing, read `../../conventions/test-implementation-checklist.md`, fix any failed item, and check: default scope produced exactly one example unless an eligible parameterized set or an explicit multi-case selection applies, one class per selected `Feature`, one method per selected `Example` or eligible parameterized set, fixture helper boundaries follow `../../conventions/test-fixture-architecture.md`, naming follows `../../conventions/test-naming.md`, new structured resources or schemas reuse or extract shared definitions instead of duplicating equivalent definitions, repository-backed cases complete Behavior State Verification, standalone generate mode returns only Kotlin without claiming a behavior state, workflow-invoked generate mode writes the generated test to its explicit target path and keeps supporting edits within its granted write set, and update mode accepts exactly one `Feature` per run and preserves the existing container code while editing in place.
