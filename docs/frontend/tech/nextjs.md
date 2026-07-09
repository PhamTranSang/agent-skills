# Next.js

Use this file when the task is about Next.js routing, server/client boundaries, data loading, or runtime conventions.

## Structure

- Follow the existing App Router or Pages Router conventions; do not mix models casually.
- Keep server/client component boundaries deliberate and small.
- Authenticate server actions like API routes.
- Keep route-level data fetching parallel where possible.

## Runtime Concerns

- Minimize serialized data passed into client components.
- Avoid mutable request state in module scope.
- Use framework-native loading, error, and not-found conventions when available.

## When To Escalate Choice

- Ask for confirmation before moving a Vite SPA or plain React app into Next.js.
- Ask for confirmation before introducing SSR or server actions into a project that is currently purely client-rendered.
