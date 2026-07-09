# React State Management

Use this file when the task is about choosing or implementing state libraries in a React app.

## Selection Heuristics

- Prefer TanStack Query for remote-data orchestration, background refresh, retries, pagination, and cache invalidation.
- Prefer Redux Toolkit when multiple features need predictable shared state transitions, middleware, or event-like workflows.
- Prefer React Context for stable low-frequency shared state such as auth metadata, theme, or UI shell coordination.
- Prefer Apollo when GraphQL is the primary transport and normalized cache behavior matters.
- Prefer MobX only when the project already depends on it or the observable model is an intentional design choice.

## Anti-Patterns

- Do not use Redux Toolkit just to fetch server data if TanStack Query would solve the problem more directly.
- Do not use Context as a high-frequency global store when updates would rerender too much of the tree.
- Do not introduce Apollo just for occasional GraphQL calls without a broader GraphQL caching need.
