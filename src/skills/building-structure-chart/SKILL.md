---
name: building-structure-chart
description: Build valid `structure-chart/v1` YAML and Mermaid `.mmd` from a root method, function, HTTP endpoint, or database table/table set. Use when you need to extract the call structure, nested modules, lambdas, conditional calls, and loops from code and return the diagram in the required spec-pack format, including reverse lookup from tables to application entry points and then charting the selected execution path.
---

# Building Structure Chart

Read `framework_checkout_root/src/conventions/feature-workdir.md`.
Read `framework_checkout_root/src/conventions/feature-stage-skill.md`.
Read `./references/output-layout.md`.
Read `./references/top-down-workflow.md`.
Read `./references/bottom-up-workflow.md`.
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
- For `Top-down`, follow `./references/top-down-workflow.md`.
- For `Bottom-up`, follow `./references/bottom-up-workflow.md`.

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
- Do not descend into platform code, framework internals, or external libraries.
- Add a platform, framework, or external-library call only as a leaf and only when that call represents a globally observable effect.
- Globally observable effects include network or storage IO, message publication, process launch, thread/job/task start, and OS-level side effects.
- Treat logging, metrics, tracing, builder setup, and result extraction as noise unless the user explicitly asks for them.
- For a fluent external call chain that performs one effect, choose only one method as the call target.
- Choose the method that best names the effect, not configuration or extraction methods in the chain.
- Do not encode fluent configuration details as `call.in` or `call.out`.
- Read each relevant statement as a full expression tree, not only by its top-level call.
- Include meaningful project calls nested in arguments, chained expressions, assigned expressions, and return expressions.
- Do not reduce an included module to only the subpath that reaches the target table; keep its other meaningful sibling calls as well.
- Do not drop a meaningful project call just because its receiver is a local variable, a lambda parameter, or an intermediate expression rather than an injected dependency.
- Do not create nodes for `if`, `when`, `switch`, `forEach`, `map`, `mapNotNull`, `filter`, loops, collections, DTOs, temporary values, or framework glue.
- Do not use Kotlin `inline` alone to decide whether a callable becomes a node.
- Model a named project function or method as a module when it owns meaningful work or meaningful project calls, even if it is an `inline` HOF.
- Collapse only HOF calls that act as control-flow, iteration, scoping, collection transformation, or builder syntax and do not own meaningful project work.
- For a collapsed HOF, do not create a callable node for the HOF.
- If a collapsed HOF uses a lambda only as the body of that syntax, do not emit a `lambda` node for it.
- Inline that lambda body into direct calls from the owning module.
- Mark calls from collapsed iteration HOFs with `call.loop`.
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

- Check that meaningful named project functions remain modules even when declared `inline` or accepting lambdas.
- Check that collapsed Kotlin HOFs are represented via direct calls and `loop` when they encode iteration, not as separate nodes.
- Check that lambdas used only as bodies of collapsed HOFs are inlined into the owner's calls and are not emitted as separate `lambdas`.
- Check that meaningful project calls nested in arguments, chained expressions, and assignment or return expressions are not skipped.
- Check that meaningful calls on local-variable receivers and inside inline-HOF bodies were kept when they resolve to project code.
- Check that external-library call nodes are leaves and represent globally observable effects.
- Check that each fluent external effect chain contributes at most one call target.
- Check that fluent configuration details are not encoded as `call.in` or `call.out`.
- For every included module, enumerate its meaningful direct project calls from the covered statements and verify that sibling calls were not pruned just because they do not touch the target table.
- If the input was DB tables, check that the rendered chart still reads from the application entry point down to the relevant table access path.
