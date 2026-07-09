# Angular Stack

Use this file when the task is about Angular component structure, forms, routing, DI, RxJS conventions, or Angular-specific state choices.

## Structure

- Prefer clear component/service boundaries.
- Follow the project's standalone component or NgModule convention.
- Keep templates readable and push complex logic into TypeScript.
- Keep dependency injection explicit and avoid service responsibility creep.

## Forms, Routing, And State

- Use reactive forms when the project already uses them or validation complexity warrants it.
- Keep route configuration, guards, interceptors, and providers aligned with the existing project structure.
- Prefer framework-local state first; use NgRx only when the app truly needs shared event-driven state, traceability, or complex side-effect orchestration.
- Keep RxJS usage explicit and aligned with the team's existing subscription and cleanup pattern.

## Tooling

- Use Angular CLI or Nx conventions already present in the repo.
