# Spring Security Guidance

Use this file when the task is about authentication, authorization, security filters, or method security.

## Security Boundary

- Keep security concerns explicit and separate from domain logic.
- Prefer a clear authentication flow and a clear authorization model rather than hiding both in the same layer.
- Keep controller and service code free of ad hoc permission checks when a security layer can own the rule.

## Configuration And Flow

- Use the security filter chain deliberately and keep the entry points readable.
- Prefer method security for fine-grained authorization that belongs to the application layer.
- Keep stateless and stateful setups explicit; do not mix them without a clear reason.

## Practical Triggers

- Use this file when adding login, JWT, session, OAuth2, role checks, or endpoint protection.
