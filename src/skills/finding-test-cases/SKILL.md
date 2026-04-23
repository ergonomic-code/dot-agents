---
name: finding-test-cases
description: Find existing test cases for modules present in a ready structural diagram, usually `structure-chart/v1` YAML. Use when the input is a structural diagram and you need a grouped list of test cases by SUT module, with evidence from `*Test`, `*Api`, and `*HttpApi` classes under `src/test` and `src/testFixtures`, especially by scanning direct calls inside `// When` blocks.
---

# Finding Test Cases

Read `framework_checkout_root/src/conventions/feature-workdir.md`.

## Resolve Paths

- If the user gave an explicit output path, use it.
- Otherwise resolve the active feature directory via `feature-workdir.md`.
- If the user gave an input diagram path inside a feature directory, use that feature directory.
- If the active feature directory is resolved and no explicit output path is given, default output path to `<feature-dir>/020-current-test-cases.md`.

Input is an existing structural diagram.
Prefer `structure-chart/v1` YAML when available.
Do not rebuild the diagram unless the user explicitly asks for it.
Use `../../artifacts/structure-chart-v1` only as the format reference.

## Workflow

1. Read the diagram and collect the concrete modules present in it.
2. Treat each collected module as a candidate SUT.
3. For each candidate SUT, grep `src/test` and `src/testFixtures` for direct symbol usage, receiver usage, and obvious test-side wrappers around that SUT.
4. Anchor cases only in classes named `*Test`.
5. Inside only those matched tests, inspect methods and keep usages that sit under `// When`.
6. If the diagram contains a controller method, extract its HTTP method and path, grep test code by path first, then keep only HTTP calls and wrappers that target the same path with the same HTTP method.
7. Merge results by SUT and write or return only concrete test cases with file and line evidence.
8. If an output path is resolved, write the result to that Markdown file.
9. If the active feature directory is resolved, an output path is resolved, and `<feature-dir>/progress.md` exists, change the checklist sub-item `Составление списка текущих тест-кейсов` to checked form when it is present, including when it is nested under `Привязка требований к коду`, and append exactly one Markdown link to the written artifact using the path relative to `progress.md` and the artifact file name as the link text.

## Core Matching Rule

A test case is always a `*Test` method.
Primary evidence is a direct call from a test method body under a `// When` block to a module or method present in the diagram.
Prefer exact symbol matches over name similarity.
Use surrounding code only to resolve the receiver or imported alias of an otherwise direct call.
Do not invent a match from naming alone.
Also include a test case when the direct `// When` call is one thin local wrapper away from the SUT and the wrapper is resolved in the same test class or fixture.
Treat a wrapper as thin only when it forwards to one concrete SUT call without branching or alternative targets.
If the same test method touches several SUT modules from the diagram, include it under each matching SUT only when that SUT touch belongs to the `// When` block.

## Search Strategy

Prefer targeted code search from each SUT over a full sweep of all tests.
Use names from the diagram as the first filter, then inspect only matched files and methods.
Look for:
- method names from the diagram;
- receiver names or injected fields bound to the SUT;
- thin test-side wrappers that forward to the SUT.

Discard grep hits outside `src/test` and `src/testFixtures`.
Discard hits from non-`*Test` classes as case anchors.
In controller expansion, allow `*HttpApi` and `*Api` only as supporting evidence.

## Controller Expansion

Apply this extra pass only when the diagram includes a controller or handler method.
Search these test-side entry patterns:
- `*HttpApi`;
- `*Api`;
- `*Test`.
Still report only `*Test` methods as test cases.

Run the pass in this order:
1. Extract the endpoint HTTP method and path from the controller mapping.
2. Normalize the path shape, including templated segments and broken placeholders.
3. Grep test-side code for that path shape or its obvious literal expansions.
4. Inspect only matched `*HttpApi`, `*Api`, and `*Test` code.
5. Drop non-HTTP calls.
6. Drop HTTP calls that use a different HTTP method.
7. Drop HTTP calls that target a different path.

Treat these as valid evidence:
- direct invocation of the controller method;
- HTTP-call helpers that target the controller endpoint;
- API wrapper methods in test code that are clearly bound to that controller endpoint and are used by a test case.

If the test reaches the controller through `*HttpApi` or `*Api`, attribute the case to the controller SUT from the diagram.
If the path is partially templated, keep the match only when the static path shape still matches the controller route.
If the controller mapping contains a broken placeholder such as `POST /orders/{orderId/cancel`, treat it as `POST /orders/{orderId}/cancel` for matching.
During path comparison, treat placeholder segments as wildcards and compare static segments literally.

## Scope Rules

Stay within SUT modules present in the input diagram.
Search only `src/test` and `src/testFixtures` unless the user expands the scope.
Exclude production callers, generated code, and unrelated helpers.
Prefer the test method as the case anchor.
If no `// When` marker exists in a candidate test, infer the action phase from the test method semantics and use only SUT touches that belong to that action phase.
Do not treat setup, assertions, or cleanup as the action phase.
Use repository-relative paths and 1-based line numbers.

## Output

If an output path is resolved, write concise Markdown grouped by SUT to that file.
Otherwise return concise Markdown grouped by SUT.
For each SUT, list:
- test case name;
- evidence kind: `direct`, `controller`, or `indirect`;
- case location as `<path>:<line>`;
- optional forwarded-call or API-helper evidence as `<path>:<line>`;
- short note when the match depends on controller expansion or thin-wrapper resolution.

When no cases are found for a SUT, say so explicitly.
