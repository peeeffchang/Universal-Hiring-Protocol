# Conceptual Tests for Privacy Settings Schema Extension

## Test Case: Valid Candidate Object with Privacy Settings

**Purpose:** To verify that the `candidate.json` schema, with the new `privacySettings` extension, correctly validates a Candidate object that includes well-formed privacy settings.

**Input (Valid Candidate Object Example):**
```json
{
  "candidateId": "cand-123",
  "profile": {
    "skills": ["JavaScript", "React"],
    "experienceYears": 5
  },
  "visibility": "Anonymized",
  "privacySettings": {
    "personalInformation": {
      "visibility": "EmployersOnly",
      "purposeBindings": ["Recruitment", "Application"]
    },
    "employmentHistory": {
      "visibility": "Private",
      "purposeBindings": ["Application"]
    },
    "education": {
      "visibility": "Public",
      "purposeBindings": ["Recruitment"]
    },
    "skills": {
      "visibility": "Public",
      "purposeBindings": ["Recruitment"]
    },
    "sensitiveInformation": {
      "visibility": "Private",
      "purposeBindings": []
    }
  }
}
```

**Expected Outcome:**
*   Validation of the above JSON object against the extended `candidate.json` schema should **PASS**.

## Test Case: Valid Candidate Object Without Privacy Settings (Backward Compatibility)

**Purpose:** To ensure that existing `candidate.json` objects, created before the `privacySettings` extension, remain valid.

**Input (Valid Candidate Object Example - Old Format):**
```json
{
  "candidateId": "cand-456",
  "profile": {
    "skills": ["Python", "ML"],
    "experienceYears": 8
  },
  "visibility": "Anonymized"
}
```

**Expected Outcome:**
*   Validation of the above JSON object against the extended `candidate.json` schema should **PASS**.

## Test Case: Invalid Privacy Settings - Unknown Visibility Enum

**Purpose:** To verify that the schema correctly rejects a `candidate.json` object if `privacySettings.personalInformation.visibility` contains an invalid enum value.

**Input (Invalid Visibility Enum Example):**
```json
{
  "candidateId": "cand-789",
  "profile": {
    "skills": ["Java"],
    "experienceYears": 10
  },
  "visibility": "Anonymized",
  "privacySettings": {
    "personalInformation": {
      "visibility": "UnknownVisibilityTier", // Invalid value
      "purposeBindings": ["Recruitment"]
    },
    "employmentHistory": {
      "visibility": "Private",
      "purposeBindings": ["Application"]
    },
    "education": {
      "visibility": "Public",
      "purposeBindings": ["Recruitment"]
    },
    "skills": {
      "visibility": "Public",
      "purposeBindings": ["Recruitment"]
    },
    "sensitiveInformation": {
      "visibility": "Private",
      "purposeBindings": []
    }
  }
}
```

**Expected Outcome:**
*   Validation of the above JSON object against the extended `candidate.json` schema should **FAIL**.
*   The validation error message should clearly indicate an invalid enum value for `personalInformation.visibility`.

## Test Case: Invalid Privacy Settings - Unknown Purpose Binding Enum

**Purpose:** To verify that the schema correctly rejects a `candidate.json` object if `privacySettings.personalInformation.purposeBindings` contains an invalid enum value.

**Input (Invalid Purpose Binding Enum Example):**
```json
{
  "candidateId": "cand-101",
  "profile": {
    "skills": ["C++"],
    "experienceYears": 12
  },
  "visibility": "Anonymized",
  "privacySettings": {
    "personalInformation": {
      "visibility": "EmployersOnly",
      "purposeBindings": ["Recruitment", "InvalidPurpose"] // Invalid value
    },
    "employmentHistory": {
      "visibility": "Private",
      "purposeBindings": ["Application"]
    },
    "education": {
      "visibility": "Public",
      "purposeBindings": ["Recruitment"]
    },
    "skills": {
      "visibility": "Public",
      "purposeBindings": ["Recruitment"]
    },
    "sensitiveInformation": {
      "visibility": "Private",
      "purposeBindings": []
    }
  }
}
```

**Expected Outcome:**
*   Validation of the above JSON object against the extended `candidate.json` schema should **FAIL**.
*   The validation error message should clearly indicate an invalid enum value within `personalInformation.purposeBindings`.

## Test Case: Missing Required Visibility Field

**Purpose:** To verify that the schema correctly rejects a `candidate.json` object if a required field like `visibility` is missing from a `privacySettings` category.

**Input (Missing Visibility Example):**
```json
{
  "candidateId": "cand-112",
  "profile": {
    "skills": ["Go"],
    "experienceYears": 7
  },
  "visibility": "Anonymized",
  "privacySettings": {
    "personalInformation": {
      // "visibility": "EmployersOnly", // Missing
      "purposeBindings": ["Recruitment"]
    },
    "employmentHistory": {
      "visibility": "Private",
      "purposeBindings": ["Application"]
    },
    "education": {
      "visibility": "Public",
      "purposeBindings": ["Recruitment"]
    },
    "skills": {
      "visibility": "Public",
      "purposeBindings": ["Recruitment"]
    },
    "sensitiveInformation": {
      "visibility": "Private",
      "purposeBindings": []
    }
  }
}
```

**Expected Outcome:**
*   Validation of the above JSON object against the extended `candidate.json` schema should **FAIL**.
*   The validation error message should clearly indicate that `visibility` is a missing required property within `personalInformation`.

## Test Case: Missing Required Purpose Bindings Field

**Purpose:** To verify that the schema correctly rejects a `candidate.json` object if a required field like `purposeBindings` is missing from a `privacySettings` category.

**Input (Missing Purpose Bindings Example):**
```json
{
  "candidateId": "cand-134",
  "profile": {
    "skills": ["Ruby"],
    "experienceYears": 6
  },
  "visibility": "Anonymized",
  "privacySettings": {
    "personalInformation": {
      "visibility": "EmployersOnly"
      // "purposeBindings": ["Recruitment"] // Missing
    },
    "employmentHistory": {
      "visibility": "Private",
      "purposeBindings": ["Application"]
    },
    "education": {
      "visibility": "Public",
      "purposeBindings": ["Recruitment"]
    },
    "skills": {
      "visibility": "Public",
      "purposeBindings": ["Recruitment"]
    },
    "sensitiveInformation": {
      "visibility": "Private",
      "purposeBindings": []
    }
  }
}
```

**Expected Outcome:**
*   Validation of the above JSON object against the extended `candidate.json` schema should **FAIL**.
*   The validation error message should clearly indicate that `purposeBindings` is a missing required property within `personalInformation`.

## Test Case: Successful Embedding of Privacy Metadata

**Purpose:** To verify that a `candidate.json` instance can successfully include the `privacySettings` metadata as defined in the schema.

**Input:** A `candidate.json` object with valid `privacySettings`. (Refer to "Valid Candidate Object with Privacy Settings" test case for example structure).

**Expected Outcome:**
*   Successful generation/serialization of the JSON payload including `privacySettings` without validation errors against the extended `candidate.json` schema. The structure and values within `privacySettings` should conform to the schema definition.

## Test Case: Accurate Extraction of Privacy Metadata

**Purpose:** To verify that an AI agent or platform can accurately parse and extract the `privacySettings` metadata from a `candidate.json` data payload.

**Input:** A `candidate.json` object with `privacySettings` metadata. (Refer to "Valid Candidate Object with Privacy Settings" test case for example structure).

**Expected Outcome:**
*   When the `candidate.json` payload is parsed, the `privacySettings` object and its sub-properties (e.g., `personalInformation`, `visibility`, `purposeBindings`) are correctly identified and accessible. The extracted values should match those embedded in the input payload.
