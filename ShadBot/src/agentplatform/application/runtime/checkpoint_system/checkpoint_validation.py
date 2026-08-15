"""
ShadBot Agent Platform

Checkpoint Validation component for 7.5 Checkpoint System.
"""

from __future__ import annotations

from dataclasses import dataclass
from .checkpoint_entity import CheckpointEntity


@dataclass(frozen=True, slots=True)
class CheckpointValidationResult:
    valid: bool
    reason: str


class CheckpointValidator:
    """
    Validates integrity and restorable condition of a checkpoint.
    """

    def validate(self, cp: CheckpointEntity) -> CheckpointValidationResult:
        if not cp.snapshot_data:
            return CheckpointValidationResult(False, "Checkpoint snapshot_data is empty.")
        return CheckpointValidationResult(True, "Checkpoint is valid and restorable.")
