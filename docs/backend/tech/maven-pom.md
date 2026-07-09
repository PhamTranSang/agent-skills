# Maven POM Details

Use this file when deciding how the root POM, parent POM, and per-module POMs should be organized.

## Build Shape

- Preserve standard Maven layout unless the project already has a reason to differ.
- Keep the root POM readable: it should explain the build, not bury it.
- Keep parent POMs focused on shared config; avoid hiding module-specific behavior too deeply.
- Use BOMs for platform dependency alignment when the ecosystem provides them, such as Spring Boot dependency management.

## POM Fundamentals

- A POM is the unit Maven uses to describe the project and how it is built.
- Keep the minimal coordinates explicit: `groupId`, `artifactId`, and `version`.
- Treat inherited defaults as part of the build model, not as magic.
- Prefer explicit build metadata when it helps humans understand the project.

## Practical Triggers

- Use this file when deciding how the root project, parent POM, and module POMs should be structured.
- Use it when the question is about naming, inheritance, repository defaults, or what belongs in the root POM.
