"""
ShadBot Agent Platform

Agent Lifecycle Management component for 7.1 Agent Runtime.
"""

from __future__ import annotations

from datetime import datetime, timezone
from uuid import UUID, uuid4
from agentplatform.domain.contracts import AgentContract
from .agent_runtime_instance import AgentRuntimeInstance
from .runtime_state import AgentRuntimeState


class AgentLifecycleManager:
    """
    Manages runtime lifecycle of an individual Agent.
    """

    def create_instance(self, agent: AgentContract) -> AgentRuntimeInstance:
        inst_id = uuid4()
        state = AgentRuntimeState(
            instance_id=inst_id,
            agent_name=agent.name,
            status="CREATED",
        )
        return AgentRuntimeInstance(instance_id=inst_id, agent=agent, state=state)

    def start_instance(self, instance: AgentRuntimeInstance) -> AgentRuntimeInstance:
        new_state = AgentRuntimeState(
            instance_id=instance.instance_id,
            agent_name=instance.agent.name,
            status="RUNNING",
            started_at=datetime.now(timezone.utc),
        )
        return AgentRuntimeInstance(instance_id=instance.instance_id, agent=instance.agent, state=new_state)

    def terminate_instance(self, instance: AgentRuntimeInstance, success: bool = True) -> AgentRuntimeInstance:
        new_state = AgentRuntimeState(
            instance_id=instance.instance_id,
            agent_name=instance.agent.name,
            status="COMPLETED" if success else "FAILED",
            started_at=instance.state.started_at,
            stopped_at=datetime.now(timezone.utc),
        )
        return AgentRuntimeInstance(instance_id=instance.instance_id, agent=instance.agent, state=new_state)
