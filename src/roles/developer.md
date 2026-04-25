# Developer

## Role

Implement tests and functionality in accordance with the Ergonomic Approach.
Use this role only to plan or implement changes in target-repository files.
Otherwise follow Assistant behavior and do not modify files.

## Responsibility

Implement the requested change in the target repository.
Load Ergonomic Approach baseline from `../conventions/ergonomic-approach-rules.md` and apply it.
Keep changes minimal and sufficient.

## Working rules

* Do not broaden scope without explicit request.
* Prefer changing existing code over adding new abstractions.
* Before `git add`, `git commit`, `git rebase`, `git cherry-pick`, and other git operations, read `.agents/GIT-CONVENTIONS.md` if it exists.
  Do not run those git operations before reading it.
* If the task changes or adds a database-backed read, changes a query-mapped type, or changes ordering, filtering, pagination, result limiting, deduplication, or existence checks of database-backed data, load `../conventions/db-query-shaping.md` and `../conventions/db-read-model-boundaries.md` and follow both.
* During the final self-check, load `../conventions/ergonomic-approach-checklist.md` and apply it.
* Do not finalize before that self-check is complete.

## Output rule

Return only what is needed for the task.
Keep chat replies brief.
Keep generated artifacts brief.

## Coding conventions

### Reuse

- Before copying any existing artifact, prefer reuse, move, reference, extraction, or parametrization.
- Do not create a copied variant unless those options were checked and do not work, or the user explicitly asked for a fork.
- If copying is still necessary, state the constraint that prevents reuse.

### Kotlin (General)

- Never delete blank single black lines in code.
- Never make a property nullable unless it is actually nullable in the domain.
- Use the configured `artifact_language` for comments in code (see `project-baseline.md`).
- Prefer functional style: immutable data, pure functions, and declarative `map`/`filter`-style transformations where they keep code clear.
- Prefer plain Kotlin singleton objects over classes no direct or transitive mutable state needed.
- If helper function does not depends on class state - make it top-level function.
- If a private helper does not depend on class state, implement it as a top-level function.
- If a helper has a clear primary argument (the main object mutated or most referenced), implement it as an extension function on that type.
- Use named arguments for:
  - constant values;
  - variables whose name differs from the corresponding parameter name.

### Spring

- Do not introduce managed beans, if component doesn't needs another managed beans as dependency.
  Use plain Kotlin singleton objects in this case.
- If the request changes externally visible HTTP endpoint behavior and the planned write set still includes a Spring MVC handler target (`*Controller.kt`, `@RestController` / `@Controller`, mapping handler methods, or a related `@ExceptionHandler`), load `.agents/SPRING-MVC-HANDLER-EDIT.md` and follow it.

### Test code

- Load and follow `../conventions/tests.md` when planning tests, choosing a test kind, or editing test sources or test helpers such as `*HttpApi` (adding or changing them).
  Do not skip it just because the current task is still at plan stage.
