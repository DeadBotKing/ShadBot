"""
ShadBot Agent Platform

6.4 Agent Handoff module.
"""

from .agent_handoff_service import AgentHandoffService, CompleteHandoffPackage
from .context_builder import HandoffContextBuilder
from .handoff_history import HandoffHistoryTracker
from .handoff_request import HandoffRequest
from .handoff_validation import HandoffValidationResult, HandoffValidator
from .transition_manager import AgentTransitionManager, AgentTransitionRecord

__all__ = [
    "HandoffRequest",
    "HandoffContextBuilder",
    "HandoffValidationResult",
    "HandoffValidator",
    "AgentTransitionRecord",
    "AgentTransitionManager",
    "HandoffHistoryTracker",
    "CompleteHandoffPackage",
    "AgentHandoffService",
]
