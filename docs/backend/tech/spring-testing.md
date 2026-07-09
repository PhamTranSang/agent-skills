# Spring Testing Guidance

Use this file when the task is about Spring-specific tests, test slices, or integration testing strategy.

## Test Levels

- Prefer the smallest test slice that still exercises the behavior under test.
- Use `@SpringBootTest` when the wiring itself is the thing being validated.
- Use controller, repository, and other slices when the scope is narrow and the boot cost would otherwise be too high.

## Test Design

- Keep contract tests close to public behavior.
- Test security, validation, and persistence behavior with realistic failure cases.
- Prefer integration tests for wiring-heavy behavior and slice tests for focused framework behavior.

## Practical Triggers

- Use this file when adding a new endpoint, repository flow, security rule, or wiring behavior that needs Spring context support.
