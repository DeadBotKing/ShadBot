"""
ShadBot Agent Platform

Resume Context Loader component for 7.6 Resume System.
"""

from __future__ import annotations

from typing import Any
from uuid import UUID
from agentplatform.application.runtime.checkpoint_system import CheckpointEntity


class ResumeContextLoader:
    """
    Loads restored checkpoint snapshot data into active execution context.
    """

    def load_context(self, checkpoint: CheckpointEntity) -> dict[str, Any]:
        data = dict(checkpoint.snapshot_data)
        data["resumed_from_version"] = checkpoint.version
        data["resumed_from_step"] = checkpoint.step_number
        return data
