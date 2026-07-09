# Library Contract

Use this file with `module-boundaries.md` when the task affects exported packages, module exports, or API layering.

## Public Surface

- Treat public APIs as contracts.
- Keep the API surface small enough that module boundaries stay understandable and stable.
- Prefer clear overloads and names over clever shortcuts.
- Keep implementation packages out of exported public surface unless the project already exposes them.
- In JPMS projects, keep exports deliberate and reflective opens narrow.

## Extension Model

- Use `interface` for open contracts where callers can provide their own implementation.
- Use an abstract base class only when there is shared behavior that would otherwise be duplicated.
- Use `sealed` types when the allowed implementations are known and exhaustive handling is desirable.
- Use a functional interface when the extension point is small and behavior-oriented.
- Prefer factories or builders over public constructors when creation rules or invariants matter.

## Error And Compatibility Model

- Keep exceptions useful for callers: distinguish malformed input, unsupported features, validation failures, verification failures, and state errors when relevant.
- Preserve binary/source compatibility when the library already has consumers or versioning expectations.
- Keep dependencies minimal and intentional.
- Avoid returning implementation types from exported APIs unless the implementation type is itself part of the contract.

## Contract Testing

- Add or adjust tests around public behavior, edge cases, and compatibility-sensitive flows.
- Test extension points through the exported contract, not through internal implementation details.
- Protect compatibility-sensitive APIs with regression tests before changing signatures or semantics.
