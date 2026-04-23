# Top-down Workflow

1. Resolve the input to a specific root entry point.
   - For an endpoint, find the controller or handler method and treat it as the root module.
   - For a method or function, use it as the root module.
2. Resolve the chart root directory, bundle directory, YAML path, and Mermaid path via `./references/output-layout.md`.
3. Read only the code needed to understand the control flow under that root.
4. For each call into project code, repeat the same procedure recursively until the relevant project control flow is covered.
5. Do not descend into platform code, framework internals, or library code.
6. Exclude tests, migrations, one-off scripts, and dead code unless the user explicitly asks for them.
7. Assemble `structure-chart/v1` YAML at the resolved YAML path.
8. Validate the generated YAML path.
9. Generate the matching Mermaid file at the resolved `.mmd` path.
10. If `index.md` update is required by `./references/output-layout.md`, add or refresh the bundle-directory row in the feature index.
