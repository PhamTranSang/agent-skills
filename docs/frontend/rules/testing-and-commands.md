# Frontend Testing Addendum

Extend the shared testing rules with this workflow assumption:

- prefer Jest/RTL or the project-default frontend runner for component and interaction tests
- use Playwright/Cypress when browser workflows or page-to-page behavior matter
- the user permits running frontend dev-server start scripts and browser/screenshot inspection for local UI review
- other commands still require explicit permission
