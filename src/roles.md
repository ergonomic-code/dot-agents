# Agent Roles

## Choosing a role

1. If the user explicitly specified a role, act in that role.
2. If the role is not specified use:
   - the **assistant** role by default;
   - the **developer** role only to plan or implement changes in target-repository files (code/tests/build/repo config);
   - the **framework-context-engineer** if the request is about modification of framework-provided context under `framework_checkout_root/src/**`;
   - the **project-context-engineer** if the request is about modification of project `AGENTS.md` or project-local files in `.agents` or `.codex` outside `framework_checkout_root/**` and outside the active feature workdir;
   - the **feature-context-engineer** if the request is about refining feature analysis or design artifacts under the active feature workdir so they guide both people and AI agents;
   - when in doubt, ask which role to use.

## Loading the active role

After the active role is determined, open and follow the corresponding role file under `framework_checkout_root/src/roles`:
- `framework_checkout_root/src/roles/assistant.md`
- `framework_checkout_root/src/roles/developer.md`
- `framework_checkout_root/src/roles/framework-context-engineer.md`
- `framework_checkout_root/src/roles/project-context-engineer.md`
- `framework_checkout_root/src/roles/feature-context-engineer.md`

The selected role file defines the role-specific goal, boundaries, outputs, and rules.
