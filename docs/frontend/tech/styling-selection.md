# Styling Selection

Use this file when choosing a styling approach or deciding whether to keep or change the current styling system.

## Decision Guide

- Prefer the existing project styling architecture unless it is actively blocking the requested change.
- Prefer CSS modules or scoped component styles when local encapsulation matters.
- Prefer Tailwind when rapid composition, utility-first workflows, or generated polished UI matter.
- Prefer a UI library style system when the project already depends on MUI or Ant Design and behavior-heavy components are common.

## Shared Rules

- Keep design tokens, spacing, color, and typography decisions centralized.
- Keep responsive rules explicit and maintainable.
- Prefer accessible contrast, focus states, and predictable interaction styling over visual cleverness.

## Detail Routing

- Use `tailwind.md` for Tailwind-specific setup and conventions.
- Use `ui-libraries.md` for Material UI, Ant Design, or design-system-library choices.
