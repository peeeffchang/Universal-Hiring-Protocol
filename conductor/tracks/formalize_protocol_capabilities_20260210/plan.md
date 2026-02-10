# Implementation Plan: Formalize Protocol Capability Discovery

## Phase 1: Define Capability Discovery Schema [checkpoint: 28efb53]

- [x] Task: Research existing capability discovery patterns and standards
    - [ ] Explore OpenAPI/Swagger specifications for capability definition.
    - [ ] Investigate GraphQL introspection for dynamic schema discovery.
    - [ ] Analyze other relevant industry standards for inspiration.
- [x] Task: Draft JSON Schema for the `/capabilities` endpoint response
    - [x] Define the top-level structure of the capabilities document.
    - [x] Specify how individual API endpoints and their functionalities are represented.
    - [x] Integrate mechanisms for referencing request and response JSON Schemas.
- [x] Task: Validate drafted schema with example capabilities
    - [x] Create mock capability definitions for existing UHP schemas (e.g., `job.json`, `candidate.json`).
    - [x] Verify that the drafted `/capabilities` schema can accurately represent these mock capabilities.
- [ ] Task: Conductor - User Manual Verification 'Phase 1: Define Capability Discovery Schema' (Protocol in workflow.md)

## Phase 2: Document Endpoint Exposure and Usage [checkpoint: e351b59]

- [x] Task: Create documentation for exposing the `/capabilities` endpoint
    - [x] Detail the expected URI path for the `/capabilities` endpoint.
    - [x] Provide clear guidelines on the HTTP method (e.g., GET) and expected response status codes.
    - [x] Include examples of the `/capabilities` document in both JSON and YAML formats.
- [x] Task: Update relevant UHP documentation
    - [x] Review `README.md` and `product.md` for sections that should reference the new capability discovery mechanism.
    - [x] Add a dedicated section or update existing ones to explain how UHP-compliant services expose their capabilities.
- [ ] Task: Conductor - User Manual Verification 'Phase 2: Document Endpoint Exposure and Usage' (Protocol in workflow.md)
