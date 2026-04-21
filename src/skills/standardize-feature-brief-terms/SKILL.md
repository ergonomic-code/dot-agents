---
name: standardize-feature-brief-terms
description: Standardize terminology in a feature brief or subfeature brief by extracting canonical domain terms, resolving inconsistent variants, and appending or refreshing a final `## Термины` section in the brief file. Use when the user asks to normalize wording in a brief, add a glossary, or make business terms consistent before further analysis.
---

# Standardize Feature Brief Terms

Read only the target brief and sources the user explicitly names as terminology authority.
If the user points to an authority file, prefer its terms over the brief's local wording.
Edit the brief file in place.

## Workflow

1. Extract stable domain terms, actor names, entity names, and recurring business phrases from the brief.
2. Group aliases, abbreviations, transport-level names, and paraphrases that denote the same concept.
3. Choose one canonical term per concept.
4. Add or update a final `## Термины` section at the end of the brief.

## Canonicalization Rules

Prefer user-provided authority terms.
Otherwise prefer the explicit term already dominant in the brief.
Prefer domain wording over UI-local, request-parameter, field, table, or implementation wording.
Keep different concepts separate even if the words are similar.
Do not invent new concepts, rules, or definitions.
Do not rewrite the main brief body unless a purely mechanical term replacement is clearly required by the new glossary.
Keep quoted paths, code identifiers, schema symbols, and document titles unchanged.

## `## Термины` Format

Place the section after the existing last section of the file.
List one bullet per concept.
Use the form ``- `Каноничный термин` — short domain meaning. Не использовать: `variant 1`, `variant 2`.``.
Omit `Не использовать` when there are no meaningful conflicting variants to freeze.
Include only terms that are used in the brief or needed to disambiguate it.
Keep definitions short and business-facing.

## Stop Conditions

Stop and report issues instead of guessing when:
- two variants may denote different concepts;
- authority sources conflict materially;
- the brief is too vague to choose a canonical term safely.

## Before Finishing

Check that:
- `## Термины` is the final section;
- each bullet defines one concept;
- canonical terms are consistent with the chosen authority;
- banned variants were actually observed in the brief or authority sources;
- definitions stay short and do not add new requirements.

## Output

Apply the file edit.
If a stop condition is hit, return only a short issue list.
