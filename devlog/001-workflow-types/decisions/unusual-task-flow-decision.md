# Unusual task flow decision

## Status

Accepted.

## Context

The framework is being reworked from one feature-development flow into a set of work types.
One open question was how to handle work that does not clearly fit an existing specialized flow.
Such work does not necessarily produce a user-facing feature, a production-code change, or a TDD implementation queue.
It still requires disciplined planning because the agent must know the target result, the current system and evidence sources, and the chosen way to close the gap.
The existing feature-flow mechanics already contain those common phases, but their feature-specific artifacts and implementation expectations are too narrow for task-only work.

## Decision

Use a universal `Task` flow for unusual work that does not clearly fit a specialized flow.
The universal flow has three required phases: define the target state, understand the current state, and choose the solution direction.
Specialized flows such as feature implementation, refactoring, and bug-fix-as-feature may extend this base flow when the task has a known work type.
Unusual work should stay in the universal flow until its required output, evidence sources, and change boundary prove that a specialized flow is needed.
The task should first define the decision or deliverable it must produce, inspect the current system and available evidence, and then choose the method, boundaries, artifacts, and validation format.
Only add an implementation or TDD phase if the chosen direction includes production-code changes or testable behavior changes.

## Consequences

The framework needs a top-level distinction between universal tasks and specialized work types.
Feature-specific files should not be the only model for tracked work.
Task workdirs may reuse the same flat `progress.md` phase structure, but their checklist items must describe task evidence and outputs instead of forced feature artifacts.
Runtime guidance should route ambiguous requests to the universal task flow first, then specialize only after the work type is clear.
