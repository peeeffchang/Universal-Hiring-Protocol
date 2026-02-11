# engine/validator.py

from typing import Dict, Any, Optional
from engine.statemachine import StateMachine, State, Transition, Action
from engine.action_envelope import IntentBasedActionEnvelope
from engine.capabilities_loader import CapabilitiesRegistry # Import CapabilitiesRegistry

class ProtocolValidator:
    """Validates actions against a state machine."""

    def __init__(self,
                 state_machine: StateMachine,
                 capabilities_registry: Optional[CapabilitiesRegistry] = None): # Added capabilities_registry
        self.state_machine = state_machine
        self.capabilities_registry = capabilities_registry

    def validate_action(self,
                        current_state_name: str,
                        action_envelope: IntentBasedActionEnvelope) -> Optional[str]:
        """
        Validates if an action is allowed from the current state according to the state machine,
        and optionally checks against registered capabilities.

        Args:
            current_state_name: The name of the current state.
            action_envelope: The IntentBasedActionEnvelope representing the action to validate.

        Returns:
            None if the action is valid, otherwise a string with an error message.
        """
        if current_state_name not in self.state_machine.states:
            return f"Invalid current state: '{current_state_name}' not found in state machine."

        intent_name = action_envelope.intent.split(':')[-1] # Extract intent name

        # Optional: Validate intent against capabilities registry if provided
        if self.capabilities_registry:
            # Check if the intent corresponds to a registered capability ID or name
            # For simplicity, we'll check against capability name, assuming it aligns with intent_name
            if not self.capabilities_registry.get_capability_by_name(intent_name):
                return (f"Intent '{action_envelope.intent}' is not a registered capability. "
                        f"From state '{current_state_name}'.")

        # Find transitions from the current state that match the action's intent
        possible_transitions = []
        for transition in self.state_machine.transitions:
            if transition.from_state == current_state_name and \
               transition.trigger_action.name == intent_name:
                possible_transitions.append(transition)
        
        if not possible_transitions:
            return (f"No valid transition found from state '{current_state_name}' "
                    f"for intent '{action_envelope.intent}'.")
        
        return None # Action is valid