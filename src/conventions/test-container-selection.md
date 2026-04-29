# Test container selection

- Choose the narrowest existing test class whose scope matches the behavior under test.
- For an operation with polymorphic input or output variants, keep common operation requirements in the operation-level test class.
- Put requirements specific to one variant into that variant's test class when it exists.
- Create a variant-specific test class only when the requirement is variant-specific and the repository already uses that class pattern.
