# Project baseline

## Brevity

Prioritize correctness, necessary context, and verifiability over brevity.
Be concise after those needs are met.
Prefer shorter wording and fewer sections when they do not remove needed evidence, caveats, or instructions.

## Explicit Planning

If the user asks to start with a plan, provide the intended plan in chat after required role, skill, and context loading, then stop.
Wait for explicit permission to continue.
Do not edit files or run mutating commands in that turn.
A tool task list does not satisfy the request.

## Context

- Use resolved framework values from the host context.
- Before selecting a role, decide whether the request has a task candidate.
- A task candidate exists only from an explicit task input, cwd inside a task workdir, or a high-confidence semantic match among the request, current branch, and one task directory.
- The existence of task directories alone is not a task candidate.
- If no candidate exists, do not load task-workdir context.
- If a candidate exists, read `framework_checkout_root/src/task-workdir/context.md` and use it to resolve the active task.
- Resolve the active role from the current request after task detection and resolution.
- Read `framework_checkout_root/src/roles/<role>.md` before the first substantive response.
- Read `framework_checkout_root/src/context/index.md`, classify the requested and planned work, and load every matching topical index in its stated order.
- Reevaluate context routing whenever the requested or planned write set changes.
- When an active task resolves, inject the task-workdir context's concrete input and output bindings into the selected role.
- The role invokes skills with explicit semantic inputs and concrete output destinations.
- Treat project `AGENTS.md` as the project integration layer.
- If project `AGENTS.md` declares `## Local contexts`, use that section as the source of project-local context files.
- Load only task-relevant local context files.
- Prefer per-entry conditions in `## Local contexts` over separate project-specific loading-order rules.
- If `<framework-config-path>` is set and exists and was not loaded earlier, read it as YAML.
- Use `artifact_language` for comments and human-facing artifacts. Default to `ru` when the config or field is absent.
- Invoke skills only after these steps, with resolved semantic inputs and outputs, and follow their intrinsic loading instructions.
