"""
ShadBot Agent Platform

Application interactive package.
"""

from .conversational_intent_detector import ConversationalIntent, ConversationalIntentDetector
from .interactive_copilot_service import InteractiveCoPilotService, InteractiveResponsePackage
from .interactive_feedback_handler import InteractiveFeedbackHandler

__all__ = [
    "ConversationalIntent",
    "ConversationalIntentDetector",
    "InteractiveFeedbackHandler",
    "InteractiveResponsePackage",
    "InteractiveCoPilotService",
]
