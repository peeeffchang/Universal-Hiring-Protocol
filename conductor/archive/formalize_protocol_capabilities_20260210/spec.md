# Track Specification: Formalize Protocol Capability Discovery

## Overview

This track aims to formalize the capability discovery mechanism within the Universal Hiring Protocol (UHP). Currently, there is no standardized, machine-readable way for AI agents to programmatically discover the capabilities offered by a UHP-compliant service. This track will address this shortcoming by defining a dedicated `/capabilities` endpoint and its response structure.

## Functional Requirements

1.  **Capability Discovery Endpoint:**
    *   A well-known, dedicated endpoint (e.g., `/capabilities`) MUST be established.
    *   This endpoint MUST return a machine-readable document describing the service's capabilities.
    *   The document format SHOULD be either JSON or YAML.

2.  **Capability Description:**
    *   For each capability, the document MUST include:
        *   The API endpoint(s) associated with the capability.
        *   A clear description of the functionality provided by the endpoint(s).
        *   Data schemas (e.g., JSON Schema references) for both request and response payloads.

## Non-Functional Requirements

*   **Machine Readability:** The `/capabilities` document MUST be easily parsable by AI agents.
*   **Extensibility:** The schema for the capabilities document SHOULD be designed to allow for future expansion (e.g., including authentication requirements, versioning information, human-readable descriptions).

## Acceptance Criteria

1.  A UHP-compliant service can expose a `/capabilities` endpoint.
2.  Accessing the `/capabilities` endpoint returns a valid machine-readable document.
3.  The document accurately lists the service's API endpoints, their functionalities, and references to their request/response schemas.

## Out of Scope

*   Implementation of the actual capabilities themselves (beyond their description).
*   Detailed specification of authentication/authorization mechanisms for capabilities (though hooks for this can be considered in the schema design).
*   Development of a registry or external discovery service for UHP capabilities.