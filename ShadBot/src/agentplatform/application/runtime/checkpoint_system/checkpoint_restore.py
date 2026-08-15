"""
ShadBot Agent Platform

Checkpoint Restore Manager component for 7.5 Checkpoint System.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any
from uuid import UUID
from .checkpoint_entity import CheckpointEntity
from .checkpoint_validation import CheckpointValidator


@dataclass(frozen=True, slots=True)
class RestoredCheckpointPackage:
    restored: bool
    checkpoint: CheckpointEntity
    data: dict[str, Any]


class CheckpointRestoreManager:
    """
    Restores runtime execution state from a persistent checkpoint.
    """

    def __init__(self, validator: CheckpointValidator | None = None) -> None:
        self._validator = validator or CheckpointValidator()

    def restore(self, cp: CheckpointEntity) -> RestoredCheckpointPackage:
        val = self._validator.validate(cp)
        if not val.valid:
            raise RuntimeError(f"Cannot restore invalid checkpoint: {val.reason}")
        return RestoredCheckpointPackage(
            restored=True,
            checkpoint=cp,
            data=dict(cp.snapshot_data),
        )
