"""
ShadBot Agent Platform

Context Merge Strategy
"""

from __future__ import annotations

from enum import Enum


class ContextMergeStrategy(str, Enum):
    """
    Defines context merge behavior.
    """

    PRIORITY_BASED = "priority_based"

    SOURCE_BASED = "source_based"

    COMPLETE = "complete"
