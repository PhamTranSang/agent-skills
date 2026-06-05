# Build Tooling And Monorepos

## Vite

- Inspect `vite.config.*`, plugin setup, aliases, env handling, test config, and library/app mode before changing config.
- Keep aliases aligned with TypeScript config.
- Avoid adding plugins unless the framework or feature requires them.

## Package Managers And Workspaces

- Detect npm, pnpm, yarn, or bun from lockfiles and `packageManager`.
- Preserve workspace layout and script conventions.
- When adding packages, choose the correct workspace/package target and dependency type.

## Nx

- Respect project boundaries, generators, executors, named inputs, targets, tags, and dependency constraints.
- Prefer existing Nx conventions before adding custom scripts.
- Use Nx when strong project graph, generators, affected builds, or enforced boundaries matter.

## Turborepo

- Respect `turbo.json` pipeline/tasks, cache inputs/outputs, package scripts, and workspace boundaries.
- Keep shared packages buildable and dependency direction clean.
- Use Turborepo when package-script orchestration and cache are enough.
