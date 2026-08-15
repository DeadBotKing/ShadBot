"""
ShadBot Agent Platform

Pipeline Definition component for 6.3 Pipeline Management.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Sequence
from uuid import UUID, uuid4
from agentplatform.domain.contracts import AgentContract


@dataclass(frozen=True, slots=True)
class PipelineStep:
    step_number: int
    agent: AgentContract
    requires_handoff_from: int | None = None


@dataclass(frozen=True, slots=True)
class ExecutionPipeline:
    pipeline_id: UUID
    task_title: str
    steps: tuple[PipelineStep, ...]
    total_steps: int
