# Context layering

Use dependency direction `baseline -> role -> skill -> conventions and artifacts`.
Treat `task-workdir` as an optional integration module beside generic skills.
The baseline alone resolves an implicit active task and loads task-workdir context.
The conditional module supplies concrete artifact bindings to the selected role.
Roles pass explicit semantic inputs and caller-selected outputs to generic skills.
Generic skills do not resolve tasks, discover task artifacts, choose task paths, or select or load roles.
Skills under `src/task-workdir/**` may know and manage the task layout and standard artifacts required by their purpose.
