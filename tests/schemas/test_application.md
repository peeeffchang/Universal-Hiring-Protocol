# Conceptual Failing Test for Application JSON Schema

## Test Case: Invalid Application Object

**Purpose:** To verify that the 'Application' JSON Schema correctly identifies and rejects an invalid Application object.

**Input (Invalid Application Object Example):**
```json
{
  "applicationId": "app-789",
  "jobId": 123, // Invalid type: should be string
  "candidateId": "cand-456",
  "state": "UnknownState", // Invalid enum value
  "extraField": "should not be here"
}
```

**Expected Outcome (Failing Test Criteria):**
*   Validation of the above JSON object against the `application.json` schema should **FAIL**.
*   The validation error message should clearly indicate:
    *   Type mismatch for `jobId`.
    *   Invalid enum value for `state`.
    *   Presence of `extraField` (if additional properties are disallowed).

This test will be considered "failing" until a valid `application.json` schema is defined that correctly rejects this invalid input.
