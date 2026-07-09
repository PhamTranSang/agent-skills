# Bootstrap Details

Use this file when the task is about wrapper scripts, toolchains, CI bootstrap, or legacy build bridges.

## Reproducibility

- Prefer wrapper scripts for Gradle and Maven when the project supports them.
- Keep Java toolchains explicit so local machines and CI use the same language level.
- Make local, CI, and release builds use the same entrypoint where possible.

## Automation And CI

- Treat CI as the reference environment for build behavior, not an afterthought.
- Keep environment-specific values in configuration, not in hard-coded build scripts.
- Prefer a small, boring bootstrap path that new contributors can run without tribal knowledge.

## Legacy Or External Build Bridges

- If the repository still needs Ant-based or other legacy build glue, isolate it behind a dedicated bridge file or plugin instead of mixing it into the core build model.
- Use legacy bridges only when a direct Gradle or Maven plugin path is not practical.
- Document the escape hatch clearly so the main build remains easy to reason about.
