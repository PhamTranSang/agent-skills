# Vue And Nuxt

Use this file when the task is about Vue Composition API, Nuxt routing, SSR boundaries, or Vue-specific state conventions.

## Structure

- Prefer Composition API if the project uses it.
- Keep props and emits explicit.
- Avoid mutating props.
- Keep composables focused on reusable behavior.

## Routing And State

- Follow existing Nuxt file-based routing, plugins, middleware, and server route conventions.
- Keep SSR/client-only boundaries explicit in Nuxt.
- Prefer local component state first; use Pinia when shared state is genuinely needed across features.
- Keep store shape and composables aligned with the project's existing pattern.

## Interaction

- Use framework-native transitions and accessibility patterns when adding interaction.
