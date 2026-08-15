"""
ShadBot Agent Platform

Project Intelligence Agent Ability
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
class ProjectIntelligenceAbility:
    """
    Built-in ability for Project Intelligence agents.

    Responsible for:
    - workspace understanding
    - architecture analysis
    - dependency analysis
    - project knowledge extraction
    - intelligence reporting

    This ability analyzes projects only.
    It does not generate or modify code.
    """

    executor: CapabilityExecutor

    ROLE = AgentRole.PROJECT_INTELLIGENCE

    CAPABILITIES = frozenset(
        {
            AgentCapability.ARCHITECTURE_ANALYSIS,
            AgentCapability.DEPENDENCY_ANALYSIS,
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

    def analyze_project(
        self,
        *,
        agent: RuntimeAgent,
        context: BrainContext,
    ) -> dict[str, object]:
        """
        Execute complete project intelligence workflow.

        Combines supported intelligence capabilities.
        """

        architecture = self.analyze_architecture(
            agent=agent,
            context=context,
        )

        dependencies = self.analyze_dependencies(
            agent=agent,
            context=context,
        )

        return {
            "architecture": architecture,
            "dependencies": dependencies,
        }

    def validate(
        self,
        agent: RuntimeAgent,
    ) -> bool:
        """
        Validate project intelligence runtime ability.
        """

        if agent.role != self.ROLE:
            return False

        return all(
            agent.supports(
                capability,
            )
            for capability in self.CAPABILITIES
        )
