# Conceptual Failing Test for Capabilities JSON Schema

## Test Case: Invalid Capabilities Object

**Purpose:** To verify that the 'Capabilities' JSON Schema correctly identifies and rejects an invalid Capabilities object.

**Input (Invalid Capabilities Object Example):**
```json
{
  "serviceName": "UHP Mock Service",
  "version": "1.0.0",
  "capabilities": [
    {
      "id": "get-jobs",
      "name": "Retrieve Job Listings",
      "description": "Allows AI agents to retrieve a list of available job postings.",
      "apiEndpoint": "/jobs",
      "httpMethod": "INVALID_METHOD", // Invalid enum value
      "extraField": "should not be here" // if additional properties are disallowed
    },
    {
      "id": "post-candidate",
      "name": "Submit Candidate Information",
      "description": "Enables AI agents to submit new candidate profiles.",
      "apiEndpoint": "/candidates"
      // Missing httpMethod, which is required
    }
  ]
}
```

**Expected Outcome (Failing Test Criteria):**
*   Validation of the above JSON object against the `capabilities.json` schema should **FAIL**.
*   The validation error message should clearly indicate:
    *   Invalid enum value for `httpMethod` in the first capability.
    *   Missing `httpMethod` in the second capability.
    *   Presence of `extraField` (if additional properties are disallowed).

This test will be considered "failing" until a valid `capabilities.json` schema is defined that correctly rejects this invalid input.
