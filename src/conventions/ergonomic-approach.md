# Ergonomic Approach rules

## Test design

- 100% of functions, business rules, and system integrations must be covered by tests.
- 90% of tests must run in under 50 ms on a modern high-end machine.
- Shared test infrastructure must start in under 10 seconds for the whole suite.
- Test cases must be decoupled from implementation details, including APIs of internal implementation classes.

## Data design

- Data must be effectively immutable.
- Data must make illegal states unrepresentable.
- Data should consist of a small number of fields.
- Prefer no more than 10 fields.

## Subprogram design

- A subprogram must be either an operation with cognitive complexity at most 4, or an effectively pure computation with cognitive complexity at most 15.
- An operation must be either a command or a query.
- A command may change observable state and must return only result data.
- A query must not change observable state and must return data derived from its parameters and accessible state.
- A system operation must serve one use case of one actor or client application.
- A subprogram implementation must stay on one abstraction level.
- A subprogram must have at least communicational or sequential cohesion.
- A non-trivial operation that includes at least two branch types among input, transformation, and output should have a balanced form.
- Prefer read, then transform, then write.

## Stateful application component design

- A stateful component may be only a resource, an operation, or a port.
- A resource must fully encapsulate 1 to 3 state elements and provide the only read and write methods for them.
- An operation must have one public method and coordinate a 2+ step workflow over 1+ resources.
- A port must translate one protocol into calls to one or more operations or resources.
- One port method must call one operation or resource method.
- Dependencies between components must not contain cycles.
- A component must have no more than 10 dependencies on other stateful components.
- The dependency graph of any component must be a tree until the transition to infrastructure components.

## General rules

- Apply DRY and SSOT.
- Apply YAGNI.
- Prefer practical code over idealized code.

