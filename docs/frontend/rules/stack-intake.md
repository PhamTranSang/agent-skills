# Stack Intake and Setup Options

When the user provides a frontend stack for a new project, scaffold, major setup, or ambiguous implementation request, present concise options before coding. Ask only for decisions that are not already determined by an existing project.

Keep the option set short and use recommendations based on the user's stack:

- Project/workspace: single app, npm/pnpm/yarn workspace, Nx monorepo, Turborepo monorepo.
- Build/framework: Vite, Next.js, Nuxt, Angular CLI, existing framework default.
- Styling: CSS modules/plain CSS, SCSS/Sass, Tailwind CSS, design-system library styles.
- UI library: none/custom components, Material UI, Ant Design, existing design system.
- State/data: framework-local state, TanStack Query, Redux Toolkit/Zustand/Pinia/NgRx, existing project pattern.
- Testing: Vitest/Jest, React Testing Library, Cypress/Playwright, framework default.

Example:

```text
Trước khi implement, mình cần chốt vài option: workspace dùng single app, Nx, hay Turborepo? Build dùng Vite hay framework default? Styling dùng CSS/SCSS hay Tailwind? UI library dùng custom, Material UI, hay Ant Design?
```

If the user asks to "choose for me", select the simplest stack that satisfies the requirements and state the choice briefly.
