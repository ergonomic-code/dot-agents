# Test container selection

- Infer the test kind from an explicit target class, explicit SUT, and sibling test style before choosing the container.
- Treat code symbols in requested class names and display names as explicit SUT anchors.
- Explicit SUT anchors override sibling style.
- If the user names an operation/resource/port test class or SUT, keep it as a component test and call that component directly.
- Use HTTP boundary helpers only when the selected container or SUT is an HTTP boundary/API surface.
- Choose the narrowest existing test class whose scope matches the behavior under test.
- If the target class has more than one public method and the requirement targets one method, choose or create `<TargetClassName>_<camelCasedMethodName>`.
- Before adding a new test case, inspect candidate and sibling cases for the same observable requirement.
- Reuse or extend an existing case when its boundary, setup, action, and assertion point fit the selected requirement.
- Create a new case only when no existing case can verify the requirement without changing its meaning or mixing unrelated obligations.
- If `Check` or `Variant` anchors are narrower than the candidate class name or display name, choose or create the narrower class when sibling tests show that pattern.
- For an operation with polymorphic input or output variants, keep common operation requirements in the operation-level test class.
- Put requirements specific to one variant into that variant's test class when it exists.
- Create a variant-specific test class only when the requirement is variant-specific and the repository already uses that class pattern.
