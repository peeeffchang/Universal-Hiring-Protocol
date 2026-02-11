# engine/action_parser.py

import json
from typing import Dict, Any
from uuid import UUID
from datetime import datetime
from engine.action_envelope import IntentBasedActionEnvelope, Constraint, Signature

class ActionParser:
    """Parses raw data into IntentBasedActionEnvelope objects."""

    @staticmethod
    def parse_from_dict(data: Dict[str, Any]) -> IntentBasedActionEnvelope:
        """
        Parses a dictionary into an IntentBasedActionEnvelope object.
        """
        envelope_id = UUID(data['envelopeId'])
        timestamp = datetime.fromisoformat(data['timestamp'].replace('Z', '+00:00')) # Handle 'Z' for UTC

        context = data.get('context', {})
        payload = data['payload']

        constraints_data = data.get('constraints', [])
        constraints = [Constraint(c['type'], c['value']) for c in constraints_data]

        signature_data = data.get('signature')
        signature = None
        if signature_data:
            signature = Signature(signature_data['algorithm'], signature_data['keyId'], signature_data['value'])

        return IntentBasedActionEnvelope(
            envelope_id=envelope_id,
            intent=data['intent'],
            originator=data['originator'],
            timestamp=timestamp,
            payload=payload,
            context=context,
            constraints=constraints,
            signature=signature
        )

    @staticmethod
    def parse_from_json(json_string: str) -> IntentBasedActionEnvelope:
        """
        Parses a JSON string into an IntentBasedActionEnvelope object.
        """
        data = json.loads(json_string)
        return ActionParser.parse_from_dict(data)