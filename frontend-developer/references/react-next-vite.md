# React, Next.js, And Vite

Use this file when the task is about React component behavior, Next.js app structure, or Vite-based frontend implementation.

## React

- Prefer function components and hooks.
- Avoid unnecessary global state.
- Memoize only when there is a real render or identity problem.
- Keep effects narrow and avoid deriving state in effects when it can be computed during render.
- Avoid boolean prop proliferation for complex behavior; prefer explicit variants or composition.
- Use compound components for complex shared UI state when it improves API clarity.
- Lift state into a provider only when sibling coordination or component API flexibility requires it.
- Keep provider interfaces explicit: state, actions, and metadata should be easy to test and replace.

## React/Next Performance

- Avoid async waterfalls: start independent requests early, use `Promise.all` for independent work, and put `await` close to the branch that needs it.
- Keep bundles small: avoid unnecessary barrel imports, prefer direct imports, dynamically import heavy UI, and defer third-party scripts.
- For server-rendered apps, minimize data serialized to client components and avoid mutable request state in module scope.
- For client data fetching, deduplicate requests and avoid duplicate global event listeners.
- Reduce re-renders by deriving state during render where practical, using primitive dependencies, and not defining components inside components.
- Use transitions/deferred values for non-urgent UI updates when it materially improves responsiveness.
- Use resource hints, image dimensions, lazy loading, and route-level splitting where the framework supports them.

## Next.js

- Follow existing App Router or Pages Router conventions.
- Keep server/client component boundaries deliberate.
- Authenticate server actions like API routes.
- Avoid passing large duplicated serialized data into client components.
- Keep route-level data fetching parallel where possible.

## Vite

- Follow existing Vite app/library mode.
- Keep aliases aligned with TypeScript config.
- Avoid adding plugins unless the framework or feature requires them.
