# UI Libraries

Use this file when the task is about choosing or working within Material UI, Ant Design, or an existing design-system library.

## Material UI

- Use the existing `ThemeProvider`, theme tokens, variants, slots, and `sx` or `styled` conventions.
- Prefer MUI components for behavior-heavy UI instead of recreating accessible primitives manually.
- Keep overrides centralized when the project already has a theme customization pattern.

## Ant Design

- Use existing `ConfigProvider`, theme tokens, form/table/modal conventions, and icon usage.
- Prefer Ant Design primitives for complex enterprise UI patterns when the project already depends on Ant Design.
- Keep custom CSS overrides narrow and stable.

## Selection Guide

- Prefer MUI when the team wants strong theming, composability, and React-centric extensibility.
- Prefer Ant Design when the app leans toward data-heavy enterprise workflows and the project already fits its interaction patterns.
