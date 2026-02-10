# Guidelines for Interpreting Privacy Metadata

This document provides guidelines for AI agents, talent platforms, and other systems interacting with Universal Hiring Protocol (UHP) data, specifically regarding the interpretation and enforcement of `privacySettings` metadata in `candidate.json`. Adherence to these guidelines is crucial for maintaining data privacy, respecting candidate preferences, and ensuring compliance with relevant regulations.

## Respecting Visibility Controls

The `privacySettings` object within `candidate.json` defines category-level `visibility` tiers for different types of candidate data. Systems must strictly adhere to these tiers:

*   **`Public`:** Data is generally accessible and can be shared widely. However, even for public data, purpose bindings should still be respected.
*   **`EmployersOnly`:** Data is visible only to direct employers (or their authorized representatives) for whom the candidate has actively applied or explicitly expressed interest in a specific job opening. This data should not be shared with third-party recruiters or other non-employer entities without additional explicit consent.
*   **`ConsentedParties`:** Data is visible only to parties for whom the candidate has provided explicit, granular consent. This requires a robust consent management system within the platform to track and verify permissions.
*   **`Private`:** Data is not generally visible. Access is highly restricted and typically requires explicit, specific consent for a narrow purpose, or is only accessible by the candidate themselves.

**Enforcement:**
*   Before displaying, transmitting, or otherwise processing any piece of candidate data, systems MUST check the `visibility` setting for the corresponding data category.
*   Data should only be presented or made accessible if the requesting entity's role and relationship to the candidate align with the specified `visibility` tier.
*   If a `visibility` tier implies explicit consent (`ConsentedParties`), the system must verify that such consent is actively in place for the requesting party.

## Enforcing Purpose Bindings

Each data category within `privacySettings` also specifies `purposeBindings`, which are the explicit purposes for which the candidate has authorized the use of their data. Systems MUST only use data for the purposes listed in the `purposeBindings` array for that specific data category.

**Defined Purpose Bindings:**
*   **`Recruitment`:** For general talent sourcing, matching, and initial outreach.
*   **`Application`:** For processing job applications, including candidate screening and administrative tasks related to the application process.
*   **`Interview`:** For coordinating and conducting interviews.
*   **`BackgroundCheck`:** For conducting background checks, identity verification, and other pre-employment screening activities.
*   **`LegalCompliance`:** For fulfilling legal and regulatory obligations.

**Enforcement:**
*   Before performing any operation that uses candidate data, systems MUST determine the purpose of that operation.
*   This purpose MUST be validated against the `purposeBindings` associated with the relevant data category.
*   If the intended purpose is not listed in the `purposeBindings` for a given data category, the data MUST NOT be used for that purpose.
*   Platforms should offer clear mechanisms for candidates to review and modify their purpose bindings.

## Best Practices for Handling Sensitive Data

The `sensitiveInformation` category within `privacySettings` is specifically designed for highly sensitive data. Systems should exercise extreme caution and implement enhanced security measures when handling data within this category.

*   **Minimize Collection:** Only collect sensitive information when absolutely necessary and with explicit, informed consent.
*   **Data Minimization:** Store only the minimum amount of sensitive data required for a specific, consented purpose.
*   **Enhanced Security:** Implement strong encryption, access controls, and audit trails for `sensitiveInformation`.
*   **Limited Access:** Restrict access to `sensitiveInformation` to only those personnel or systems that absolutely require it for a legitimate, consented purpose.
*   **Transparency:** Be fully transparent with candidates about what sensitive information is collected, why it's collected, and how it's protected and used.

## General Principles

*   **Transparency:** Inform candidates clearly and concisely about their `privacySettings` options and the implications of each choice.
*   **Granularity:** Provide candidates with granular control over their data as enabled by the category-level `privacySettings`.
*   **Auditability:** Maintain clear audit trails of data access, usage, and consent decisions.
*   **Data Minimization:** Collect and retain only the data necessary for stated and consented purposes.
*   **User Control:** Empower candidates to easily review, modify, and revoke their privacy preferences and consent at any time.
