
# engine/statemachine.py

from typing import Dict, List, Any, Optional

class Action:
    """Represents an action associated with a state or transition."""
    def __init__(self, name: str, params: Optional[Dict[str, Any]] = None):
        self.name = name
        self.params = params if params is not None else {}

    def __repr__(self):
        return f"Action(name='{self.name}', params={self.params})"

class Transition:
    """Represents a transition between two states."""
    def __init__(self,
                 from_state: str,
                 to_state: str,
                 trigger_action: Action,
                 conditions: Optional[List[Dict[str, Any]]] = None):
        self.from_state = from_state
        self.to_state = to_state
        self.trigger_action = trigger_action
        self.conditions = conditions if conditions is not None else []

    def __repr__(self):
        return (f"Transition(from_state='{self.from_state}', to_state='{self.to_state}', "
                f"trigger_action={self.trigger_action}, conditions={self.conditions})")

class State:
    """Represents a state in a state machine."""
    def __init__(self,
                 name: str,
                 entry_actions: Optional[List[Action]] = None,
                 exit_actions: Optional[List[Action]] = None):
        self.name = name
        self.entry_actions = entry_actions if entry_actions is not None else []
        self.exit_actions = exit_actions if exit_actions is not None else []

    def __repr__(self):
        return (f"State(name='{self.name}', entry_actions={self.entry_actions}, "
                f"exit_actions={self.exit_actions})")

class StateMachine:
    """Represents a complete state machine."""
    def __init__(self,
                 name: str,
                 initial_state: str,
                 states: Dict[str, State],
                 transitions: List[Transition]):
        self.name = name
        self.initial_state = initial_state
        self.states = states
        self.transitions = transitions

    def __repr__(self):
        return (f"StateMachine(name='{self.name}', initial_state='{self.initial_state}', "
                f"states={list(self.states.keys())}, transitions_count={len(self.transitions)})")
