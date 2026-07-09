# Research And Specs

When the user asks to research a technology, RFC, specification, official documentation, standard, or library behavior before designing or implementing, read the primary source before giving conclusions. Do not rely only on memory for spec-driven work.

When available, coordinate with `$research-engineer` for research-heavy tasks. Use `$research-engineer` to gather sourced findings, then use this skill to turn those findings into design decisions, trade-offs, and a recommended implementation path.

For RFC/JWT/JOSE-style tasks:

- Prefer official RFC text or standards-track sources.
- Identify the exact sections that affect the implementation.
- Separate normative requirements from implementation recommendations.
- Translate spec language into concrete API/model/parser/builder/test implications.
- Call out security-sensitive requirements and Best Current Practice guidance when relevant.

Example: if the user asks to study RFC 7515 to RFC 7519 before designing JWT headers, first read the relevant RFC sections, then propose the header model, required/optional parameters, validation rules, and tests.

For broad framework/library research, expect `$research-engineer` to include official docs, reputable best-practice sources, common errors, classic pitfalls, and version-sensitive notes before this skill gives the final recommendation.
