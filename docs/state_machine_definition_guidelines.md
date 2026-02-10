# UHP State Machine Definition Guidelines

This document details the standardized YAML structure and conventions for defining state machines within the Universal Hiring Protocol (UHP). These guidelines ensure consistency, machine readability, and human understanding across all UHP state machine definitions.

## 1. Overall Structure

Each state machine definition is a YAML file with a top-level structure comprising `metadata` and `states`.

```yaml
metadata:
  name: <string>
  description: <string>
  initial_state: <string>
states:
  - name: <string>
    description: <string>
    transitions:
      - event: <string>
        target: <string>
```

## 2. `metadata` Section

The `metadata` section provides high-level information about the state machine.

*   **`name` (required, string):** A unique identifier for the state machine (e.g., `candidate_application_process`).
*   **`description` (required, string):** A brief, human-readable description of the state machine's purpose.
*   **`initial_state` (required, string):** The name of the state where the entity begins its lifecycle. This must correspond to a `name` in the `states` list.

## 3. `states` Section

The `states` section is a list of all possible states an entity can be in. Each item in the list represents a single state.

### State Object Structure

*   **`name` (required, string):** A unique identifier for the state within this state machine (e.g., `applied`, `in_review`).
*   **`description` (required, string):** A clear, human-readable description of what this state represents.
*   **`on_entry` (optional, list of objects):** A list of actions to perform when *entering* this state.
    *   Each action object must have:
        *   **`action_type` (string):** An identifier for the type of action (e.g., `send_notification`, `update_timestamp`).
        *   **`params` (map):** A map of key-value pairs representing parameters for the action.
*   **`on_exit` (optional, list of objects):** A list of actions to perform when *exiting* this state. Structure is identical to `on_entry`.
*   **`transitions` (required, list of objects):** A list of valid transitions that can occur from this state. If a state is a final state with no outbound transitions, this list should be empty (`[]`).

## 4. `transitions` Section

The `transitions` section, nested within each state, defines how an entity moves from one state to another.

### Transition Object Structure

*   **`event` (required, string):** The name of the event that triggers this transition (e.g., `review_application`, `accept_offer`).
*   **`target` (required, string):** The name of the state to which the entity transitions. This must correspond to a `name` in the main `states` list.
*   **`conditions` (optional, list of objects):** A list of conditions (guards) that must be met for the transition to be valid.
    *   Each condition object must have:
        *   **`condition_type` (string):** An identifier for the type of condition (e.g., `has_permission`, `all_fields_completed`).
        *   **`params` (map):** A map of key-value pairs representing parameters for the condition.
*   **`actions` (optional, list of objects):** A list of actions to perform *during* this transition. Structure is identical to `on_entry`.

## 5. Examples

### Example: Simplified Candidate Application State
```yaml
metadata:
  name: candidate_status
  description: Simplified state machine for candidate tracking.
  initial_state: new_application

states:
  - name: new_application
    description: Application received.
    transitions:
      - event: process_application
        target: in_review
  - name: in_review
    description: Application is being evaluated.
    on_entry:
      - action_type: update_timestamp
        params: { field: "review_start_date" }
    transitions:
      - event: approve_for_interview
        target: interview_scheduled
        conditions:
          - condition_type: has_required_skills
            params: { skills: ["Python", "SQL"] }
      - event: reject_application
        target: rejected
  - name: interview_scheduled
    description: Interview scheduled with candidate.
    transitions:
      - event: interview_complete
        target: final_review
  - name: final_review
    description: Final evaluation after interview.
    transitions:
      - event: extend_offer
        target: offer_made
      - event: final_reject
        target: rejected
  - name: offer_made
    description: Job offer extended.
    transitions:
      - event: accept_offer
        target: hired
      - event: decline_offer
        target: rejected # Or 'offer_declined' for more granularity
  - name: hired
    description: Candidate accepted offer.
    transitions: []
  - name: rejected
    description: Candidate was rejected.
    transitions: []
```
