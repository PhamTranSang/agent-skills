# Example: Ticket Sizing and Split

## User input

> Break the document approval feature into tickets.

## Expected shape

- Each ticket should cover one concern
- Each ticket should be small enough to pick up in a sprint
- Split hidden dependencies into separate tasks when they can block delivery
- Avoid combining UI, API, auth, and migration work into one ticket

## Good split

### Story 1: Review pending documents

As an approver, I want to view pending documents so that I can decide what to do next.

### Task 1: Add approval status query support

- Implement API filtering for pending documents
- Add test coverage for query behavior

### Task 2: Wire review page status badge

- Render status badge on the review page
- Handle loading and empty states

### Spike 1: Clarify cross-team permission rules

- Determine how reviewer permissions should behave for shared documents

## Bad split

- One ticket for UI, API, auth, audit log, and migration together
- One story that covers multiple user roles and multiple outcomes
- One task that mixes unrelated technical changes
