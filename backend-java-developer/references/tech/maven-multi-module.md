# Maven Multi-Module Details

Use this file when the task is about Maven multi-module structure, reactor behavior, or module split decisions.

## Module Shape

- For multi-module builds, use a parent/aggregator POM with `<modules>` and keep module dependencies explicit.
- Split modules by stable domain or platform boundaries, not by every technical layer by default.
- Avoid cyclic dependencies.
- Keep API modules small and dependency-light.

## Reactor Behavior

- Treat the reactor as the core ordering mechanism for multi-module builds.
- Use module order intentionally, but rely on dependency relationships for correctness.
- Keep module dependencies and build order easy to read from the root build.

## Practical Triggers

- Use this file when deciding whether a domain should become a separate module.
- Use it when a root build is already multi-module or is about to become one.
