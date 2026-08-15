"""
ShadBot Agent Platform

Checkpoint Versioning component for 7.5 Checkpoint System.
"""

from __future__ import annotations

from typing import Sequence
from .checkpoint_entity import CheckpointEntity


class CheckpointVersioning:
    """
    Calculates next checkpoint version number for a project.
    """

    def next_version(self, existing: Sequence[CheckpointEntity]) -> int:
        if not existing:
            return 1
        return max(c.version for c in existing) + 1
