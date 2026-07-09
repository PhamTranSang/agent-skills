# Gradle Multi-Project Details

Use this file when the task is about Gradle multi-project structure, shared build logic, or module-level build conventions.

## Build Shape

- Preserve the existing DSL: Groovy `build.gradle` or Kotlin `build.gradle.kts`.
- Keep root build files thin; put reusable logic in convention plugins instead of copying config across subprojects.
- For multi-project builds, prefer convention plugins for repeated configuration and `build-logic` for larger shared build logic.
- Use `buildSrc` mainly for small, local build logic where its rebuild and configuration impact is acceptable.
- Align Java toolchains, test setup, compiler options, publishing, and quality plugins through shared conventions.
- Prefer version catalogs or the repo's established convention for dependency versions.

## Useful Patterns

- Prefer precompiled or binary convention plugins over ad hoc cross-project configuration when a pattern repeats across modules.
- Use lazy task configuration and task configuration avoidance where possible.
- Keep dependency constraints and version alignment in one place rather than sprinkling overrides across subprojects.
- Model shared build behavior as a plugin when the same setup is applied to multiple modules or feature groups.

## Practical Triggers

- Use this file when a build needs to be organized around shared conventions, repeated configuration, or module-by-module build customization.
- Use it before deciding between `build-logic`, `buildSrc`, or per-module build script duplication.
