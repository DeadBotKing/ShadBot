"""
ShadBot Agent Platform

Checkpoint Storage component for 7.5 Checkpoint System.
"""

from __future__ import annotations

from uuid import UUID
from .checkpoint_entity import CheckpointEntity


class CheckpointStorage:
    """
    Stores and retrieves persistent runtime checkpoints.
    """

    def __init__(self) -> None:
        self._checkpoints: dict[UUID, list[CheckpointEntity]] = {}

    def save_checkpoint(self, cp: CheckpointEntity) -> CheckpointEntity:
        if cp.project_id not in self._checkpoints:
            self._checkpoints[cp.project_id] = []
        self._checkpoints[cp.project_id].append(cp)
        return cp

    def load_latest(self, project_id: UUID) -> CheckpointEntity | None:
        cps = self._checkpoints.get(project_id, [])
        if not cps:
            return None
        return sorted(cps, key=lambda c: c.version, reverse=True)[0]
