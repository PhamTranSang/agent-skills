# Implementation Standards

- Keep components focused and composable.
- Prefer framework-native patterns and existing local abstractions.
- Use TypeScript types to model component contracts and data shapes clearly.
- Keep state as local as practical; introduce shared state only when it removes real coordination complexity.
- Handle loading, empty, error, disabled, and optimistic states when the workflow needs them.
- Preserve accessibility: semantic HTML, keyboard support, focus management, labels, contrast, and ARIA only when appropriate.
- Keep UI responsive without relying on fragile viewport-only font scaling.
- Avoid introducing dependencies unless they solve a real problem and fit the project.
- Keep edits scoped to the requested behavior.
- For generated large UIs, keep the screen visually complete but structurally maintainable.
- Prefer real UI controls over explanatory text. The app should show usable workflows, not describe them.
