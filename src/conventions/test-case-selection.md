---
keywords:
  - tests
---

# Test case selection

## Design-time kind and SUT

- Start from the intent to demonstrate that the selected desired behavior is absent from the current system.
- From that behavior and actual code or supplied design, identify the available boundary, component, and unit SUT candidates through which the same behavior can be exercised and observed.
- Prefer a unit SUT when the behavior can be exercised and observed directly without infrastructure or IO.
- Otherwise prefer the stable external boundary that exposes the behavior.
- Use a component SUT instead when moving inward from that boundary materially shortens the test or its execution time, or keeps the test on the standard test infrastructure.
- Select one evidence-backed kind and SUT before selecting examples.
- Stop when no candidate is evidence-backed or the priority does not select one unambiguously.
- After selecting the kind and SUT, use the corresponding interaction rules from `test-design.md`.

## Polymorphic operations

- Keep the operation itself as the SUT for behavior common to all input or output variants.
- Qualify the SUT with the exact variant from code or supplied design when the behavior belongs to only that variant.

## Existing coverage

- After selecting the SUT, inspect its existing and sibling tests for cases that exercise the selected obligation or its behaviorally distinguishing input or context classes.
- Select exactly one target disposition, its examples, and its form together in this order:
  - select `strengthen` when an existing case already exercises the selected precondition and action and its verification can be added or strengthened without changing the meaning of any invocation; record that case's existing `example`, `parameterized`, or `property` form and the examples needed to state the strengthened obligation;
  - otherwise select `extend-parameterized` when an existing parameterized case verifies the same rule over the same varying axis and can receive a behaviorally distinguishing concrete example not covered by an existing invocation; record `parameterized` and the added example;
  - otherwise select `new`, prefer a generated example class when the rule can be expressed over that class and the repository has an applicable property-testing facility for the selected SUT, otherwise select several concrete examples when they form a meaningful set of materially distinct cases, or one concrete example when they do not.
- For `new` without `property`, when one obligation maps a finite set of mutually exclusive input or context states to expected outcomes, include the complete set as concrete examples unless the user explicitly selects a subset.
- For `new`, map one concrete example to `example`, several concrete examples to `parameterized`, and a generated example class to `property`.

## Coding-time mapping

- Derive a new container and path mechanically from the selected kind and SUT through `test-naming.md`.
- Implement the selected example, parameterized, or property form.
- Strengthen or extend the selected existing case in place, preserving its other assertions and invocations.
