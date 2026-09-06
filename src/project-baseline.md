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
- Before role selection or routed-context loading, pass exactly once the initial user request verbatim through stdin to `framework_checkout_root/src/task-workdir/load_task_context.py --repo-root "$(git rev-parse --show-toplevel)"` and treat its stdout as authoritative session task context.
- Invoke the loader only once per session, retain its result, and do not rerun it for later user requests.
- If the loader reports `Active task: none`, state this in chat and continue without task context; otherwise use the emitted task context directly.
- Resolve the active role from the current request after task-context loading.
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
