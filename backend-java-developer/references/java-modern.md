# Modern Java Backend Implementation

- Use records for transparent immutable data carriers when behavior is minimal.
- Use sealed types for closed hierarchies where exhaustive handling matters.
- Use pattern matching where it improves clarity.
- Use `var` only for local obvious types.
- Prefer immutable collections and defensive copies at boundaries.
- Keep null handling explicit; use `Optional` for return values where absence is expected, not for fields or parameters by default.
- Keep domain errors explicit and avoid broad runtime failures.
- Validate inputs at boundaries and avoid unsafe defaults.
- Avoid leaking infrastructure concerns into domain or API layers.
- Keep dependency direction clean and avoid cycles.
