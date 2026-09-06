# Context layering

Use dependency direction `baseline -> task-context loader`, `task-context loader -> task resolver`, `task-context loader -> task-workdir context`, `baseline -> role`, `baseline -> context routing -> conventions, references, patterns, and artifact references`, `role -> skill`, and `skill -> intrinsic dependencies`.
The baseline invokes the task-context loader once for the initial request, uses its output directly, loads the role, and invokes the root context index.
The task resolver owns task selection only.
The task-context loader owns task-context assembly and emits either complete task context or no active task.
The root index classifies the requested and planned work and loads every matching topical index.
Roles define responsibility and behavioral boundaries; they do not route engineering context.
Generic skills load only dependencies intrinsic to their operation, artifact format, algorithm, or skill-specific guard.
Conventions define rules; applicability based on what work touches belongs to context routing.
Every convention declares at least one keyword in YAML front matter; prefer no more than three.
Treat the keywords as an intersection: every rule in the file must concern every declared keyword.
Add a keyword to the taxonomy only when it is needed to distinguish a new convention file or appears in at least two convention files.
Create a convention file only when its topic has at least two rules; otherwise put the rule in the most relevant existing convention.
Split rules with a different keyword intersection into a separate convention and route each convention independently.
Treat `task-workdir` as an optional integration module beside generic skills.
The baseline orchestrates task-context loading only.
The conditional module supplies concrete artifact bindings to the selected role.
Roles pass explicit semantic inputs and caller-selected outputs to generic skills.
Generic skills do not resolve tasks, discover task artifacts, choose task paths, or select or load roles.
Skills under `src/task-workdir/**` may know and manage the task layout and standard artifacts required by their purpose.
