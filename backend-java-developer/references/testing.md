# Java Backend Testing

- Prefer JUnit 5 as the default when the project already uses it or has no established alternative.
- Use AssertJ for expressive assertions when already present or acceptable.
- Use Mockito for narrow unit-level collaboration tests, not to recreate the whole application graph.
- Use Testcontainers for integration tests that depend on real infrastructure behavior.
- In Spring Boot, use test slices when they reduce context size and match the behavior under test.
- Add negative tests for security-sensitive, validation-sensitive, and parser/codec behavior.
- Keep tests close to public behavior for libraries and close to use cases for backend services.
- Do not run test commands unless current user preferences permit command execution for that task.
