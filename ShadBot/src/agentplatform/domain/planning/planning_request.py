"""
ShadBot Agent Platform

Planning request contract.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from uuid import UUID

from agentplatform.domain.tasks import AgentTask


@dataclass(frozen=True, slots=True)
class PlanningRequest:
    """
    Input contract for planning.
    """

    task: AgentTask

    project_id: UUID | None = None

    metadata: dict[str, object] = field(
        default_factory=dict,
    )
