# tests/engine/test_validator.py

import pytest
from datetime import datetime
from uuid import UUID
from engine.statemachine import Action, State, Transition, StateMachine
from engine.statemachine_loader import StateMachineLoader
from engine.action_envelope import IntentBasedActionEnvelope
from engine.validator import ProtocolValidator
from engine.capabilities_loader import CapabilitiesRegistry, Capability # Import new classes

# Fixture from test_statemachine_loader.py for sample YAML
@pytest.fixture
def sample_yaml_file(tmp_path):
    yaml_content = """
    name: CandidateApplication
    initial_state: Applied
    states:
      Applied:
        on_entry:
          - name: send_confirmation_email
            params:
              template: application_received
      Interviewing:
        on_entry: []
      Rejected: {}
      Hired: {}
    transitions:
      - from: Applied
        to: Interviewing
        trigger:
          name: schedule_interview
        conditions:
          - field: score
            operator: greater_than
            value: 70
      - from: Interviewing
        to: Rejected
        trigger:
          name: reject_candidate
      - from: Interviewing
        to: Hired
        trigger:
          name: offer_accepted
    """
    filepath = tmp_path / "sample_statemachine.yaml"
    filepath.write_text(yaml_content)
    return filepath

@pytest.fixture
def sample_capabilities_file(tmp_path):
    json_content = """
    {
      "serviceName": "UHP Test Service",
      "version": "1.0.0",
      "capabilities": [
        {
          "id": "cap-schedule-interview",
          "name": "schedule_interview",
          "description": "Schedule an interview.",
          "apiEndpoint": "/interviews",
          "httpMethod": "POST"
        },
        {
          "id": "cap-reject-candidate",
          "name": "reject_candidate",
          "description": "Reject a candidate.",
          "apiEndpoint": "/candidates/{id}/reject",
          "httpMethod": "POST"
        },
        {
          "id": "cap-offer-accepted",
          "name": "offer_accepted",
          "description": "Mark offer as accepted.",
          "apiEndpoint": "/candidates/{id}/hire",
          "httpMethod": "POST"
        }
      ]
    }
    """
    filepath = tmp_path / "sample_capabilities.json"
    filepath.write_text(json_content)
    return filepath

@pytest.fixture
def sample_capabilities_registry(sample_capabilities_file):
    return CapabilitiesRegistry.load_from_json(sample_capabilities_file)

@pytest.fixture
def sample_state_machine(sample_yaml_file):
    return StateMachineLoader.load_from_yaml(sample_yaml_file)

def test_validate_action_valid_transition(sample_state_machine, sample_capabilities_registry):
    # Action envelope for scheduling an interview from 'Applied' state
    action_envelope = IntentBasedActionEnvelope(
        envelope_id=UUID("a1b2c3d4-e5f6-7890-1234-567890abcdef"),
        intent="uhp:intent:schedule_interview",
        originator="test_agent",
        timestamp=datetime.now(),
        payload={}
    )
    validator = ProtocolValidator(sample_state_machine, sample_capabilities_registry)
    error_message = validator.validate_action("Applied", action_envelope)
    assert error_message is None

def test_validate_action_invalid_transition(sample_state_machine, sample_capabilities_registry):
    # Action envelope for rejecting candidate from 'Applied' state (invalid transition)
    action_envelope = IntentBasedActionEnvelope(
        envelope_id=UUID("b2c3d4e5-f6a7-8901-2345-67890abcdef0"),
        intent="uhp:intent:reject_candidate",
        originator="test_agent",
        timestamp=datetime.now(),
        payload={}
    )
    validator = ProtocolValidator(sample_state_machine, sample_capabilities_registry)
    error_message = validator.validate_action("Applied", action_envelope)
    assert error_message is not None
    assert "No valid transition found from state 'Applied'" in error_message

def test_validate_action_unknown_current_state(sample_state_machine, sample_capabilities_registry):
    # Action from an unknown state
    action_envelope = IntentBasedActionEnvelope(
        envelope_id=UUID("c3d4e5f6-a7b8-9012-3456-7890abcdef01"),
        intent="uhp:intent:some_action", # This intent is also not in capabilities
        originator="test_agent",
        timestamp=datetime.now(),
        payload={}
    )
    validator = ProtocolValidator(sample_state_machine, sample_capabilities_registry)
    error_message = validator.validate_action("UnknownState", action_envelope)
    assert error_message is not None
    assert "Invalid current state: 'UnknownState' not found in state machine." in error_message

def test_validate_action_no_matching_intent(sample_state_machine, sample_capabilities_registry):
    # Action with no matching intent from 'Applied' state
    action_envelope = IntentBasedActionEnvelope(
        envelope_id=UUID("d4e5f6a7-b8c9-0123-4567-890abcdef012"),
        intent="uhp:intent:unknown_intent",
        originator="test_agent",
        timestamp=datetime.now(),
        payload={}
    )
    validator = ProtocolValidator(sample_state_machine, sample_capabilities_registry)
    error_message = validator.validate_action("Applied", action_envelope)
    assert error_message is not None
    assert "No valid transition found from state 'Applied' for intent 'uhp:intent:unknown_intent'." in error_message

def test_validate_action_valid_transition_with_different_state(sample_state_machine, sample_capabilities_registry):
    # Valid transition from Interviewing to Hired
    action_envelope = IntentBasedActionEnvelope(
        envelope_id=UUID("e5f6a7b8-c9d0-1234-5678-90abcdef0123"),
        intent="uhp:intent:offer_accepted",
        originator="test_agent",
        timestamp=datetime.now(),
        payload={}
    )
    validator = ProtocolValidator(sample_state_machine, sample_capabilities_registry)
    error_message = validator.validate_action("Interviewing", action_envelope)
    assert error_message is None

def test_validate_action_intent_not_in_capabilities(sample_state_machine, sample_capabilities_registry):
    # Action envelope with an intent not registered in capabilities
    action_envelope = IntentBasedActionEnvelope(
        envelope_id=UUID("f1g2h3i4-j5k6-7890-1234-567890abcde0"),
        intent="uhp:intent:new_unregistered_action",
        originator="test_agent",
        timestamp=datetime.now(),
        payload={}
    )
    validator = ProtocolValidator(sample_state_machine, sample_capabilities_registry)
    error_message = validator.validate_action("Applied", action_envelope)
    assert error_message is not None
    assert "Intent 'uhp:intent:new_unregistered_action' is not a registered capability." in error_message

def test_validate_action_no_capabilities_registry(sample_state_machine):
    # Test without capabilities registry (should behave as before)
    action_envelope = IntentBasedActionEnvelope(
        envelope_id=UUID("a1b2c3d4-e5f6-7890-1234-567890abcdef"),
        intent="uhp:intent:schedule_interview",
        originator="test_agent",
        timestamp=datetime.now(),
        payload={}
    )
    validator = ProtocolValidator(sample_state_machine) # No capabilities_registry passed
    error_message = validator.validate_action("Applied", action_envelope)
    assert error_message is None
