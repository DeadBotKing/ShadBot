"""
ShadBot Agent Platform

Research Operations
"""

from __future__ import annotations

from enum import Enum


class ResearchOperation(str, Enum):
    """
    Supported research operations.
    """

    SEARCH = "search"

    ANALYZE = "analyze"

    COMPARE = "compare"

    SUMMARIZE = "summarize"
