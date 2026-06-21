# Bug fix flow decision

## Status

Accepted.

## Context

The framework is being reworked from one feature-development flow into a set of work types.
One open question was whether bug fixes need a separate top-level workflow.
Bug fixes still require the same feature-flow phases: clarify the target behavior, understand the current implementation, choose a solution direction, run preliminary refactoring when needed, and implement through TDD.
The bug-fix-specific difference is the initial state of the work.
A defect already points to violated behavior, and the first red case is often already known or becomes known during reproduction.
Reproduction and localization fit the phase for understanding the current implementation and finding the target components.
Writing the reproducer also belongs to that current-state phase.
Sometimes the current-state phase needs limited preliminary refactoring before the reproducer can be written ergonomically.

## Decision

Bug fix is not a separate top-level workflow type.
Treat bug fix as a specialized case of the feature flow.
The defect is the input that defines the gap between current and target behavior.
The current-state phase must include writing the reproducer, reproducing the defect, and localizing it.
The current-state phase may include preliminary refactoring when the existing structure blocks an ergonomic reproducer.
The implementation phase usually starts with an already selected red case.
From that point, the ordinary TDD lifecycle applies.

## Consequences

Feature-flow mechanics remain reusable for bug fixes: feature brief, target behavior, code anchors, solution direction, preliminary refactoring, and TDD implementation.
Bug-fix guidance should specialize phase expectations instead of duplicating the whole flow.
Bug-fix guidance must not defer writing the reproducer to the implementation phase when it is needed to understand the current defect.
Preliminary refactoring is not only a later feature-flow phase for bug fixes; it can also be a current-state enabler for the reproducer.
Runtime skills such as `fix-red-case` remain implementation-phase tools for a selected failing case, not evidence that bug fix is a separate workflow.
