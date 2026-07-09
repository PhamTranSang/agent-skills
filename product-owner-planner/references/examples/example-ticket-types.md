# Example: Ticket Type Split

## User input

> Break this feature into tickets for Jira.

## Expected shape

- User story only when there is user-visible value
- Task for backend, frontend, infra, migration, test, and wiring work
- Bug for observed vs expected behavior
- Spike for unresolved product or technical uncertainty

## Good split

### User Story

As a reviewer, I want to see document status so that I know what I can act on.

### Task

- Implement status badge component
- Wire API response into review page

### Bug

- Document status badge disappears after refresh

### Spike

- How should permission checks behave for cross-team reviewers?
