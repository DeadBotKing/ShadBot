"""
ShadBot Agent Platform

Agent profile capabilities.
"""

from __future__ import annotations

from enum import Enum


class ProfileCapability(str, Enum):
    """
    Supported agent capabilities.
    """

    REASONING = "reasoning"

    PLANNING = "planning"

    DECISION = "decision"

    REFLECTION = "reflection"

    VALIDATION = "validation"

    MEMORY = "memory"

    PROJECT_INTELLIGENCE = "project_intelligence"
