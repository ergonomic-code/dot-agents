# Ergonomic component structure projection

Use this file with `./ergonomic-architecture.md` when a task concerns ports, operations, DOPs, resources, component dependencies, or effect graph shape.

## Terminology

- `ports` — entry points that receive external signals and delegate to one operation or one resource method.
- `operations` — top-level scenario components that orchestrate one use case over resources.
- `domain operations` (`DOPs`) — reusable lower-level effect sequences that are shared by multiple operations.
- `resources` — stateful or externally connected runtime components that expose explicit effects over aggregates, integrations, or other state.
- `complex resources` — domain-facing resources that expose one resource API over several lower-level resources or storage/integration mechanisms.
- `primitive resources` — resources that are internal implementation parts of a higher-level resource.
- `infrastructure resources` — project-owned infrastructure-facing resources reused as implementation parts of multiple domain-facing resources.

## Rules

- Use a complex resource when one domain resource must coordinate several primitive or infrastructure resources behind a single bounded API.
- Keep primitive resources private to one higher-level resource unless the project intentionally creates multiple configured instances with non-overlapping state.
- Do not let infrastructure API types leak through a domain-facing resource API.
- User explicit behavior layering: operations on top, optional domain operations below them, resources below operations, and optional infrastructure resources below resources.
- For each behavior layer except DOPs, forbid horizontal dependencies between peers on the same layer.
- Inject the resources an operation uses directly into that operation.
- Keep domain operations, when they exist, between orchestration-level operations and resources instead of mixing those responsibilities.
- Do not register DOPs in the DI container.
- Operations instantiate DOPs from dependencies already injected into the operation.
- Keep infrastructure concerns behind infrastructure resources instead of leaking them into domain-facing resources or operations.
- Do not hide core dependencies behind incidental facades when direct operation-to-resource wiring is the intended shape.

## Typical component names

- Ports: `NewsController`, `RabbitMqReplicationListener`, `DailyReplicationScheduler`.
- Operations: `PublishNewsOp`, `ReplicateAggregateOp`, `CreateUserOp`.
- Resources: `ExercisesRepo`, `ExternalSystemClient`, `ConfirmEmailsChannel`, `FillScheduleNotificationsChannel`.
- Complex resources: `ConfirmEmailService`.
- Primitive resources: `ConfirmTokensDao`, `OutboxDao`, `ConfirmEmailsChannel`.
- Infrastructure resources: `FilesStorage`, `EmailSender`, `PushNotificationsService`.
