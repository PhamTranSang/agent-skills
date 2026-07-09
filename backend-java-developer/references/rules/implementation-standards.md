# Implementation Standards

- Use modern Java idioms where they improve clarity.
- Do not introduce frameworks or dependencies unless they solve a real problem and fit the existing project.
- Keep boundaries clear: API vs implementation, domain vs infrastructure, controller vs service vs repository.
- Make invalid states hard to represent when practical.
- Prefer explicit errors and domain-specific exceptions over broad runtime failures.
- Keep security-sensitive code conservative: validate inputs, avoid unsafe defaults, and add negative cases.
- Keep edits scoped to the requested behavior.
