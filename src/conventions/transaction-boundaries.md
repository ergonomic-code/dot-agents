# Transaction boundaries

## Scope

- Apply this convention when adding or changing a database transaction boundary or a database-backed mutation.

## Rules

- Keep a database transaction limited to database interactions and bounded in-process work required for their atomicity.
- Do not call external systems inside a database transaction except for explicitly allowed local-broker publication.
- Do not write to internal services inside a database transaction when one write is expected to take more than 5 ms.
- Do not perform computations inside a database transaction when they are expected to take more than 5 ms.
- Do not perform any other work that can retain the database connection long enough to threaten availability unless this convention or project context explicitly allows it.
- By default, the only allowed non-database I/O inside a database transaction is publishing messages to a local broker such as RabbitMQ, Kafka, or ActiveMQ.
