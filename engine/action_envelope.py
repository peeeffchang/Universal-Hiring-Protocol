# engine/action_envelope.py

from typing import Dict, List, Any, Optional
from datetime import datetime
from uuid import UUID

class Constraint:
    """Represents a constraint that must be satisfied for the action."""
    def __init__(self, type: str, value: Dict[str, Any]):
        self.type = type
        self.value = value

    def __repr__(self):
        return f"Constraint(type='{self.type}', value={self.value})"

class Signature:
    """Represents the cryptographic signature details for the action envelope."""
    def __init__(self, algorithm: str, key_id: str, value: str):
        self.algorithm = algorithm
        self.key_id = key_id
        self.value = value

    def __repr__(self):
        return (f"Signature(algorithm='{self.algorithm}', key_id='{self.key_id}', "
                f"value='{self.value[:10]}...')") # Truncate value for brevity

class IntentBasedActionEnvelope:
    """Represents an Intent-Based Action Envelope."""
    def __init__(self,
                 envelope_id: UUID,
                 intent: str,
                 originator: str,
                 timestamp: datetime,
                 payload: Dict[str, Any],
                 context: Optional[Dict[str, Any]] = None,
                 constraints: Optional[List[Constraint]] = None,
                 signature: Optional[Signature] = None):
        self.envelope_id = envelope_id
        self.intent = intent
        self.originator = originator
        self.timestamp = timestamp
        self.payload = payload
        self.context = context if context is not None else {}
        self.constraints = constraints if constraints is not None else []
        self.signature = signature

    def __repr__(self):
        return (f"IntentBasedActionEnvelope(envelope_id='{self.envelope_id}', intent='{self.intent}', "
                f"originator='{self.originator}', timestamp='{self.timestamp.isoformat()}', "
                f"payload_keys={list(self.payload.keys())}, context_keys={list(self.context.keys())}, "
                f"constraints_count={len(self.constraints)}, signature={'Present' if self.signature else 'Absent'})")