"""
ShadBot Agent Platform

Checkpoint Creator component for 7.5 Checkpoint System.
"""

from __future__ import annotations

from typing import Any
from uuid import UUID, uuid4
from .checkpoint_entity import CheckpointEntity


class CheckpointCreator:
    """
    Creates snapshot checkpoints of active runtime state.
    """

    def create(
        self,
        project_id: UUID,
        session_id: UUID,
        step_number: int,
        version: int,
        snapshot_data: dict[str, Any],
    ) -> CheckpointEntity:
        return CheckpointEntity(
            checkpoint_id=uuid4(),
            project_id=project_id,
            session_id=session_id,
            step_number=step_number,
            version=version,
            snapshot_data=dict(snapshot_data),
        )
