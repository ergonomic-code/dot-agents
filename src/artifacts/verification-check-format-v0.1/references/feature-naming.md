# Feature naming

Name `Feature` as `<human-readable verified object> (<SUT reference>)`.
Use an evidence-backed SUT reference and do not invent one.
If a SUT reference cannot be resolved, stop and report the missing anchor.
Render an HTTP boundary SUT reference as `<HTTP method> <path>`.
For another boundary, use its stable external operation identifier, such as a command, topic, queue name, route, CLI command, or external operation.
Render a component SUT reference as `<ClassName>` for class-wide behavior or a class with one public operation, and as `<ClassName>.<methodName>` for behavior scoped to one of several public operations.
Render a unit SUT reference as `<ClassName>` for class-wide behavior, as `<ClassName>.<methodName>` for method-scoped behavior, or as the exact top-level function name from actual code or supplied design.
For behavior specific to one polymorphic variant, append `, <exact variant reference>` inside the SUT parentheses.
Do not append the SUT reference when the exact parenthesized suffix is already present.
Treat the materialized SUT reference as a required coding anchor, not as an incidental technical detail to abstract away.
