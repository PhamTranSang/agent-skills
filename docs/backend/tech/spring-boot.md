# Spring Boot

Use this file with `spring-framework.md` when the task is about application bootstrapping, runtime wiring, or web/persistence integration.

## Application Structure

- Follow existing controller/service/repository/configuration conventions.
- Keep controllers thin and push business logic into services.
- Prefer constructor injection.
- Use configuration properties for environment-dependent values.
- Keep transaction boundaries explicit and close to use cases.
- Validate request DTOs at the boundary.
- Avoid leaking persistence entities through public API responses unless the project already intentionally does so.

## Web And Integration

- Keep REST DTOs separate from persistence entities when the API is public or expected to evolve.
- Use Spring WebFlux only when the project already uses reactive patterns or the requirement justifies it.
- Keep HTTP client, messaging, and persistence adapters behind clear service boundaries.
- Centralize cross-cutting concerns such as error handling, security, logging, and tracing using existing project patterns.

## Data

- Use Spring Data repositories for straightforward persistence; use jOOQ or custom repositories when query shape/control warrants it.
- Use Flyway or Liquibase consistently when schema migrations are part of the project.
- Keep transaction and locking semantics visible for concurrency-sensitive flows.
