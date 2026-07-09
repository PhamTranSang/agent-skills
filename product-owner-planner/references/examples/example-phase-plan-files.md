# Example: Phase Plan Files

## User input

> Create the phase 2 plan for the project.

## Expected output shape

```text
phase-2/
  README.md
  p0-security/
    story-1-refresh-session.md
    task-1-redirect-on-expiry.md
  p1-core-flow/
    story-1-review-pending-documents.md
    task-1-status-query-support.md
  p2-observability/
    task-1-audit-event-logging.md
    spike-1-clarify-permission-rules.md
```

## README.md summary only

- problem summary
- goals
- scope
- non-goals
- assumptions
- dependencies
- risks and mitigations
- open questions
- handoff notes for `engineering-mentor`

## Ticket files

Each file should focus on one ticket and include:

- title
- description
- scenario
- acceptance criteria
- estimate or priority when relevant
