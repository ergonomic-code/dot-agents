# Persistence models

## Kotlin

- Keep primary constructors of persistence-backed classes free of default argument values.
- Put initial values for new objects in factory methods on the same class.
- Pass persisted values explicitly from repositories, row mappers, serializers, or persistence adapters.
