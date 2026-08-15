"""
ShadBot Agent Platform

Dependency Management component for 6.3 Pipeline Management.
"""

from __future__ import annotations

from .pipeline_definition import PipelineStep


class PipelineDependencyManager:
    """
    Checks if a pipeline step is ready for execution based on required handoffs.
    """

    def is_step_ready(self, step: PipelineStep, completed_steps: tuple[int, ...]) -> bool:
        if step.requires_handoff_from is None:
            return True
        return step.requires_handoff_from in completed_steps
