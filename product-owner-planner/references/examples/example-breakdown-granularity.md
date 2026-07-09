# Example: Breakdown Granularity

## User input

> Plan phase 2 for document approval and admin controls.

## Good breakdown

### Milestone folder: `p0-security`

- `story-1-refresh-session.md`
- `task-1-redirect-on-expiry.md`
- `spike-1-clarify-cross-team-permission-rules.md`

### Milestone folder: `p1-core-flow`

- `story-1-review-pending-documents.md`
- `task-1-status-query-support.md`
- `task-2-approval-audit-log.md`

## Why this is correct

- The security work is a separate delivery slice, so it gets its own folder
- The core user flow is another slice, so it gets its own folder
- Each story has one user-visible outcome
- Each story is split into tasks only where implementation is non-trivial

## Bad breakdown

- One milestone folder with every ticket mixed together
- One giant story that includes approval flow, admin controls, audit logging, and permissions
- One task that mixes frontend, backend, config, and migration
