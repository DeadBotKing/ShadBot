"""
ShadBot Agent Platform

Agent intent model.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum


class IntentType(str, Enum):
    """
    User intention categories.
    """

    CREATE = "create"

    MODIFY = "modify"

    FIX = "fix"

    ANALYZE = "analyze"

    OPTIMIZE = "optimize"

    RESEARCH = "research"

    EXPLAIN = "explain"

    REVIEW = "review"

    DECIDE = "decide"

    EXECUTE = "execute"

    CONTINUE = "continue"


@dataclass(frozen=True, slots=True)
class Intent:
    """
    Classified user intent.
    """

    intent_type: IntentType

    confidence: float

    explanation: str
