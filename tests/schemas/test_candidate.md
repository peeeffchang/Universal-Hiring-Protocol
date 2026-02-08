# Conceptual Failing Test for Candidate JSON Schema

## Test Case: Invalid Candidate Object

**Purpose:** To verify that the 'Candidate' JSON Schema correctly identifies and rejects an invalid Candidate object.

**Input (Invalid Candidate Object Example):**
```json
{
  "candidateId": "cand-456",
  "profile": {
    "skills": ["Python", "ML"],
    "experienceYears": "eight" // Invalid type: should be integer
  },
  "visibility": "Public", // Invalid enum value: should be Anonymized
  "name": "John Doe" // Should not exist at v0.1
}
```

**Expected Outcome (Failing Test Criteria):**
*   Validation of the above JSON object against the `candidate.json` schema should **FAIL**.
*   The validation error message should clearly indicate:
    *   Type mismatch for `profile.experienceYears`.
    *   Invalid enum value for `visibility`.
    *   Presence of `name` (if additional properties are disallowed or name is explicitly excluded).

This test will be considered "failing" until a valid `candidate.json` schema is defined that correctly rejects this invalid input and enforces the "Anonymized Only" rule for candidates at v0.1.
