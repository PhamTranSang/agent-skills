# Frontend Testing Selection

Use this file when deciding how to test frontend behavior or which testing layer matches the requested change.

## Decision Guide

- Prefer component and user-behavior tests for interactive UI logic.
- Prefer framework-native or local defaults unless the project already standardizes on another runner.
- Use Playwright or Cypress when end-to-end workflows, browser behavior, or integration across pages matters.

## Framework Fit

- In React, prefer React Testing Library with the existing test runner unless the project already uses another pattern.
- In Angular or Vue, stay aligned with the framework's established testing setup before adding extra layers.

## Practical Triggers

- Use this file when deciding whether a change needs component tests, integration tests, or browser-level validation.
