# Candidate Schema Privacy Extension

This document details the privacy-related extensions made to the `candidate.json` schema within the Universal Hiring Protocol (UHP). These extensions introduce category-level privacy controls and purpose bindings for candidate data, allowing for granular management of data visibility and usage.

## New Property: `privacySettings`

A new top-level property, `privacySettings`, has been added to the `candidate.json` schema. This object encapsulates all privacy-related configurations for a candidate's profile.

### Structure of `privacySettings`

The `privacySettings` object contains several sub-objects, each corresponding to a specific category of candidate information. Each category object defines a `visibility` tier and `purposeBindings`.

```json
"privacySettings": {
  "type": "object",
  "description": "Privacy settings for different categories of candidate data.",
  "properties": {
    "personalInformation": { /* ... details ... */ },
    "employmentHistory": { /* ... details ... */ },
    "education": { /* ... details ... */ },
    "skills": { /* ... details ... */ },
    "sensitiveInformation": { /* ... details ... */ }
  },
  "additionalProperties": false,
  "default": { /* ... default values ... */ }
}
```

### Privacy Categories and Their Details

The following privacy categories are defined within `privacySettings`:

#### `personalInformation`
*   **Description:** Privacy settings for personal identifying information (e.g., name, contact details, address).
*   **`visibility` (Enum):**
    *   `Public`: Visible to all parties.
    *   `EmployersOnly`: Visible only to employers for whom the candidate has applied or expressed interest.
    *   `ConsentedParties`: Visible only to parties for whom explicit consent has been given.
    *   `Private`: Not visible unless explicitly granted for a specific purpose.
*   **`purposeBindings` (Array of Enum):**
    *   `Recruitment`: Data can be used for general recruitment activities.
    *   `Application`: Data can be used for processing job applications.
    *   `Interview`: Data can be used for scheduling and conducting interviews.
    *   `BackgroundCheck`: Data can be used for background verification.

#### `employmentHistory`
*   **Description:** Privacy settings for employment history (e.g., past jobs, roles, dates).
*   **`visibility` (Enum):** Same as `personalInformation` visibility options.
*   **`purposeBindings` (Array of Enum):**
    *   `Recruitment`
    *   `Application`
    *   `Interview`

#### `education`
*   **Description:** Privacy settings for educational background (e.g., degrees, institutions, dates).
*   **`visibility` (Enum):** Same as `personalInformation` visibility options.
*   **`purposeBindings` (Array of Enum):**
    *   `Recruitment`
    *   `Application`

#### `skills`
*   **Description:** Privacy settings for skills (e.g., technical skills, soft skills).
*   **`visibility` (Enum):** Same as `personalInformation` visibility options.
*   **`purposeBindings` (Array of Enum):**
    *   `Recruitment`
    *   `Application`

#### `sensitiveInformation`
*   **Description:** Privacy settings for sensitive personal information (e.g., protected characteristics, background check results).
*   **`visibility` (Enum):**
    *   `Private`
    *   `ConsentedParties`
*   **`purposeBindings` (Array of Enum):**
    *   `BackgroundCheck`
    *   `LegalCompliance`

## Default Values

The `privacySettings` object and its sub-properties have default values to ensure a baseline level of privacy and backward compatibility for existing `candidate.json` instances that do not specify these settings.

## Usage Considerations for AI Agents and Platforms

AI agents and platforms processing `candidate.json` payloads must:
*   Respect the `visibility` settings for each category when displaying or sharing candidate information.
*   Adhere to the `purposeBindings` for each category, ensuring data is only used for explicitly permitted purposes.
*   Implement mechanisms to obtain explicit consent from candidates for data usage beyond the default or publicly available settings.
