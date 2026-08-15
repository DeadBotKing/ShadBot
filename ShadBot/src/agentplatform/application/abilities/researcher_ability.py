"""
ShadBot Agent Platform

Researcher Agent Ability
"""

from __future__ import annotations

from dataclasses import dataclass

from agentplatform.application.agents import (
    RuntimeAgent,
)
from agentplatform.application.capabilities import (
    CapabilityExecutor,
)
from agentplatform.domain.agents import (
    AgentCapability,
    AgentRole,
)
from agentplatform.domain.context import (
    BrainContext,
)


@dataclass(slots=True)
class ResearcherAbility:
    """
    Built-in ability for Researcher agents.

    Responsible for:
    - technical research
    - documentation analysis
    - technology investigation
    - solution comparison
    """

    executor: CapabilityExecutor

    ROLE = AgentRole.RESEARCHER

    CAPABILITIES = frozenset(
        {
            AgentCapability.RESEARCH,
        }
    )

    def supports(
        self,
        capability: AgentCapability,
    ) -> bool:
        """
        Check capability support.
        """

        return capability in self.CAPABILITIES

    def research(
        self,
        *,
        agent: RuntimeAgent,
        context: BrainContext,
    ) -> object:
        """
        Execute research capability.
        """

        return self.executor.execute(
            capability=AgentCapability.RESEARCH,
            agent=agent,
            context=context,
        )

    def validate(
        self,
        agent: RuntimeAgent,
    ) -> bool:
        """
        Validate researcher runtime ability.
        """

        if agent.role != self.ROLE:
            return False

        return all(
            agent.supports(
                capability,
            )
            for capability in self.CAPABILITIES
        )
