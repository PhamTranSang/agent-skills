# Routing Selection

Use this file when deciding how routing should work in a frontend app or when the app may move between framework-native routing and library routing.

## Decision Guide

- Prefer framework-native routing when using Next.js, Nuxt, or Angular because routing is part of the framework contract.
- Prefer React Router in plain React/Vite apps that need client-side routing.
- Keep route conventions close to the framework defaults unless the project already has a strong custom abstraction.

## Practical Triggers

- Ask for confirmation before introducing client-side routing into a currently single-view app.
- Ask for confirmation before replacing framework-native routing with a third-party router.
