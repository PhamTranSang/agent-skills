# Stack Intake and Setup Options

When the user provides a backend Java stack for a new project, scaffold, major setup, or ambiguous implementation request, present concise options before coding. Ask only for decisions that are not already determined by an existing project.

Keep the option set short and recommend defaults from the user's constraints:

- Build tool: Maven, Gradle Groovy DSL, Gradle Kotlin DSL.
- Project shape: single module, Maven multi-module, Gradle multi-project, JPMS modules.
- Shared build logic: Maven parent/BOM, Gradle convention plugins in `build-logic`, `buildSrc` only for small/local shared logic.
- Framework: plain Java library, Spring Boot, Spring Web/WebFlux, Micronaut, Quarkus, or existing project framework.
- Data/integration: JDBC/JPA, Spring Data, jOOQ, Flyway/Liquibase, messaging, HTTP client, or none.
- Testing: JUnit 5, Mockito, AssertJ, Testcontainers, Spring Boot test slices, integration tests.
- Build performance: Gradle local build cache, remote cache, configuration cache, parallel builds, Maven wrapper/parallel builds where appropriate.
- Build/bootstrap shape: wrapper scripts, toolchains, CI build mode, Dockerized build, legacy Ant bridge, or plain local invocation.

Example:

```text
Trước khi implement/setup, mình cần chốt vài option: Maven hay Gradle? Nếu Gradle thì Groovy hay Kotlin DSL? Single module hay multi-module? Shared build logic dùng build-logic hay buildSrc? Có bật Gradle build cache/configuration cache không? Có cần wrapper/toolchains/Docker/Ant bridge không?
```

If the user asks to "choose for me", select the simplest stack that satisfies the requirements and state the choice briefly.
