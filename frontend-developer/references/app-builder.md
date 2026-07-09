# v0-Like App Builder Mode

Use this file when the user asks for a full page, dashboard, landing page, SaaS UI, admin tool, ecommerce screen, internal tool, prototype, or "build me an app/site" request.

Use when the user asks for a full page, dashboard, landing page, SaaS UI, admin tool, ecommerce screen, internal tool, prototype, or "build me an app/site" request.

## Workflow

1. Extract product intent: audience, primary workflow, pages/screens, data shown, actions, and visual tone.
2. Ask stack intake options only when choices are missing and materially affect the app.
3. Choose a default stack when the user asks to choose for them.
4. Build the actual usable screen/app as the first view, not a marketing explanation page unless the request is specifically for a landing page.
5. Create realistic states: loading, empty, error, selected/active, disabled, and responsive layouts where relevant.
6. Use realistic sample data when backend data is unavailable.
7. Start the local frontend dev server using the detected stack when current user preferences allow it.
8. Inspect the local preview with browser/screenshot tooling when available and permitted.
9. Fix layout, accessibility, responsiveness, and interaction issues found during inspection.
10. Finish with the local URL, changed files, and any checks skipped due to permission limits.

## Local Preview

When dev-server start is allowed, prefer the project's package manager:

```bash
pnpm dev
npm run dev
yarn dev
bun run dev
```

Do not run install, build, test, lint, typecheck, Playwright, Cypress, validation, deployment, or destructive commands unless the user explicitly permits them for the task.

## Default Choices

- React SPA: Vite + TypeScript + CSS modules or Tailwind, depending on design-system needs.
- React full-stack/product app: Next.js when routing, SSR, server components, or app-level conventions matter.
- Angular app: Angular CLI/Nx depending on whether it is single app or monorepo.
- Vue SPA: Vite + Vue + TypeScript; Nuxt when SSR/routing conventions matter.
- Multi-app frontend platform: Nx when strong project graph/generators/enforced boundaries matter; Turborepo when package-script orchestration and cache are enough.
