# Conceptual Failing Test for Job JSON Schema

## Test Case: Invalid Job Object

**Purpose:** To verify that the 'Job' JSON Schema correctly identifies and rejects an invalid Job object.

**Input (Invalid Job Object Example):**
```json
{
  "jobId": "job-123",
  "title": 12345,  // Invalid type: should be string
  "skills": ["Python"],
  "location": "Remote",
  "visibility": "Public",
  "extraField": "should not be here" // Extra field
}
```

**Expected Outcome (Failing Test Criteria):**
*   Validation of the above JSON object against the `job.json` schema should **FAIL**.
*   The validation error message should clearly indicate:
    *   Type mismatch for `title`.
    *   Presence of `extraField` (if additional properties are disallowed).

This test will be considered "failing" until a valid `job.json` schema is defined that correctly rejects this invalid input.
