# State Management Selection

Use this file when deciding whether the app needs local state only, shared client state, server-cache tooling, or GraphQL-focused data state.

## Decision Guide

- Keep state local by default.
- Prefer TanStack Query when the main problem is server data fetching, cache synchronization, invalidation, and background refresh.
- Prefer Redux Toolkit when the app needs shared client state, explicit event flow, middleware, or broad cross-feature coordination.
- Prefer Apollo when the app is already GraphQL-first and normalized GraphQL caching is central to the product.
- Prefer MobX only when the project already uses it or the team intentionally wants observable mutable models.
- Prefer React Context for low-frequency shared configuration or lightweight coordination, not high-churn app-wide state.

## Routing To Detail

- Use `react-state.md` for React-specific trade-offs among TanStack Query, RTK, Context, Apollo, and MobX.
- Use framework-specific files for Vue and Angular state guidance.
