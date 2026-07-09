# Framework Selection

Use this file when the user needs help choosing a frontend framework, runtime model, or delivery shape before implementation.

## Decision Guide

- Prefer React when the project needs a broad ecosystem, flexible composition, or team familiarity with component-driven UI.
- Prefer Next.js when routing, SSR, server components, or app-level conventions matter more than bare SPA flexibility.
- Prefer Vite when the project needs a fast SPA or library build with minimal framework ceremony.
- Prefer Angular when the team wants strong framework conventions, integrated DI/forms/routing, or enterprise-scale structure.
- Prefer Vue for a lighter mental model with strong SFC ergonomics; prefer Nuxt when SSR, file routing, or app conventions matter.

## Confirmation Triggers

- Ask for confirmation when switching between SPA and SSR/SSG.
- Ask for confirmation when the user has not chosen between framework conventions and bare-tool flexibility.
- Ask for confirmation before introducing Angular, Next.js, or Nuxt into an existing non-matching app.
