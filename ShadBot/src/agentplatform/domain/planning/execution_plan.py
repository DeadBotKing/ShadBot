"""
ShadBot Agent Platform

Execution plan domain model.
"""

from __future__ import annotations

from dataclasses import dataclass, field

from agentplatform.domain.agents import AgentRole
from agentplatform.domain.tasks import AgentTask


@dataclass(frozen=True, slots=True)
class ExecutionPlan:
    """
    Agent execution pipeline plan.
    """

    task: AgentTask

    agents: tuple[AgentRole, ...]

    metadata: dict[str, object] = field(
        default_factory=dict,
    )
