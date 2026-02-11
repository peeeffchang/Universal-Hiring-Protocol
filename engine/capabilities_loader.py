# engine/capabilities_loader.py

import json
from typing import Dict, List, Any, Optional

class Capability:
    """Represents a single UHP capability."""
    def __init__(self,
                 id: str,
                 name: str,
                 api_endpoint: str,
                 http_method: str,
                 description: Optional[str] = None,
                 request_schema: Optional[str] = None,
                 response_schema: Optional[str] = None):
        self.id = id
        self.name = name
        self.api_endpoint = api_endpoint
        self.http_method = http_method
        self.description = description
        self.request_schema = request_schema
        self.response_schema = response_schema

    def __repr__(self):
        return f"Capability(id='{self.id}', name='{self.name}', http_method='{self.http_method}')"

class CapabilitiesRegistry:
    """Loads and provides query access to UHP capabilities."""

    def __init__(self, service_name: str, version: str, capabilities: List[Capability]):
        self.service_name = service_name
        self.version = version
        self.capabilities = {cap.id: cap for cap in capabilities}
        self.capabilities_by_name = {cap.name: cap for cap in capabilities}

    @staticmethod
    def load_from_json(filepath: str) -> 'CapabilitiesRegistry':
        """
        Loads capabilities from a capabilities.json file.
        """
        with open(filepath, 'r') as file:
            data = json.load(file)

        service_name = data['serviceName']
        version = data['version']
        
        capabilities_list = []
        for cap_data in data['capabilities']:
            capability = Capability(
                id=cap_data['id'],
                name=cap_data['name'],
                api_endpoint=cap_data['apiEndpoint'],
                http_method=cap_data['httpMethod'],
                description=cap_data.get('description'),
                request_schema=cap_data.get('requestSchema'),
                response_schema=cap_data.get('responseSchema')
            )
            capabilities_list.append(capability)
        
        return CapabilitiesRegistry(service_name, version, capabilities_list)

    def get_capability_by_id(self, cap_id: str) -> Optional[Capability]:
        """Returns a capability by its ID."""
        return self.capabilities.get(cap_id)

    def get_capability_by_name(self, cap_name: str) -> Optional[Capability]:
        """Returns a capability by its human-readable name."""
        return self.capabilities_by_name.get(cap_name)