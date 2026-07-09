# Modern Java Backend Implementation

Use this file with `module-boundaries.md` when the task affects package layout or dependency direction.

## Implementation Style

- Prefer `record` for immutable data carriers, request/response DTOs, and value objects with simple invariants.
- Prefer `sealed` types when the hierarchy is closed and exhaustive handling matters.
- Use pattern matching when it makes control flow flatter and easier to read.
- Use `var` only when the type is obvious from the right-hand side and the local scope stays readable.
- Prefer immutable collections and defensive copies at boundaries.
- Keep null handling explicit; use `Optional` for return values where absence is expected, not for fields or parameters by default.
- Keep domain errors explicit and avoid broad runtime failures.
- Validate inputs at boundaries and avoid unsafe defaults.

## Design Pattern Selection

- Use `Strategy` when one behavior varies by policy, algorithm, or rule and the caller should not know the details.
- Use a `Factory` when object creation has meaningful rules, dependencies, or invariants.
- Use `Builder` when an object has many optional arguments or creation order matters.
- Use `Adapter` when a legacy or external API must fit an internal boundary.
- Use `Facade` when a subsystem is too noisy for the caller and a simpler entry point is useful.
- Use `Decorator` when you need to add behavior without changing the core contract.
- Use `Command` when an action should be queued, retried, logged, or audited as a unit.
- Use `Chain of Responsibility` only when the request naturally passes through independent stages that may stop early.

## Functional Alternatives

- Prefer a functional interface when the variation point is small, stateless, and easy to name.
- Use `Function`, `Supplier`, `Consumer`, or `Predicate` when the generic type already communicates enough.
- Define a custom functional interface when the callback is part of the domain vocabulary or needs a clearer semantic name.
- Avoid lambda-based APIs when the behavior is long-lived, stateful, or important enough that a named class reads better.
- Use a small class instead of a callback when the logic needs test seams, branching, or richer state.

## Clean Code Rules

- Favor names that describe intent, not implementation details.
- Keep method names action-oriented and boolean methods in `is/has/can/should` form.
- Split methods when a block has multiple responsibilities, nested branching, or repeated temporary variables.
- Extract a class when a group of methods shares a responsibility or lifecycle.
- Apply SOLID, KISS, DRY, and YAGNI as decision checks, not slogans:
  - `SOLID` when boundaries or extension points are getting hard to reason about.
  - `KISS` when a simpler shape still preserves the required behavior.
  - `DRY` only when the repeated code has the same meaning, not just similar syntax.
  - `YAGNI` when an extension point has no evidence yet.

## Boundary Awareness

- Keep dependency direction clean and avoid cycles.
- Avoid leaking infrastructure concerns into domain or API layers.
- Prefer idioms that make boundaries obvious rather than idioms that compress code at the cost of architectural clarity.
