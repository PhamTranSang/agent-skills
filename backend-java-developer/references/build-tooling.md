# Maven, Gradle, And Multi-Module Build Tooling

## Gradle

- Preserve the existing DSL: Groovy `build.gradle` or Kotlin `build.gradle.kts`.
- Prefer convention plugins for shared build logic in multi-project builds.
- For larger builds, prefer an included `build-logic` composite build for convention plugins. Use `buildSrc` mainly for small, local build logic where its rebuild/configuration impact is acceptable.
- Keep dependency versions centralized with version catalogs or established project conventions.
- Keep root build files thin; put reusable logic in convention plugins instead of copying config across subprojects.
- Align Java toolchains, test setup, compiler options, publishing, and quality plugins through shared conventions.
- Use Gradle Wrapper when available and preserve wrapper-based commands.
- Consider build cache when tasks are cacheable, outputs are reproducible, and developers/CI frequently rebuild the same work.
- Consider configuration cache for larger builds after verifying custom tasks/plugins are compatible.
- Be careful with remote build cache: enable it only when trust, reproducibility, cache key hygiene, CI policy, and artifact sensitivity are understood.

## Maven

- Preserve standard Maven layout unless the project already has a reason to differ.
- For multi-module builds, use an aggregator/root POM with `<modules>` and keep module dependencies explicit.
- Use `dependencyManagement` to centralize dependency versions while still declaring actual dependencies in modules.
- Use `pluginManagement` to centralize plugin versions/config while applying plugins where needed.
- Prefer Maven Wrapper when the project needs reproducible Maven versions across machines/CI.
- Keep parent POMs focused on shared config; avoid hiding module-specific behavior too deeply.
- Use BOMs for platform dependency alignment when the ecosystem provides them, such as Spring Boot dependency management.

## Module Boundaries

- Split modules by stable domain or platform boundaries, not by every technical layer by default.
- Avoid cyclic dependencies.
- Keep API modules small and dependency-light.
- Put integration adapters behind clear interfaces when the domain needs independence.
- In JPMS projects, update `module-info.java` as part of any new exported API, required dependency, or reflective framework access.
