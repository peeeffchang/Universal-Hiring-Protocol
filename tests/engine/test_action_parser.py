# tests/engine/test_action_parser.py

import pytest
import json
from datetime import datetime
from uuid import UUID
from engine.action_envelope import IntentBasedActionEnvelope, Constraint, Signature
from engine.action_parser import ActionParser

@pytest.fixture
def sample_action_envelope_dict():
    return {
        "envelopeId": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
        "intent": "uhp:intent:ScheduleInterview",
        "originator": "urn:uhp:agent:recruiting-ai-v1",
        "timestamp": "2026-02-11T14:30:00Z",
        "payload": {"interviewType": "technical"},
        "context": {"jobId": "urn:uhp:job:j123"},
        "constraints": [{"type": "privacyConsent", "value": {"consentId": "consent-id-123"}}],
        "signature": {"algorithm": "ES256", "keyId": "key-id-abc", "value": "base64encodedSignature"}
    }

@pytest.fixture
def sample_action_envelope_json(sample_action_envelope_dict):
    return json.dumps(sample_action_envelope_dict)

def test_parse_from_dict_success(sample_action_envelope_dict):
    envelope = ActionParser.parse_from_dict(sample_action_envelope_dict)

    assert isinstance(envelope, IntentBasedActionEnvelope)
    assert envelope.envelope_id == UUID("a1b2c3d4-e5f6-7890-1234-567890abcdef")
    assert envelope.intent == "uhp:intent:ScheduleInterview"
    assert envelope.originator == "urn:uhp:agent:recruiting-ai-v1"
    assert envelope.timestamp.replace(tzinfo=None) == datetime(2026, 2, 11, 14, 30, 0) # Compare naive datetimes
    assert envelope.payload == {"interviewType": "technical"}
    assert envelope.context == {"jobId": "urn:uhp:job:j123"}
    assert len(envelope.constraints) == 1
    assert envelope.constraints[0].type == "privacyConsent"
    assert envelope.constraints[0].value == {"consentId": "consent-id-123"}
    assert envelope.signature.algorithm == "ES256"

def test_parse_from_json_success(sample_action_envelope_json):
    envelope = ActionParser.parse_from_json(sample_action_envelope_json)

    assert isinstance(envelope, IntentBasedActionEnvelope)
    assert envelope.envelope_id == UUID("a1b2c3d4-e5f6-7890-1234-567890abcdef")
    assert envelope.intent == "uhp:intent:ScheduleInterview"
    assert envelope.originator == "urn:uhp:agent:recruiting-ai-v1"
    assert envelope.payload == {"interviewType": "technical"}

def test_parse_from_dict_missing_required_field():
    minimal_data = {
        "envelopeId": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
        "originator": "urn:uhp:agent:recruiting-ai-v1",
        "timestamp": "2026-02-11T14:30:00Z",
        "payload": {"interviewType": "technical"}
        # 'intent' is missing
    }
    with pytest.raises(KeyError, match="'intent'"):
        ActionParser.parse_from_dict(minimal_data)

def test_parse_from_json_invalid_json():
    invalid_json_string = "clearly not json"
    with pytest.raises(json.JSONDecodeError):
        ActionParser.parse_from_json(invalid_json_string)