"""
ShadBot Agent Platform

Memory type definitions.
"""

from __future__ import annotations

from enum import Enum


class MemoryType(str, Enum):
    """
    Persistent memory categories.
    """

    EXPERIENCE = "experience"

    KNOWLEDGE = "knowledge"

    DECISION = "decision"

    LESSON = "lesson"

    EXECUTION = "execution"

    PROFILE = "profile"
