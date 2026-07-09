# Spring Messaging Guidance

Use this file when the task is about events, async messaging, broker integration, or messaging-based coordination.

## Messaging Model

- Use application events when the coordination stays inside the same deployable unit.
- Use broker-backed messaging when the integration must survive process boundaries.
- Keep message payloads explicit and version-aware.

## Reliability Concerns

- Make retries, idempotency, and failure handling explicit.
- Keep producer and consumer responsibilities separate.
- Prefer an outbox or equivalent reliability pattern when a business event must not be lost.

## Practical Triggers

- Use this file when adding event listeners, message handlers, queue/topic publishers, or broker integration code.
