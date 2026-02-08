# Conceptual Failing Test for Consent JSON Schema

## Test Case: Invalid Consent Object

**Purpose:** To verify that the 'Consent' JSON Schema correctly identifies and rejects an invalid Consent object.

**Input (Invalid Consent Object Example):**
```json
{
  "consentId": "cons-001",
  "subject": 123, // Invalid type: should be string
  "grantedTo": "EmployerAgent-1",
  "scope": ["identity"],
  "purpose": "InvalidPurpose", // Not in allowed enum
  "state": "InvalidState" // Not in allowed enum
}
```

**Expected Outcome (Failing Test Criteria):**
*   Validation of the above JSON object against the `consent.json` schema should **FAIL**.
*   The validation error message should clearly indicate:
    *   Type mismatch for `subject`.
    *   Invalid enum value for `purpose`.
    *   Invalid enum value for `state`.

This test will be considered "failing" until a valid `consent.json` schema is defined that correctly rejects this invalid input.
