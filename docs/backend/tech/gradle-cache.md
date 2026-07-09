# Gradle Cache Details

Use this file when deciding whether Gradle cache or configuration cache is worth enabling and how to roll it out.

## What To Enable

- Use the Gradle Wrapper and keep wrapper-based commands as the default invocation path.
- Enable the build cache when tasks are cacheable, outputs are reproducible, and the team rebuilds the same work often.
- Consider configuration cache for larger builds after verifying custom tasks and plugins are compatible.

## When It Is Worth It

- Add build cache when repeated CI or local builds spend meaningful time on the same tasks and the outputs are deterministic.
- Add configuration cache when configuration time is a visible bottleneck and the build logic is compatible.
- Keep remote build cache conservative: enable it only when trust, reproducibility, cache-key hygiene, CI policy, and artifact sensitivity are understood.

## How To Roll It Out

1. Keep the build wrapper in place first.
2. Make task outputs reproducible and inputs explicit.
3. Remove hidden environment coupling from build scripts and plugins.
4. Verify custom tasks, task graph wiring, and plugins before enabling configuration cache broadly.
5. Use CI to validate cache behavior, then expand to team usage.

## Failure Modes To Watch

- Non-reproducible tasks that claim to be cacheable.
- Build logic that reads environment state during configuration.
- Custom plugins that break configuration cache compatibility.
- Remote cache reuse across contexts that should not share build artifacts.
