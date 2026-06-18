# Ergonomic data structure projection

Use this file with `./ergonomic-architecture.md` when a task concerns domain data shape, entities, value objects, aggregates, references, or persistence boundaries.

## Terminology

- `entities` — domain objects with identity.
- `value objects` — immutable domain objects without identity that are compared by value.
- `aggregates` — persistence and loading units of the domain model that are loaded and saved as a whole.
- `aspect entities` — technical or design-driven entity slices that reuse the identity of another entity instead of defining a new one.
- `anchor entities` — the ordinary entities whose identity is reused by aspect entities.

## Rules

- Model the domain with entities, value objects, and aggregates.
- Entities and value objects should be effectively immutable.
- Prefer a small number of meaningful fields.
- Group cohesive fields into value objects.
- Aggregates are the persistence unit and should be loaded and saved as a whole.
- References inside an aggregate may be direct.
- References between aggregates should go by identifier.
- Do not create cycles between aggregates.
- Do not model many-to-many links directly in the data model.
- Split oversized entities into separate aggregates or aspect entities when that improves boundaries without losing meaning.
