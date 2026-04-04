# Agent Roles

## Choosing a role

1. If the user explicitly specified a role, act in that role.
2. If the role is not specified use:
   - the **assistant** role by default;
   - the **developer** role, if the request is about implementing or changing code, tests, build, or configuration;
   - the **project-context-engineer** if the request is about modification of `AGENTS.md` or files in `.agents` directory; 
   - when in doubt, ask which role to use.

## Loading the active role

After the active role is determined, open and follow the corresponding role file under `framework_checkout_root/src/roles`:
- `framework_checkout_root/src/roles/assistant.md`
- `framework_checkout_root/src/roles/developer.md`
- `framework_checkout_root/src/roles/project-context-engineer.md`

The selected role file defines the role-specific goal, boundaries, outputs, and rules.
