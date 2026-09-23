# Kotlin context

Load Kotlin production and test entries independently.

- Kotlin production code: `../conventions/kotlin/kotlin-implementation.md` and `../conventions/kotlin/kotlin-implementation-checklist.md`;
- Kotlin persistence code only when the applicable work also touches persistence mappings, adapters, serializers, repositories, constructors, or factories: `../conventions/kotlin/persistence-models.md`;
- Kotlin tests: `../conventions/kotlin/test-implementation.md` and `../conventions/kotlin/checklist.md`.

Do not load Kotlin production process for a test-only Kotlin change.
