"""
ShadBot Agent Platform

Engineer Agent Ability
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
class EngineerAbility:
    """
    Built-in ability for Engineer agents.

    Responsible for:
    - code implementation
    - refactoring
    - test creation
    - code improvement
    - engineering execution workflow
    """

    executor: CapabilityExecutor

    ROLE = AgentRole.ENGINEER

    CAPABILITIES = frozenset(
        {
            AgentCapability.CODE_GENERATION,
            AgentCapability.CODE_REFACTORING,
            AgentCapability.TEST_GENERATION,
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

    def generate_code(
        self,
        *,
        agent: RuntimeAgent,
        context: BrainContext,
    ) -> object:
        """
        Execute code generation capability.
        """

        return self.executor.execute(
            capability=AgentCapability.CODE_GENERATION,
            agent=agent,
            context=context,
        )

    def refactor_code(
        self,
        *,
        agent: RuntimeAgent,
        context: BrainContext,
    ) -> object:
        """
        Execute code refactoring capability.
        """

        return self.executor.execute(
            capability=AgentCapability.CODE_REFACTORING,
            agent=agent,
            context=context,
        )

    def generate_tests(
        self,
        *,
        agent: RuntimeAgent,
        context: BrainContext,
    ) -> object:
        """
        Execute test generation capability.
        """

        return self.executor.execute(
            capability=AgentCapability.TEST_GENERATION,
            agent=agent,
            context=context,
        )

    def create_implementation_plan(
        self,
        *,
        agent: RuntimeAgent,
        request: PlanningRequest,
    ) -> object:
        """
        Create engineering execution plan.
        """

        if agent.role != self.ROLE:
            raise PermissionError(
                "Only engineer agents can create implementation plans",
            )

        if agent.planning is None:
            raise RuntimeError(
                "Agent planning binding is missing",
            )

        return agent.planning.create_plan(
            request,
        )

    def validate(
        self,
        agent: RuntimeAgent,
    ) -> bool:
        """
        Validate engineer runtime ability.
        """

        if agent.role != self.ROLE:
            return False

        return all(
            agent.supports(
                capability,
            )
            for capability in self.CAPABILITIES
        )
