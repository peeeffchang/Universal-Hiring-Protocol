# tests/engine/test_action_envelope.py

import pytest
from datetime import datetime
from uuid import UUID
from engine.action_envelope import IntentBasedActionEnvelope, Constraint, Signature

def test_constraint_creation():
    constraint = Constraint(type="privacyConsent", value={"consentId": "consent-id-123"})
    assert constraint.type == "privacyConsent"
    assert constraint.value == {"consentId": "consent-id-123"}

def test_signature_creation():
    signature = Signature(algorithm="ES256", key_id="key-id-abc", value="base64encodedSignature")
    assert signature.algorithm == "ES256"
    assert signature.key_id == "key-id-abc"
    assert signature.value == "base64encodedSignature"

def test_intent_based_action_envelope_creation_minimal():
    envelope_id = UUID("a1b2c3d4-e5f6-7890-1234-567890abcdef")
    timestamp = datetime.now()
    payload = {"interviewType": "technical"}

    envelope = IntentBasedActionEnvelope(
        envelope_id=envelope_id,
        intent="uhp:intent:ScheduleInterview",
        originator="urn:uhp:agent:recruiting-ai-v1",
        timestamp=timestamp,
        payload=payload
    )

    assert envelope.envelope_id == envelope_id
    assert envelope.intent == "uhp:intent:ScheduleInterview"
    assert envelope.originator == "urn:uhp:agent:recruiting-ai-v1"
    assert envelope.timestamp == timestamp
    assert envelope.payload == payload
    assert envelope.context == {}
    assert envelope.constraints == []
    assert envelope.signature is None

def test_intent_based_action_envelope_creation_full():
    envelope_id = UUID("a1b2c3d4-e5f6-7890-1234-567890abcdef")
    timestamp = datetime.now()
    payload = {"interviewType": "technical"}
    context = {"jobId": "urn:uhp:job:j123"}
    constraint = Constraint(type="privacyConsent", value={"consentId": "consent-id-123"})
    signature = Signature(algorithm="ES256", key_id="key-id-abc", value="base64encodedSignature")

    envelope = IntentBasedActionEnvelope(
        envelope_id=envelope_id,
        intent="uhp:intent:ScheduleInterview",
        originator="urn:uhp:agent:recruiting-ai-v1",
        timestamp=timestamp,
        payload=payload,
        context=context,
        constraints=[constraint],
        signature=signature
    )

    assert envelope.envelope_id == envelope_id
    assert envelope.intent == "uhp:intent:ScheduleInterview"
    assert envelope.originator == "urn:uhp:agent:recruiting-ai-v1"
    assert envelope.timestamp == timestamp
    assert envelope.payload == payload
    assert envelope.context == context
    assert envelope.constraints == [constraint]
    assert envelope.signature == signature
