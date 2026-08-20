# Ergonomic component structure projection

Use this file with `./ergonomic-architecture.md` when a task concerns ports, operations, DOPs, resources, component dependencies, or effect graph shape.

## Terminology

- `ports` — entry points that receive external signals and delegate to one operation or one resource method.
- `operations` — top-level scenario components that orchestrate one use case over resources.
- `domain operations` (`DOPs`) — reusable lower-level effect sequences that are shared by multiple operations.
- `resources` — runtime components that encapsulate stateful code or abstract another runtime dependency behind an explicit API, whether that dependency is stateful or stateless.
- `complex resources` — domain-facing resources that expose one resource API over several lower-level resources or storage/integration mechanisms.
- `primitive resources` — resources that are internal implementation parts of a higher-level resource.
- `infrastructure resources` — project-owned infrastructure-facing resources reused as implementation parts of multiple domain-facing resources.

## Rules

- Reserve `port` for an entry point that receives an external signal; model outbound and internal dependencies as resources, not ports.
- Introduce a component interface only when current requirements, the selected design, or verified production code indicate at least two production implementations; test doubles do not count as production implementations.
- When a design artifact needs to show one not-yet-implemented component, use a concrete class declaration or explicitly labeled pseudocode instead of an interface.
- Expose one public use-case method name from each operation; allow multiple overloads of that method when needed.
- Keep the component dependency graph acyclic.
- Use a complex resource when one domain resource must coordinate several primitive or infrastructure resources behind a single bounded API.
- Keep primitive resources private to one higher-level resource unless the project intentionally creates multiple configured instances with non-overlapping state.
- Do not let infrastructure API types leak through a domain-facing resource API.
- Use explicit behavior layering: operations on top, optional domain operations below them, resources below operations, and optional infrastructure resources below resources.
- For each behavior layer except DOPs, forbid horizontal dependencies between peers on the same layer.
- Inject the resources an operation uses directly into that operation.
- Keep domain operations, when they exist, between orchestration-level operations and resources instead of mixing those responsibilities.
- Do not register DOPs in the DI container.
- Operations instantiate DOPs from dependencies already injected into the operation.
- Keep infrastructure concerns behind infrastructure resources instead of leaking them into domain-facing resources or operations.
- Do not hide core dependencies behind incidental facades when direct operation-to-resource wiring is the intended shape.

## Resource class naming

- Treat resource as an architectural category, not a concrete class role.
- Never end a resource class name with `Resource`.
- Name a resource class by its concrete role.
- Common role suffixes are `Repo` for an entity repository, `Dao` for storage operations over data that do not fit the entity model, `Client` for an external-system client, `Service` for a composite resource, and `Channel` for a channel of domain-specific messages.
- This suffix list is not exhaustive; use another role-specific name when it communicates the responsibility better.

## Typical component names

- Ports: `NewsController`, `RabbitMqReplicationListener`, `DailyReplicationScheduler`.
- Operations: `PublishNewsOp`, `ReplicateAggregateOp`, `CreateUserOp`.
- Resources: `ExercisesRepo`, `ExternalSystemClient`, `ConfirmEmailsChannel`, `FillScheduleNotificationsChannel`.
- Complex resources: `ConfirmEmailService`.
- Primitive resources: `ConfirmTokensDao`, `OutboxDao`, `ConfirmEmailsChannel`.
- Infrastructure resources: `FilesStorage`, `EmailSender`, `PushNotificationsService`.
