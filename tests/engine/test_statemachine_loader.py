# tests/engine/test_statemachine_loader.py

import pytest
import os
import yaml
from engine.statemachine import StateMachine, State, Transition, Action
from engine.statemachine_loader import StateMachineLoader

# Create a temporary YAML file for testing
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
        on_exit:
          - name: update_applicant_status
            params:
              status: processed
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

def test_load_from_yaml_success(sample_yaml_file):
    sm = StateMachineLoader.load_from_yaml(sample_yaml_file)

    assert sm.name == "CandidateApplication"
    assert sm.initial_state == "Applied"
    assert len(sm.states) == 4
    assert "Applied" in sm.states
    assert "Interviewing" in sm.states
    assert "Rejected" in sm.states
    assert "Hired" in sm.states

    applied_state = sm.states["Applied"]
    assert len(applied_state.entry_actions) == 1
    assert applied_state.entry_actions[0].name == "send_confirmation_email"
    assert applied_state.entry_actions[0].params == {"template": "application_received"}

    assert len(sm.transitions) == 3

    # Test a specific transition
    interview_transition = None
    for t in sm.transitions:
        if t.from_state == "Applied" and t.to_state == "Interviewing":
            interview_transition = t
            break
    assert interview_transition is not None
    assert interview_transition.trigger_action.name == "schedule_interview"
    assert len(interview_transition.conditions) == 1
    assert interview_transition.conditions[0]["field"] == "score"

def test_load_from_yaml_missing_initial_state(tmp_path):
    yaml_content = """
    name: InvalidMachine
    states: {}
    transitions: []
    """
    filepath = tmp_path / "invalid_statemachine.yaml"
    filepath.write_text(yaml_content)

    with pytest.raises(ValueError, match="State machine YAML must specify an 'initial_state'"):
        StateMachineLoader.load_from_yaml(filepath)

def test_load_from_yaml_file_not_found(tmp_path):
    with pytest.raises(FileNotFoundError):
        StateMachineLoader.load_from_yaml(tmp_path / "non_existent.yaml")