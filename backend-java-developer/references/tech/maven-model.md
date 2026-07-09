# Maven Model and Plugin Control

Use this file when the task is about `dependencyManagement`, `pluginManagement`, lifecycle bindings, or version alignment.

## Dependency And Plugin Control

- Use `dependencyManagement` to centralize dependency versions while still declaring actual dependencies in modules.
- Use `pluginManagement` to centralize plugin versions and config while applying plugins where needed.
- Keep plugin configuration explicit at the module that uses the plugin unless the setting is truly shared.
- Prefer standard lifecycle phases over custom execution chains when a built-in phase already matches the need.

## Useful Patterns

- Keep version alignment in one place rather than scattering overrides across modules.
- Treat plugin bindings as part of the build model, not as incidental configuration.
- Use Maven plugins deliberately instead of inventing custom shell glue when an existing plugin already covers the workflow.

## Practical Triggers

- Use this file when a task is about dependency inheritance, plugin defaults, lifecycle bindings, or version management.
- Use it when the build needs reproducible plugin behavior across modules.
