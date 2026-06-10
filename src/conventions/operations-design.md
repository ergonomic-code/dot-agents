# Operations design

## Balanced form

- Use balanced form for non-trivial operations that mix input, calculation, or output responsibilities.
- Read branch roots are queries that obtain inputs from resources, repositories, services, protocols, files, clocks, random sources, or other external dependencies.
- Calculate branch roots are pure queries over explicit logical inputs.
- Write branch roots are commands that apply already decided result data to resources, repositories, services, protocols, files, or other external dependencies.
- Prefer completing reads before calculations and writes after calculations.
- Keep exceptions to read-calculate-write order explicit and confined.
- Keep costly dependency calls out of calculate branches.
- Keep complex classification, localization, aggregation, filtering, default selection, and domain decisions out of read and write branches.
- If a dependency adapter must map protocol data, keep that mapping local and decision-free.
- If a renderer, exporter, serializer, or view builder is only output assembly, treat it as a write-side humble object and pass ready display data explicitly.
