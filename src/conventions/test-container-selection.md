---
keywords:
  - tests
  - container-selection
---

# Test container selection

- Infer the test kind from an explicit target class, explicit `Feature`, explicit target surface, and sibling test style before choosing the container.
- Choose the technical container name only after determining the test kind.
- Explicit target anchors override sibling style.
- If the user names an operation/resource/port test class or target surface, keep it as a component test and call that component directly.
- Use HTTP boundary helpers only when the selected container or `Feature` is an HTTP boundary/API surface.
- Name an HTTP boundary/API container `<OperationName>ApiTest`.
- Choose the narrowest existing test class whose scope matches the behavior under test.
- For a component test, choose or create `<TargetClassName>Test` when the requirement verifies a class-wide invariant or the target class has one public method.
- If a component-test requirement targets one method of a target class with two or more public methods, choose or create `<TargetClassName>_<camelCasedMethodName>`.
- Before adding a new test case, inspect candidate and sibling cases for the same observable requirement.
- Reuse or extend an existing case when its boundary, setup, action, and assertion point fit the selected requirement.
- Create a new case only when no existing case can verify the requirement without changing its meaning or mixing unrelated obligations.
- If `Rule` or `Example` anchors are narrower than the candidate class name or display name, choose or create the narrower class when sibling tests show that pattern.
- For an operation with polymorphic input or output variants, keep common operation requirements in the operation-level test class.
- Put requirements specific to one variant into that variant's test class when it exists.
- Create a variant-specific test class only when the requirement is variant-specific and the repository already uses that class pattern.
