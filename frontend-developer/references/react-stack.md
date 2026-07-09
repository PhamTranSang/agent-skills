# React Stack

Use this file when the task is about React component behavior, composition, rendering, or React-first application structure.

## Component Model

- Prefer function components and hooks.
- Keep components focused; extract hooks or child components when behavior or rendering branches grow.
- Avoid boolean prop proliferation for complex behavior; prefer explicit variants, composition, or slot-like children.
- Use context only when sibling coordination or extensible component APIs justify shared state.

## Rendering And Performance

- Derive state during render when practical instead of syncing derived state in effects.
- Memoize only when there is a real render cost or unstable identity problem.
- Use transitions or deferred values for non-urgent updates when responsiveness materially improves.
- Avoid defining components inside components when it causes unnecessary remounts or hard-to-follow identity changes.

## Ecosystem Routing

- Use `react-state.md` when the task is about state or data-fetching library choice.
- Use `react-routing.md` when the task is about routing in React apps outside Next.js.
- Use `nextjs.md` when the task touches App Router, server/client boundaries, or Next.js runtime behavior.
- Use `vite.md` when the task touches SPA tooling, aliases, plugins, or dev/build config.
