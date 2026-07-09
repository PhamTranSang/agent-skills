# React Routing

Use this file when the task is about routing in React apps outside Next.js.

## Routing Model

- Prefer React Router for multi-view client-rendered React apps.
- Keep route objects, nested layouts, loaders, and navigation conventions aligned with the existing app.
- Keep route-level code splitting explicit when it materially improves startup performance.

## Design Rules

- Place route concerns close to feature boundaries when the app is package-by-feature.
- Keep navigation state and route params typed and easy to trace.
- Do not over-abstract route definitions unless the project already uses a routing wrapper intentionally.
