"""
ShadBot Agent Platform

Pipeline Completion Detection component for 6.3 Pipeline Management.
"""

from __future__ import annotations

from .pipeline_definition import ExecutionPipeline
from .state_tracking import PipelineState


class PipelineCompletionDetector:
    """
    Detects if an execution pipeline has completed all scheduled steps.
    """

    def is_completed(self, pipeline: ExecutionPipeline, state: PipelineState) -> bool:
        return len(state.completed_steps) >= pipeline.total_steps
