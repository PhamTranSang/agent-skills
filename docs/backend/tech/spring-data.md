# Spring Data Guidance

Use this file when the task is about repositories, persistence mapping, JPA, custom queries, or transaction boundaries.

## Repository Model

- Use Spring Data repositories for straightforward persistence.
- Use custom repositories or jOOQ when query shape, control, or performance needs go beyond derived queries.
- Keep repository interfaces focused on persistence access, not business orchestration.

## Mapping And Transactions

- Keep persistence entities separate from API DTOs when the API is public or expected to evolve.
- Keep transaction boundaries explicit and close to use cases.
- Make locking and consistency semantics visible in the code.
- Use schema migrations consistently when the persistence model changes.

## Practical Triggers

- Use this file when introducing a new entity, repository, query method, transactional flow, or migration.
