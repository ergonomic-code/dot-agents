# Context layering

Use dependency direction `baseline -> role`, `baseline -> context routing -> conventions and references`, `role -> skill`, and `skill -> intrinsic dependencies`.
The baseline resolves task and role context, loads the role, and invokes the root context index.
The root index classifies the requested and planned work and loads every matching topical index.
Roles define responsibility and behavioral boundaries; they do not route engineering context.
Generic skills load only dependencies intrinsic to their operation, artifact format, algorithm, or skill-specific guard.
Conventions define rules; applicability based on what work touches belongs to context routing.
Treat `task-workdir` as an optional integration module beside generic skills.
The baseline alone resolves an implicit active task and loads task-workdir context.
The conditional module supplies concrete artifact bindings to the selected role.
Roles pass explicit semantic inputs and caller-selected outputs to generic skills.
Generic skills do not resolve tasks, discover task artifacts, choose task paths, or select or load roles.
Skills under `src/task-workdir/**` may know and manage the task layout and standard artifacts required by their purpose.
