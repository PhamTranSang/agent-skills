# Spring Config Guidance

Use this file when the task is about externalized configuration, configuration properties, profiles, or environment-specific settings.

## Externalized Configuration

- Prefer `@ConfigurationProperties` for grouped settings with structure and defaults.
- Keep environment-specific values out of code and inside configuration.
- Use profiles for deployment variants, not for hiding core business rules.
- Make required configuration fail fast and clearly.

## Bootstrap Concerns

- Keep application bootstrap separate from runtime feature wiring.
- Use configuration classes to expose only the settings and beans that need to be explicit.
- Keep secrets and infrastructure endpoints outside source-controlled defaults.

## Practical Triggers

- Use this file when adding new properties, changing startup behavior, or wiring environment-specific beans.
