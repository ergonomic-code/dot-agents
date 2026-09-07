# Project baseline

## Brevity

Prioritize correctness, necessary context, and verifiability over brevity.
Be concise after those needs are met.
Prefer shorter wording and fewer sections when they do not remove needed evidence, caveats, or instructions.

## Explicit Planning

If the user asks to start with a plan, provide the intended plan in chat after required skill and context loading, then stop.
Wait for explicit permission to continue.
Do not edit files or run mutating commands in that turn.
A tool task list does not satisfy the request.

## Execution boundaries

- Perform the requested work directly without selecting, loading, or switching roles, profiles, modes, personas, or another request-classification layer.
- Modify only the caller-authorized scope and do not broaden it without an explicit request.
- Do not modify requirements, design artifacts, framework context, or project context unless the user includes them in the requested change.
- When modifying a human-facing artifact, preserve its human purpose and readability instead of turning it into agent-only instructions unless explicitly asked.
- Stop and report the boundary when correctness requires an unauthorized product decision or changes outside the authorized scope.
- Do not claim completion while required work or relevant verification remains unfinished.
- Report the completed result, changed scope, verification commands and results, and remaining blockers or caveats.

## Context

- Use resolved framework values from the host context.
- Before routed-context loading, pass exactly once the initial user request verbatim through stdin to `framework_checkout_root/src/task-workdir/load_task_context.py --repo-root "$(git rev-parse --show-toplevel)"` and treat its stdout as authoritative session task context.
- Invoke the loader only once per session, retain its result, and do not rerun it for later user requests.
- If the loader reports `Active task: none`, state this in chat and continue without task context; otherwise use the emitted task context directly.
- Read `framework_checkout_root/src/context/index.md`, classify the requested and planned work, and load every matching topical index in its stated order.
- Apply every loaded framework and project instruction that is relevant to the requested or planned work.
- Reevaluate context routing whenever the requested or planned write set changes.
- When an active task resolves, use the task-workdir context to resolve only the artifact bindings applicable to the requested operation.
- Pass resolved artifact content or concrete paths directly to the applicable skill or operation as explicit semantic inputs and caller-authorized output destinations.
- Treat project `AGENTS.md` as the project integration layer.
- If project `AGENTS.md` declares `## Local contexts`, use that section as the source of project-local context files.
- Load only task-relevant local context files.
- Prefer per-entry conditions in `## Local contexts` over separate project-specific loading-order rules.
- If `<framework-config-path>` is set and exists and was not loaded earlier, read it as YAML.
- Use `artifact_language` for comments and human-facing artifacts. Default to `ru` when the config or field is absent.
- Invoke skills only after these steps, with resolved semantic inputs and outputs, and follow their intrinsic loading instructions.
