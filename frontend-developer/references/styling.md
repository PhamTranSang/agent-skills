# Styling And UI Libraries

## CSS, SCSS, Sass

- Follow the project's existing styling architecture: global styles, CSS modules, component styles, utility classes, or design tokens.
- Keep selectors scoped and avoid broad global overrides unless the project already uses them intentionally.
- Prefer variables/tokens/mixins that already exist before adding new color, spacing, or typography values.
- Keep responsive rules explicit and maintainable.

## Tailwind CSS

- Use existing Tailwind config, theme tokens, plugins, and class ordering conventions.
- Prefer design-system components or composed utility patterns when they already exist.
- Avoid arbitrary values unless they reflect a one-off design constraint that cannot be represented by tokens.
- When setting up Tailwind, configure the correct content paths, PostCSS integration, framework adapter, and base stylesheet imports.
- For v0-like generation, Tailwind plus a component primitive system is a strong default when the user wants fast polished UI and has not chosen MUI/Ant Design.

## Material UI

- Use the existing `ThemeProvider`, theme tokens, variants, slots, and `sx`/styled conventions.
- Prefer MUI components for behavior-heavy UI instead of recreating accessible primitives manually.
- Keep overrides centralized when the project has a theme customization pattern.

## Ant Design

- Use existing `ConfigProvider`, theme tokens, form/table/modal conventions, and icon usage.
- Prefer Ant Design primitives for complex enterprise UI patterns when the project already depends on Ant Design.
- Keep custom CSS overrides narrow and stable.
