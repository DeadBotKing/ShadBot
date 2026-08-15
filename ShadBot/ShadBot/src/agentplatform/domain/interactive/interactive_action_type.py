"""
ShadBot Agent Platform

Interactive Action Type enum.
"""

from __future__ import annotations

from enum import Enum


class InteractiveActionType(str, Enum):
    """
    Types of conversational co-pilot actions.
    """

    BUG_FIX = "bug_fix"
    FEATURE_ADDITION = "feature_addition"
    REFACTORING = "refactoring"
    OPTIMIZATION = "optimization"
    EXPLANATION = "explanation"
    GENERAL_CHAT = "general_chat"
