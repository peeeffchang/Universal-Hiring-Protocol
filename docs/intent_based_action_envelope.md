# Intent-Based Action Envelope

## Introduction

The Universal Hiring Protocol (UHP) is designed to facilitate seamless and intelligent interactions between various AI agents, talent platforms, and hiring systems. A cornerstone of this vision is the "Intent-Based Action Envelope," a standardized mechanism that moves beyond simple API calls to enable explicit, semantically rich communication of desired outcomes.

## Definition

An **Intent-Based Action Envelope** is a standardized, machine-readable container that encapsulates a specific, intended action within the UHP ecosystem. It explicitly defines *what* an AI agent or system wishes to achieve, *why* it's taking that action, and *what data* is required to fulfill the intent, along with any relevant context or constraints.

Unlike traditional command-and-control interfaces, the action envelope focuses on the *intention* behind an operation, providing a higher level of abstraction that AI agents can reason about and that systems can validate against predefined rules and state models.

## Purpose

The primary purposes of the Intent-Based Action Envelope are to:

1.  **Enhance AI Agent Reasoning:** Provide AI agents with a clear, structured representation of intentions, allowing them to better understand, formulate, and execute complex hiring workflows autonomously.
2.  **Improve Interoperability:** Standardize the communication of actions across diverse UHP-compliant systems, ensuring that intentions are understood and processed consistently, regardless of the underlying implementation.
3.  **Ensure Security and Auditability:** By explicitly detailing the intent, originator, and context of an action, the envelope facilitates robust authorization, validation, and logging, thereby increasing transparency and accountability in AI-driven processes.
4.  **Enable Context-Aware Processing:** Embed crucial contextual information (e.g., job ID, candidate ID, process state) directly within the envelope, allowing receiving systems to process actions with full awareness of their operational environment.
5.  **Support Privacy-Preserving Workflows:** Incorporate privacy constraints and consent references directly into the action, reinforcing UHP's privacy-native design by ensuring actions respect user preferences and regulatory requirements.
6.  **Drive State Transitions:** Serve as the primary input for UHP state machines, translating an agent's intent into observable events that drive the progression of hiring processes.

By adopting the Intent-Based Action Envelope, UHP aims to create a more robust, intelligent, and trustworthy framework for the future of AI-driven hiring.

## Structure and Schema

The Intent-Based Action Envelope is a structured JSON object designed for clarity, machine-readability, and extensibility. It comprises several key fields:

### Fields

*   **`envelopeId`** (`string`, required):
    *   A universally unique identifier (UUID) for this specific action envelope instance. Ensures idempotency and traceability.
    *   *Example:* `"envelopeId": "a1b2c3d4-e5f6-7890-1234-567890abcdef"`

*   **`intent`** (`string`, required, `format: uri`):
    *   A URI that explicitly declares the intended action or outcome. This URI should be standardized within the UHP (e.g., following a URN or URL pattern). It acts as the core verb of the action.
    *   *Example:* `"intent": "uhp:intent:ScheduleInterview"`

*   **`originator`** (`string`, required):
    *   Identifies the entity (e.g., AI agent, platform, user ID) that initiated the intent. Essential for authentication, authorization, and auditing.
    *   *Example:* `"originator": "urn:uhp:agent:recruiting-ai-v1"`

*   **`timestamp`** (`string`, required, `format: date-time`):
    *   The ISO 8601 formatted timestamp indicating when the action envelope was created. Provides chronological context.
    *   *Example:* `"timestamp": "2026-02-11T14:30:00Z"`

*   **`context`** (`object`, optional):
    *   An object containing relevant contextual information that helps the receiving system understand the broader situation or process to which the intent applies. This can include identifiers for related UHP entities.
    *   *Example:*
        ```json
        "context": {
          "jobId": "urn:uhp:job:j123",
          "candidateId": "urn:uhp:candidate:c456",
          "processId": "a7b8c9d0-e1f2-3456-7890-1234567890ab"
        }
        ```

*   **`payload`** (`object`, required):
    *   The actual data necessary to execute the `intent`. This field is highly dynamic and typically embeds or references existing UHP data schemas (e.g., `application.json`, `consent.json`). The structure of the `payload` is determined by the `intent`.
    *   *Example (for intent `uhp:intent:ScheduleInterview`):*
        ```json
        "payload": {
          "interviewType": "technical",
          "interviewers": ["interviewer-id-1", "interviewer-id-2"],
          "proposedSlots": [
            {
              "startTime": "2026-03-01T10:00:00Z",
              "endTime": "2026-03-01T11:00:00Z",
              "timezone": "America/New_York"
            },
            {
              "startTime": "2026-03-02T14:00:00Z",
              "endTime": "2026-03-02T15:00:00Z",
              "timezone": "Europe/London"
            }
          ]
        }
        ```
    *   *Example (for intent `uhp:intent:SubmitApplication`, embedding `application.json` content):*
        ```json
        "payload": {
          "applicationId": "app-789",
          "jobId": "urn:uhp:job:j123",
          "candidateId": "urn:uhp:candidate:c456",
          "submissionDate": "2026-02-11T14:30:00Z",
          "status": "submitted",
          "documents": [
            {
              "type": "resume",
              "url": "https://example.com/resume-c456.pdf"
            }
          ]
        }
        ```

*   **`constraints`** (`array`, optional):
    *   An array of objects specifying conditions or rules that must be satisfied for the action to be considered valid and executable. This can include privacy consents, deadlines, or other policy requirements.
    *   *Example (requiring explicit consent for sensitive data processing):*
        ```json
        "constraints": [
          {
            "type": "privacyConsent",
            "value": {
              "consentId": "consent-id-123",
              "requiredScopes": ["profile:read", "contact:write"]
            }
          },
          {
            "type": "deadline",
            "value": "2026-02-15T23:59:59Z"
          }
        ]
        ```

*   **`signature`** (`object`, optional):
    *   Cryptographic signature details to verify the authenticity and integrity of the action envelope. This typically includes fields for the signing algorithm, key ID, and the signature value itself.
    *   *Example (simplified):*
        ```json
        "signature": {
          "algorithm": "ES256",
          "keyId": "key-id-abc",
          "value": "base64encodedSignature"
        }
        ```

## Integration with UHP Components

The Intent-Based Action Envelope is designed to seamlessly integrate with and orchestrate interactions across various core Universal Hiring Protocol (UHP) components. It acts as a primary communication mechanism for AI agents and systems, translating high-level intents into concrete, auditable actions that impact the state of UHP entities.

### Key Integration Points

1.  **Candidate (`candidate.json`) and Job (`job.json`) Entities:**
    *   **Description:** Action envelopes can be used to manage the lifecycle of candidate profiles and job postings. Intents such as `uhp:intent:UpdateCandidateProfile` or `uhp:intent:PublishJob` would encapsulate the relevant `candidate.json` or `job.json` data within their `payload`.
    *   **Example Scenario:** An AI career assistant, upon a candidate's approval, sends an action envelope with `uhp:intent:UpdateCandidateProfile` and an updated `candidate.json` in the `payload` to a talent platform.

2.  **Application (`application.json`) Entity:**
    *   **Description:** The process of applying for a job is a prime use case for action envelopes. An `uhp:intent:SubmitApplication` would typically include a complete `application.json` structure within its `payload`, along with `jobId` and `candidateId` in its `context`. Subsequent intents, like `uhp:intent:WithdrawApplication` or `uhp:intent:AcceptOffer`, would reference the `applicationId`.
    *   **Example Scenario:** A UHP-compliant talent platform receives an `uhp:intent:SubmitApplication` from an AI agent, validates the `payload` against `application.json` schema, and processes the job application.

3.  **Consent (`consent.json`) Entity:**
    *   **Description:** Privacy and explicit consent are central to UHP. Action envelopes can be used to request, grant, or revoke consents. An `uhp:intent:RequestConsent` might have a `payload` defining the consent terms (`consent.json`), and the `constraints` field of any action could require a specific `consentId` to be present and active before execution.
    *   **Example Scenario:** A recruiting AI needs to process sensitive candidate data. It first sends an `uhp:intent:RequestConsent` action envelope. Upon receiving an `uhp:intent:GrantConsent` from the candidate's personal data agent, it then proceeds with the data processing intent.

4.  **Capabilities (`capabilities.json`):**
    *   **Description:** Capabilities define the services a UHP participant offers (e.g., ability to schedule interviews, perform skill assessments). The `intent` field of an action envelope directly maps to a discovered capability. An AI agent discovers a `uhp:capability:ScheduleInterview` and then constructs an `uhp:intent:ScheduleInterview` action envelope to invoke that capability.
    *   **Example Scenario:** An AI orchestrator queries a UHP platform for its capabilities. Discovering a `uhp:capability:ScheduleInterview`, it then sends an action envelope with `uhp:intent:ScheduleInterview` in the `intent` field and relevant details in the `payload` to initiate the interview scheduling process.

5.  **State Machines (YAML Definitions):**
    *   **Description:** UHP state machines (e.g., for candidate application, job posting lifecycle) define the permissible states and transitions of a process. Action envelopes are the event triggers for these state transitions. The `intent` acts as the event, and the `context` often contains the `processId` of the state machine instance being affected.
    *   **Example Scenario:** Within a `candidate_application_process` state machine, an `uhp:intent:AdvanceApplication` with a `payload` indicating "stage: interview" could trigger a transition from `ApplicationReviewed` to `InterviewScheduled` state. The state machine would validate if this transition is allowed based on its current state and rules.

By standardizing the communication of intents, the Action Envelope empowers UHP participants to interact more intelligently, securely, and in alignment with defined processes and policies.
