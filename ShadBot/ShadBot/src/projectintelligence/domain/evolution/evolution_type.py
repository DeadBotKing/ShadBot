"""
ShadBot Project Intelligence

Evolution Type
"""

from __future__ import annotations

from enum import Enum


class EvolutionType(str, Enum):
    """
    Types of project evolution.
    """

    ADDED = "added"

    REMOVED = "removed"

    MODIFIED = "modified"

    RENAMED = "renamed"

    MOVED = "moved"
