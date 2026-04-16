---
name: building-structure-chart
description: Build valid `structure-chart/v1` YAML and Mermaid `.mmd` from a root method, function, HTTP endpoint, or database table/table set. Use when you need to extract the call structure, nested modules, lambdas, conditional calls, and loops from code and return the diagram in the required spec-pack format, including reverse lookup from tables to application entry points and then charting the selected execution path.
---

# Building Structure Chart

Write files to the working directory.
If no path is specified, use `./tmp`.
Create `./tmp` if it does not exist.
For a single chart, use `./tmp/structure-chart.yaml` for YAML.
For a single chart, use `./tmp/structure-chart.mmd` for Mermaid.
For per-entry-point output, use `<output-directory>/<endpoint-slug>-structure-chart.yaml` and `<output-directory>/<endpoint-slug>-structure-chart.mmd`.
Use the shared artifact at `src/artifacts/structure-chart-v1`.
Read only the files you need from:
- `../../artifacts/structure-chart-v1/references/structure-chart-v1.schema.json`
- `../../artifacts/structure-chart-v1/scripts/validate_structure_chart.py`
- `../../artifacts/structure-chart-v1/scripts/render_mermaid.py`
- `../../artifacts/structure-chart-v1/references/validation-rules.md`
- `../../artifacts/structure-chart-v1/references/rendering-rules.md`
- `../../artifacts/structure-chart-v1/references/example-structure-chart.yaml`
- `../../artifacts/structure-chart-v1/references/example-structure-chart.mmd`

## Hard Gate

Create both the YAML and the `.mmd` by default.
If the user explicitly asks for only one artifact, you may skip writing the other after successful validation.
Always validate the YAML with `python <artifact-dir>/scripts/validate_structure_chart.py <yaml-path>`.
If validation fails, fix the YAML and repeat until it passes.
Do not render Mermaid before successful validation.
Render Mermaid with `python <artifact-dir>/scripts/render_mermaid.py <yaml-path> > <mmd-path>`.
If `Bottom-up` resolves one or more HTTP endpoints, the parent agent must call `spawn_agent` once per selected endpoint before any downward expansion starts.
If `spawn_agent` is available, treating the downward pass as local work is a failure to follow this skill.
If `spawn_agent` is unavailable or blocked, stop and report that the reverse pass is blocked instead of silently continuing locally.

## Input Modes

- `Top-down`: input is an endpoint, method, or function.
- `Bottom-up`: input is one or more DB tables.

## Workflow: Top-down

1. Resolve the input to a specific root entry point.
   - For an endpoint, find the controller or handler method and treat it as the root module.
   - For a method or function, use it as the root module.
2. Read only the code needed to understand the control flow under that root.
3. For each call into project code, repeat the same procedure recursively until the relevant project control flow is covered.
4. Do not descend into platform code, framework internals, or library code.
5. Exclude tests, migrations, one-off scripts, and dead code unless the user explicitly asks for them.
6. Assemble `structure-chart/v1` YAML in `./tmp/structure-chart.yaml` by default, or in the chart output directory when one is provided.
7. Validate the generated YAML path.
8. Generate the matching Mermaid file next to that YAML path.

## Workflow: Bottom-up

1. Normalize the input tables.
   - Keep schema-qualified and unqualified names.
   - Use aliases, entity names, jOOQ names, repository names, and hardcoded SQL spellings only as search aids.
2. Find persistence touch points that read or write those tables.
3. Walk upward through project callers until you reach application entry points such as controllers, handlers, jobs, schedulers, batch launchers, or message consumers.
4. Distinguish direct evidence from inference.
   - If the table link is only implied by naming or mapping conventions, say so in `notes`.
5. Choose chart scope.
   - If one entry point is found, use it as the root module.
   - If multiple entry points are found and the user selected one, use that one as the root module.
   - If multiple entry points are found and the user did not narrow the scope, build one chart per entry point under separate output directories.
   - Name files as `<output-directory>/<endpoint-slug>-structure-chart.yaml` and `<output-directory>/<endpoint-slug>-structure-chart.mmd`.
6. Treat the upward walk as a way to discover candidate application entry points, not as the final chart shape.
   - The upward result is a chain of callers.
   - The final structure chart must still be a tree rooted at the selected entry point.
7. For each selected HTTP endpoint entry point, always run a separate agent to extend the chart from that endpoint downward.
   - Launch that agent with the `spawn_agent` tool.
   - Give the agent the exact endpoint, reverse-pass evidence, output directory, and the requirement to follow the `Top-down` workflow.
   - Do not perform any part of that endpoint's downward expansion in the parent agent.
   - Do not replace the required `spawn_agent` call with a local loop over endpoints.
   - Wait for each reverse-pass agent result before final assembly of that endpoint chart.
   - In that agent, apply the `Top-down` workflow starting from the endpoint.
   - Use the upward chain only to choose the endpoint and to identify which downward branches must be present because they lead to the target tables.
   - Build the full relevant downward tree under that endpoint, not just the previously discovered chain.
   - After a module is included in the chart, keep all of its meaningful project calls from the covered code, even when some sibling calls do not participate in the target-table path.
   - Keep one agent per endpoint so the downward expansions stay isolated.
8. For non-HTTP entry points, perform the same top-down tree expansion locally from that entry point downward.
9. When assembling the chart, keep the selected entry point as the single root and include the relevant branching structure under it.
   - Do not emit a linear caller chain as the final diagram when the code below the root forms a wider tree.
   - Put unresolved gaps or inferred links into `notes`.
10. Do not descend into platform code, framework internals, or library code.
11. Exclude tests, migrations, one-off scripts, and dead code unless the user explicitly asks for them.
12. Assemble `structure-chart/v1` YAML in the working directory as `structure-chart.yaml`, or in `<output-directory>/<endpoint-slug>-structure-chart.yaml` when multiple charts are needed.
13. Validate each generated YAML path.
14. Generate the matching Mermaid file next to each YAML as `structure-chart.mmd` in the working directory, or as `<output-directory>/<endpoint-slug>-structure-chart.mmd` for per-entry-point output.

## Reverse-Pass Subagent Prompt Template

Use this template when launching the reverse-pass agent for a selected HTTP endpoint.

```text
Build a structure chart for this HTTP endpoint with the `building-structure-chart` skill.

Endpoint:
- <HTTP method> <path>
- Root handler: <repo-relative file path>:<line> <symbol>

Output directory:
- <output dir>

Constraints:
- Follow the `Top-down` workflow from the selected endpoint downward.
- Keep the selected endpoint as the single root.
- Use the reverse-pass caller chain only as evidence for endpoint selection and for required downward branches.
- Build the full relevant downward tree under the endpoint, not only the caller chain that was already discovered.
- Keep meaningful sibling calls after a module is included, even when they do not lead to the target tables.
- Treat <output dir> as the chart output directory for this run instead of the default `./tmp`.
- Exclude platform code, framework internals, external libraries, tests, migrations, one-off scripts, and dead code unless explicitly requested.
- Validate the YAML before rendering Mermaid.
- Write `<endpoint-slug>-structure-chart.yaml` and `<endpoint-slug>-structure-chart.mmd` into <output dir>.

Evidence from the reverse pass:
- <caller or touch-point evidence>
- <caller or touch-point evidence>
```

Fill every placeholder before launch.
Do not launch the agent with unresolved placeholders.
Do not rewrite the template into a shorter implicit prompt before launch.
## Shared Modeling Rules

- Model named executable units as `modules`.
- Use stable `id` values derived from code identifiers.
- Always add `code.path` and `code.line` for every module and lambda.
- Use repository-relative paths in `code.path` and a 1-based line number in `code.line`.
- Fill module names from code verbatim.
- For methods and extension functions, write `title` as `<ClassName>.<br/>methodName`.
- Use `title` for the rendered module name; write `title` and `notes` in the `artifact_language`.
- Keep exactly one root module for the root method or handler.
- If the input was an HTTP endpoint, reflect the HTTP method and path in `title` or `notes`, not in an artificial `id`, if the code already provides a stable name.
- If the input was DB tables, keep the root module as the selected application entry point, not as the repository or SQL touch point.
- Use `parent` only when one named function is syntactically nested inside another named function.
- Model local or anonymous callables as `lambdas` with `owner` set to the module where they are declared.
- Do not add modules or calls from the platform, frameworks, or external libraries to the diagram.
- Read each relevant statement as a full expression tree, not only by its top-level call.
- Include meaningful project calls nested in arguments, chained expressions, assigned expressions, and return expressions.
- Do not reduce an included module to only the subpath that reaches the target table; keep its other meaningful sibling calls as well.
- Do not drop a meaningful project call just because its receiver is a local variable, a lambda parameter, or an intermediate expression rather than an injected dependency.
- Do not create nodes for `if`, `when`, `switch`, `forEach`, `map`, `mapNotNull`, `filter`, loops, collections, DTOs, temporary values, or framework glue.
- Treat Kotlin HOFs declared with the `inline` modifier as syntax for control flow, not as callable nodes.
- This applies even when the inline HOF is not one of the common collection names.
- Collection HOFs such as `forEach`, `map`, `mapNotNull`, and `filter` are common examples of that rule.
- If such an inline HOF uses an inline lambda only as the body of that control flow, do not emit a `lambda` node for it.
- Inline the lambda body into direct calls from the owning module and mark those calls with `call.loop`.
- Example: `savedEvents.map { EventToEditEventViewConverter.convert(it, languageTag) }` should produce a looped call from the owner to `EventToEditEventViewConverter.convert`, not `owner -> lambda -> convert`.
- Example: `savedEvents.mapNotNull { DiaryEventCreated.fromDto(userId, it, serial) }` should produce a looped call from the owner to `DiaryEventCreated.fromDto`, not `owner -> mapNotNull -> lambda -> fromDto`.
- Represent a condition in `call.if`.
- Represent iteration in `call.loop`.
- Put a passed module or lambda in `call.in`.
- Put a returned module or lambda in `call.out`.
- Create exactly one `calls[*]` entry per `(from, to)` pair and merge `if`, `loop`, `in`, and `out` into it.
- Omit noisy calls: logging, getters/setters, trivial mappers, constructors, framework wrappers. Keep orchestration, validation, branching, side effects, and meaningful computational steps.
- Keep meaningful nested calls even when they appear inside another kept call's arguments or pipeline.
- Repository reads/writes, domain-event factories, and event publication are meaningful by default and should not be dropped as noise.
- If a callable is passed as a parameter and then invoked later, first show it in `in`, then add a separate normal `call` to that callable.
- Do not draw reverse arrows for `out` when no reverse call exists in the code.

## Shared Validation

- Check that Kotlin inline HOFs are represented via direct calls and `loop` when they encode iteration, not as separate nodes.
- Check that inline lambdas used only as bodies of inline HOFs are inlined into the owner's calls and are not emitted as separate `lambdas`.
- Check that meaningful project calls nested in arguments, chained expressions, and assignment or return expressions are not skipped.
- Check that meaningful calls on local-variable receivers and inside inline-HOF bodies were kept when they resolve to project code.
- For every included module, enumerate its meaningful direct project calls from the covered statements and verify that sibling calls were not pruned just because they do not touch the target table.
- If the input was DB tables, check that the rendered chart still reads from the application entry point down to the relevant table access path.
