# Example: Feature Breakdown

## User input

> Draft phase 2 for a document approval feature.

## Expected shape

- Problem summary
- Goals
- Milestones / Epics
- User Stories under each milestone
- Implementation Tasks under each user story
- Scenarios
- Acceptance criteria
- Open questions
- Handoff notes for `engineering-mentor`

## Good example

### Milestone 1: Approval workflow foundation

#### Story 1

As an approver, I want to review a submitted document so that I can accept or reject it.

#### Scenario

- Happy path: approver opens a pending document and sees approve/reject actions
- Failure path: document no longer exists or is no longer pending

#### Acceptance criteria

- Approver can view only pending documents
- Approve and reject actions are available only when status is pending

#### Tasks

- Implement status gating
- Add audit event logging
- Add tests for pending and non-pending states
