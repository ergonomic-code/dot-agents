# Bottom-up Workflow

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
   - If multiple entry points are found and the user did not narrow the scope, build one chart bundle per entry point under the chart root directory resolved via `./references/output-layout.md`.
6. Treat the upward walk as a way to discover candidate application entry points, not as the final chart shape.
   - The upward result is a chain of callers.
   - The final structure chart must still be a tree rooted at the selected entry point.
7. For each selected HTTP endpoint entry point, always run a separate agent to extend the chart from that endpoint downward.
   - Launch that agent with the `spawn_agent` tool.
   - Give the agent the exact endpoint, reverse-pass evidence, bundle directory, and the requirement to follow the `Top-down` workflow.
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
12. Assemble each `structure-chart/v1` YAML at the resolved YAML path for that entry point.
13. Validate each generated YAML path.
14. Generate the matching Mermaid file next to each YAML path.
15. If `index.md` update is required by `./references/output-layout.md`, add or refresh one feature-index row per created bundle directory.

## Reverse-Pass Subagent Prompt Template

Use this template when launching the reverse-pass agent for a selected HTTP endpoint.

```text
Build a structure chart for this HTTP endpoint with the `building-structure-chart` skill.

Endpoint:
- <HTTP method> <path>
- Root handler: <repo-relative file path>:<line> <symbol>

Output bundle directory:
- <bundle dir>

Constraints:
- Follow the `Top-down` workflow from `./references/top-down-workflow.md`.
- Keep the selected endpoint as the single root.
- Use the reverse-pass caller chain only as evidence for endpoint selection and for required downward branches.
- Build the full relevant downward tree under the endpoint, not only the caller chain that was already discovered.
- Keep meaningful sibling calls after a module is included, even when they do not lead to the target tables.
- Treat <bundle dir> as the final chart bundle directory for this run.
- Exclude platform code, framework internals, external libraries, tests, migrations, one-off scripts, and dead code unless explicitly requested.
- Validate the YAML before rendering Mermaid.
- Write `<slug>-structure-chart.yaml` and `<stage-code>-structure-chart.mmd` into <bundle dir>.

Evidence from the reverse pass:
- <caller or touch-point evidence>
- <caller or touch-point evidence>
```

Fill every placeholder before launch.
Do not launch the agent with unresolved placeholders.
Do not rewrite the template into a shorter implicit prompt before launch.
