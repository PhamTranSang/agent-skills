# Coordination With Engineering Mentor

When invoked after `$engineering-mentor`:

1. Treat the mentor's selected approach as the implementation plan.
2. Re-check the relevant code before editing; do not implement from the plan blindly.
3. Preserve the trade-offs and constraints identified by the mentor.
4. If implementation details contradict the mentor plan, explain the mismatch and adapt with the smallest coherent change.

When invoked directly and the task needs design choices, briefly frame the options, choose one, then implement.

If the task touches build tooling, module boundaries, or bootstrap/environment setup, surface the concrete options first and ask for confirmation before changing the structure.
