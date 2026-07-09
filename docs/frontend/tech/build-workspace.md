# Build And Workspace

Use this file when the task is about package managers, workspaces, Nx, Turborepo, or broader frontend workspace topology.

## Package Managers

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
