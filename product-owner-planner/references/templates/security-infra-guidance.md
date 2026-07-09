# Security / Infra Guidance

When the feature touches auth, permission, token, config, redirect, or integration boundaries, include:

- hidden dependencies
- config or environment tasks
- integration and regression checks
- explicit 401 / 403 / failure-path behavior
