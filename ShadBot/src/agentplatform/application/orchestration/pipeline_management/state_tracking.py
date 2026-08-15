"""
ShadBot Agent Platform

Pipeline State Tracking component for 6.3 Pipeline Management.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from uuid import UUID


@dataclass(frozen=True, slots=True)
class PipelineState:
    pipeline_id: UUID
    current_step: int
    completed_steps: tuple[int, ...]
    status: str
    last_updated: str


class PipelineStateTracker:
    """
    Tracks state of an active execution pipeline.
    """

    def __init__(self) -> None:
        self._states: dict[UUID, PipelineState] = {}

    def init_state(self, pipeline_id: UUID) -> PipelineState:
        st = PipelineState(
            pipeline_id=pipeline_id,
            current_step=1,
            completed_steps=(),
            status="RUNNING",
            last_updated=datetime.now(timezone.utc).isoformat(),
        )
        self._states[pipeline_id] = st
        return st

    def complete_step(self, pipeline_id: UUID, step_number: int) -> PipelineState:
        old = self._states.get(pipeline_id)
        if old is None:
            raise KeyError(f"Pipeline not tracked: {pipeline_id}")
        new_comp = tuple(sorted(set(old.completed_steps + (step_number,))))
        st = PipelineState(
            pipeline_id=pipeline_id,
            current_step=step_number + 1,
            completed_steps=new_comp,
            status=old.status,
            last_updated=datetime.now(timezone.utc).isoformat(),
        )
        self._states[pipeline_id] = st
        return st
