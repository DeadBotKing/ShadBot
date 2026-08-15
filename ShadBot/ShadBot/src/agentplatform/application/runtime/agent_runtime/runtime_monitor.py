"""
ShadBot Agent Platform

Agent Runtime Monitor component for 7.1 Agent Runtime.
"""

from __future__ import annotations

from dataclasses import dataclass
from uuid import UUID
from .agent_runtime_instance import AgentRuntimeInstance


@dataclass(frozen=True, slots=True)
class AgentRuntimeHealth:
    instance_id: UUID
    agent_name: str
    status: str
    is_active: bool


class AgentRuntimeMonitor:
    """
    Monitors status and active health of running agent instances.
    """

    def inspect(self, instance: AgentRuntimeInstance) -> AgentRuntimeHealth:
        return AgentRuntimeHealth(
            instance_id=instance.instance_id,
            agent_name=instance.agent.name,
            status=instance.state.status,
            is_active=(instance.state.status == "RUNNING"),
        )
