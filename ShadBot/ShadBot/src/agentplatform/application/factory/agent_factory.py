"""
Agent Factory.

Creates agent instances based on registered definitions.
"""

from __future__ import annotations

from typing import Type

from agentplatform.domain.contracts import AgentContract
from agentplatform.domain.models import AgentDefinition


class AgentFactory:
    """
    Factory responsible for creating agents.

    The factory separates agent creation logic from
    execution and orchestration layers.
    """

    def __init__(self) -> None:
        self._agents: dict[str, Type[AgentContract]] = {}

    def register(
        self,
        definition: AgentDefinition,
        agent_type: Type[AgentContract],
    ) -> None:
        """
        Register an agent implementation.

        Args:
            definition: Agent metadata definition.
            agent_type: Agent implementation class.
        """

        self._agents[definition.name] = agent_type

    def create(
        self,
        definition: AgentDefinition,
    ) -> AgentContract:
        """
        Create an agent instance.

        Args:
            definition: Requested agent definition.

        Returns:
            Agent instance.

        Raises:
            ValueError: If agent is not registered.
        """

        agent_type = self._agents.get(definition.name)

        if agent_type is None:
            raise ValueError(f"Agent '{definition.name}' is not registered")

        return agent_type()
