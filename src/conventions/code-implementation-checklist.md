# Code implementation checklist

## Reuse

- Does the final diff reuse or change existing code and definitions instead of copying them or adding unnecessary abstractions?
- Is every repeated responsibility implemented once, with its complete shared behavior centralized rather than only a common inner fragment?

## Kotlin

- Does every Kotlin expression body represent only fast, safe behavior that is functionally pure or limited to fast, safe ambient reads?
- Does expression-body classification include all work deferred through lambdas, sequences, streams, futures, or similar lazy values, with a block body used for other I/O, observable state changes, potentially blocking work, and resource lifecycles?
- Are fully qualified names absent from Kotlin use sites, with imports or import aliases used instead?
