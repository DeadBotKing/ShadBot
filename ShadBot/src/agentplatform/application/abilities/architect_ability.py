"""
ShadBot Agent Platform

Architect Agent Ability
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
from agentplatform.domain.planning import (
    PlanningRequest,
)


@dataclass(slots=True)
class ArchitectAbility:
    """
    Built-in ability for Architect agents.

    Responsible for:
    - architecture analysis
    - design decisions
    - dependency evaluation
    - technical planning
    """

    executor: CapabilityExecutor

    ROLE = AgentRole.ARCHITECT

    CAPABILITIES = frozenset(
        {
            AgentCapability.ARCHITECTURE_ANALYSIS,
            AgentCapability.DESIGN_REVIEW,
            AgentCapability.DEPENDENCY_ANALYSIS,
        }
    )

    def supports(
        self,
        capability: AgentCapability,
    ) -> bool:
        """
        Check architect ability capability support.
        """

        return capability in self.CAPABILITIES

    def analyze_architecture(
        self,
        *,
        agent: RuntimeAgent,
        context: BrainContext,
    ) -> object:
        """
        Execute architecture analysis.
        """

        return self.executor.execute(
            capability=AgentCapability.ARCHITECTURE_ANALYSIS,
            agent=agent,
            context=context,
        )

    def review_design(
        self,
        *,
        agent: RuntimeAgent,
        context: BrainContext,
    ) -> object:
        """
        Execute design review.
        """

        return self.executor.execute(
            capability=AgentCapability.DESIGN_REVIEW,
            agent=agent,
            context=context,
        )

    def analyze_dependencies(
        self,
        *,
        agent: RuntimeAgent,
        context: BrainContext,
    ) -> object:
        """
        Execute dependency analysis.
        """

        return self.executor.execute(
            capability=AgentCapability.DEPENDENCY_ANALYSIS,
            agent=agent,
            context=context,
        )

    def create_architecture_plan(
        self,
        *,
        agent: RuntimeAgent,
        request: PlanningRequest,
    ) -> object:
        """
        Create technical architecture plan.
        """

        if agent.role != self.ROLE:
            raise PermissionError("Only architect agents can create architecture plans")

        if agent.planning is None:
            raise RuntimeError("Agent planning binding is missing")

        return agent.planning.create_plan(
            request,
        )

    def validate(
        self,
        agent: RuntimeAgent,
    ) -> bool:
        """
        Validate architect runtime ability.
        """

        if agent.role != self.ROLE:
            return False

        return all(
            agent.supports(
                capability,
            )
            for capability in self.CAPABILITIES
        )
