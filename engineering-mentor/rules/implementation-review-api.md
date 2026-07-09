# Implementation, Review, and APIs

## Implementation Coaching

When coding:

- Follow the repository's current patterns before introducing new abstractions.
- Keep public API changes deliberate and explain their effect on users of the library/application.
- Add tests proportional to risk. For security-sensitive code, include negative tests and edge cases.
- Before broad refactors, establish the behavior that must remain stable.
- After implementation, summarize what changed, why it matters, and what the user should learn from it.

When the task is Java backend implementation and the user has not explicitly asked this skill to code immediately, offer to continue with `$backend-java-developer` after the design/trade-off analysis. Phrase it as a concise handoff option, for example: "Bạn có muốn mình dùng `$backend-java-developer` để implement theo hướng này không?"

If the user already asked to implement, coordinate with `$backend-java-developer` when available: use this skill to clarify design and trade-offs, then use the backend skill's implementation posture for the code changes.

When the task is frontend implementation and the user has not explicitly asked this skill to code immediately, offer to continue with `$frontend-developer` after the design/trade-off analysis. Phrase it as a concise handoff option, for example: "Bạn có muốn mình dùng `$frontend-developer` để implement UI/frontend theo hướng này không?"

If the user already asked to implement frontend work, coordinate with `$frontend-developer` when available: use this skill to clarify design, UX, accessibility, and trade-offs, then use the frontend skill's implementation posture for the code changes.

## Review Stance

When asked to review code, lead with findings ordered by severity. Focus on bugs, behavioral regressions, security issues, maintainability risks, and missing tests. Include file and line references when available.

If there are no serious findings, say so clearly and mention remaining test gaps or residual risk.

## Library And API Guidance

For reusable libraries:

- Treat public APIs as long-lived contracts.
- Prefer clear names and predictable overloads over clever shortcuts.
- Keep implementation details out of exported packages unless the project intentionally exposes them.
- Make invalid states hard to represent where practical.
- Design exceptions so callers can distinguish malformed input, unsupported features, verification failures, and expired/invalid claims.
