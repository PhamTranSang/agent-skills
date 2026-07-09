# Spring Core Guidance

Use this file when the task is about the Spring container, bean lifecycle, component scanning, or dependency injection.

## Core Container

- Prefer constructor injection for required dependencies.
- Keep `@Component` scanning aligned with the project package structure and feature boundaries.
- Use `@Configuration` and `@Bean` for explicit wiring that should stay visible.
- Use `@Profile` and conditional config only when the behavior genuinely differs by environment or deployment mode.

## Bean Design

- Keep beans small and role-focused.
- Prefer stateless beans unless the state is a real part of the contract.
- Use lifecycle hooks sparingly and only when initialization or cleanup needs to be explicit.
- Avoid making the container hide domain decisions that should stay in application code.

## Practical Triggers

- Use this file when introducing shared wiring, custom factory methods, conditional beans, or container-managed collaborators.
