"""
ShadBot Agent Platform

5.12 Goal & Intent Flow module.
"""

from .goal_alignment import AlignedGoal, GoalAligner
from .goal_intent_service import GoalIntentPackage, GoalIntentService
from .intent_correction import CorrectedIntent, IntentCorrector
from .intent_detection import DetectedIntent, IntentDetector
from .priority_management import PriorityAllocation, PriorityManager

__all__ = [
    "DetectedIntent",
    "IntentDetector",
    "AlignedGoal",
    "GoalAligner",
    "PriorityAllocation",
    "PriorityManager",
    "CorrectedIntent",
    "IntentCorrector",
    "GoalIntentPackage",
    "GoalIntentService",
]
