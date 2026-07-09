# Module Boundaries

Use this file when the task is about feature-first structure, clean/onion/hexagonal boundaries, or deciding when to split modules.

Treat this file as the structural contract for the project. Read it before making package, module, or export decisions, and keep `java-modern.md` and `library-contract.md` aligned with it.

## Default Direction

- Split modules by stable domain or platform boundaries, not by every technical layer by default.
- Avoid cyclic dependencies.
- Keep API modules small and dependency-light.
- Put integration adapters behind clear interfaces when the domain needs independence.
- In JPMS projects, update `module-info.java` as part of any new exported API, required dependency, or reflective framework access.

## Feature-Oriented Structure

- Prefer a feature-first modular monolith when the codebase is still one deployable unit but the domains are distinct.
- Inside each feature, use clean layered boundaries: entrypoints, application/use cases, domain, and adapters.
- Keep dependencies flowing inward; infrastructure depends on domain, not the other way around.
- Move shared code into a small shared kernel only when it is truly stable and broadly needed.
- Keep the package structure aligned to features first, not technical layers first, when the project needs domain clarity.

## Feature-First Package Layout

- Prefer a `feature/api` and `feature/impl` split inside each bounded feature when it helps implementation stay simple and explicit.
- Put DTOs and service interfaces in `api`, and controllers, repositories, entities, mappers, and service implementations in `impl`.
- Keep cross-cutting shared code in small `common/api` and `common/impl` packages only when multiple features really need it.
- This layout is a good default when the project is one deployable unit and the team wants fast, low-friction implementation.
- Keep feature names stable and domain-oriented, such as `identity`, `products`, or `catalog`.

## Architecture Mix

- Use Clean Architecture to keep use cases and domain logic independent from frameworks.
- Use Onion/Hexagonal ideas to define ports and adapters around the core.
- Let features own their implementation details, but expose small ports for cross-feature collaboration.
- Prefer one clear boundary model per project; combine patterns only when they reinforce the same dependency direction.
- If the project already has a feature-first layout, preserve it unless the user explicitly asks for a structural rewrite.

## When To Split Further

- Split into separate Gradle or Maven modules when the boundary is stable, the dependency direction is clear, and the module can be built or tested independently.
- Keep feature packages as packages first, modules second, unless the build benefits clearly from separate modules.
- Before splitting modules, confirm the impact on public APIs, build complexity, and test boundaries.
