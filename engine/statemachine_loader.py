# engine/statemachine_loader.py

import yaml
from typing import Dict, List
from engine.statemachine import StateMachine, State, Transition, Action

class StateMachineLoader:
    """Loads state machine definitions from YAML files."""

    @staticmethod
    def load_from_yaml(filepath: str) -> StateMachine:
        """
        Loads a state machine definition from a YAML file.

        Args:
            filepath: The path to the YAML file.

        Returns:
            A StateMachine object.
        """
        with open(filepath, 'r') as file:
            data = yaml.safe_load(file)

        name = data.get('name', 'UnnamedStateMachine')
        initial_state_name = data.get('initial_state')
        
        if not initial_state_name:
            raise ValueError("State machine YAML must specify an 'initial_state'.")

        states: Dict[str, State] = {}
        for state_name, state_data in data.get('states', {}).items():
            entry_actions = [Action(a['name'], a.get('params')) for a in state_data.get('on_entry', [])]
            exit_actions = [Action(a['name'], a.get('params')) for a in state_data.get('on_exit', [])]
            states[state_name] = State(state_name, entry_actions, exit_actions)

        transitions: List[Transition] = []
        for transition_data in data.get('transitions', []):
            from_state = transition_data['from']
            to_state = transition_data['to']
            trigger_action_name = transition_data['trigger']['name']
            trigger_action_params = transition_data['trigger'].get('params')
            trigger_action = Action(trigger_action_name, trigger_action_params)
            conditions = transition_data.get('conditions', [])
            transitions.append(Transition(from_state, to_state, trigger_action, conditions))

        return StateMachine(name, initial_state_name, states, transitions)