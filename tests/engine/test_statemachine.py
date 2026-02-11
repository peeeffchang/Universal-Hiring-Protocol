# tests/engine/test_statemachine.py

import pytest
from engine.statemachine import Action, Transition, State, StateMachine

def test_action_creation():
    action = Action("start_process", {"param1": "value1"})
    assert action.name == "start_process"
    assert action.params == {"param1": "value1"}

    action_no_params = Action("end_process")
    assert action_no_params.name == "end_process"
    assert action_no_params.params == {}

def test_state_creation():
    entry_action = Action("log_entry")
    exit_action = Action("log_exit")
    state = State("initial", entry_actions=[entry_action], exit_actions=[exit_action])
    assert state.name == "initial"
    assert state.entry_actions == [entry_action]
    assert state.exit_actions == [exit_action]

    state_no_actions = State("final")
    assert state_no_actions.name == "final"
    assert state_no_actions.entry_actions == []
    assert state_no_actions.exit_actions == []

def test_transition_creation():
    trigger = Action("event_triggered")
    transition = Transition("state_a", "state_b", trigger, [{"condition_type": "equals", "key": "data", "value": "xyz"}])
    assert transition.from_state == "state_a"
    assert transition.to_state == "state_b"
    assert transition.trigger_action == trigger
    assert transition.conditions == [{"condition_type": "equals", "key": "data", "value": "xyz"}]

    transition_no_conditions = Transition("state_b", "state_c", trigger)
    assert transition_no_conditions.conditions == []

def test_statemachine_creation():
    action1 = Action("start")
    action2 = Action("finish")

    state1 = State("start_state", entry_actions=[action1])
    state2 = State("end_state", exit_actions=[action2])

    trigger_action = Action("proceed")
    transition = Transition("start_state", "end_state", trigger_action)

    states = {"start_state": state1, "end_state": state2}
    transitions = [transition]

    sm = StateMachine("my_process", "start_state", states, transitions)
    assert sm.name == "my_process"
    assert sm.initial_state == "start_state"
    assert sm.states == states
    assert sm.transitions == transitions
    assert len(sm.transitions) == 1
