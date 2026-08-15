"""
ShadBot Agent Platform

Unified service for 6.3 Pipeline Management.
"""

from __future__ import annotations

from typing import Sequence
from agentplatform.domain.contracts import AgentContract
from .completion_detection import PipelineCompletionDetector
from .dependency_management import PipelineDependencyManager
from .pipeline_builder import PipelineBuilder
from .pipeline_definition import ExecutionPipeline, PipelineStep
from .state_tracking import PipelineState, PipelineStateTracker


class PipelineManagementService:
    """
    Orchestrates building, tracking, checking dependencies, and completion of execution pipelines.
    """

    def __init__(
        self,
        builder: PipelineBuilder | None = None,
        tracker: PipelineStateTracker | None = None,
        dep_mgr: PipelineDependencyManager | None = None,
        detector: PipelineCompletionDetector | None = None,
    ) -> None:
        self._builder = builder or PipelineBuilder()
        self._tracker = tracker or PipelineStateTracker()
        self._dep_mgr = dep_mgr or PipelineDependencyManager()
        self._detector = detector or PipelineCompletionDetector()

    def create_pipeline(self, task_title: str, agents: Sequence[AgentContract]) -> tuple[ExecutionPipeline, PipelineState]:
        pipe = self._builder.build_pipeline(task_title, agents)
        state = self._tracker.init_state(pipe.pipeline_id)
        return pipe, state

    def check_ready(self, step: PipelineStep, state: PipelineState) -> bool:
        return self._dep_mgr.is_step_ready(step, state.completed_steps)

    def advance_pipeline(self, pipeline: ExecutionPipeline, step_number: int) -> tuple[PipelineState, bool]:
        new_state = self._tracker.complete_step(pipeline.pipeline_id, step_number)
        done = self._detector.is_completed(pipeline, new_state)
        return new_state, done
