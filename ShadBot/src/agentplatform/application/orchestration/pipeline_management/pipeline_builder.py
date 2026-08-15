"""
ShadBot Agent Platform

Pipeline Builder component for 6.3 Pipeline Management.
"""

from __future__ import annotations

from typing import Sequence
from uuid import uuid4
from agentplatform.domain.contracts import AgentContract
from .pipeline_definition import ExecutionPipeline, PipelineStep


class PipelineBuilder:
    """
    Builds an execution pipeline from an ordered sequence of selected agents.
    """

    def build_pipeline(self, task_title: str, agents: Sequence[AgentContract]) -> ExecutionPipeline:
        steps: list[PipelineStep] = []
        for idx, ag in enumerate(agents, start=1):
            prev = (idx - 1) if idx > 1 else None
            steps.append(
                PipelineStep(
                    step_number=idx,
                    agent=ag,
                    requires_handoff_from=prev,
                )
            )
        return ExecutionPipeline(
            pipeline_id=uuid4(),
            task_title=task_title,
            steps=tuple(steps),
            total_steps=len(steps),
        )
