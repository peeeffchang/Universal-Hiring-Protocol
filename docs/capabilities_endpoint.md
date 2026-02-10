# Capability Discovery Endpoint

This document specifies the guidelines for exposing the Universal Hiring Protocol (UHP) Capability Discovery Endpoint. This endpoint allows AI agents and other clients to programmatically discover the functionalities and data structures supported by a UHP-compliant service.

## Endpoint Details

*   **URI Path:** `/capabilities`
*   **HTTP Method:** `GET`
*   **Response Content-Type:** `application/json` (or `application/x-yaml` if YAML is supported)
*   **Success Response:** `200 OK`
*   **Error Responses:**
    *   `404 Not Found`: If the `/capabilities` endpoint is not implemented.
    *   `500 Internal Server Error`: For unexpected server-side issues.

## Response Structure

The response from the `/capabilities` endpoint MUST be a machine-readable document conforming to the `capabilities.json` JSON Schema. This schema defines how a service's name, version, and a list of its available capabilities are described.

**Schema Reference:**
*   [./schemas/capabilities.json](../schemas/capabilities.json)

## Example

### JSON Example

```json
{
  "serviceName": "UHP Example Service",
  "version": "1.0.0",
  "capabilities": [
    {
      "id": "get-job-listings",
      "name": "Retrieve Job Listings",
      "description": "Allows retrieval of active job postings based on various filters.",
      "apiEndpoint": "/jobs",
      "httpMethod": "GET",
      "responseSchema": "https://your-service.com/schemas/job.json"
    },
    {
      "id": "submit-application",
      "name": "Submit Job Application",
      "description": "Enables submission of a job application for a specific job.",
      "apiEndpoint": "/applications",
      "httpMethod": "POST",
      "requestSchema": "https://your-service.com/schemas/application.json",
      "responseSchema": "https://your-service.com/schemas/application_response.json"
    }
  ]
}
```

### YAML Example

```yaml
serviceName: UHP Example Service
version: 1.0.0
capabilities:
  - id: get-job-listings
    name: Retrieve Job Listings
    description: Allows retrieval of active job postings based on various filters.
    apiEndpoint: /jobs
    httpMethod: GET
    responseSchema: https://your-service.com/schemas/job.json
  - id: submit-application
    name: Submit Job Application
    description: Enables submission of a job application for a specific job.
    apiEndpoint: /applications
    httpMethod: POST
    requestSchema: https://your-service.com/schemas/application.json
    responseSchema: https://your-service.com/schemas/application_response.json
```
