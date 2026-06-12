# Abstraction level boundaries

A code unit must keep one local abstraction level.
Use this when reviewing, refactoring, or extracting a callable unit or class.

## Rule

A code unit is valid when its name, role, state, collaborators, methods, and inline steps belong to either:
- one dominant vocabulary;
- or one explicit source-to-target translation vocabulary pair.

A code unit violates the rule when understanding it requires switching between semantic vocabularies or scales, such as business meaning, protocol framing, persistence mechanics, serialization, or UI details.

## Callable units

A callable body must read as steps one level below the callable name.
Foreign vocabulary belongs behind named helpers or collaborators.

A translation callable must make its direction explicit in the name or surrounding API, such as `toDomain`, `fromHttp`, `mapToDto`, `encode`, or `decode`.
It must not contain independent business policy, workflow orchestration, retries, or persistence decisions.

## Classes

A class must keep one dominant responsibility vocabulary across its name, constructor, fields, public methods, and primary collaborators.
A class violates the rule when it owns mechanics from another vocabulary, even if each method is internally coherent.
Move foreign mechanics to a helper, value type, mapper, adapter, or collaborator named in that vocabulary.

An adapter or translator class may own a source-to-target vocabulary pair.
It must not also own unrelated workflow, business policy, or storage responsibility.

## Refactoring test

Identify the vocabulary from the unit name, package or module, parameters, fields, return types, public methods, main locals, and primary callees.
If owned behavior belongs to another vocabulary, extract or move it behind an API named in that vocabulary.
Keep the enclosing unit in its dominant vocabulary.

