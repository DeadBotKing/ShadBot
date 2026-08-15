"""
ShadBot Agent Platform

Reviewer Agent Ability
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
class ReviewerAbility:
    """
    Built-in ability for Reviewer agents.

    Responsible for:
    - code review
    - bug detection
    - security assessment
    - quality evaluation
    """

    executor: CapabilityExecutor

    ROLE = AgentRole.REVIEWER

    CAPABILITIES = frozenset(
        {
            AgentCapability.CODE_REVIEW,
            AgentCapability.BUG_DETECTION,
            AgentCapability.SECURITY_REVIEW,
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

    def review_code(
        self,
        *,
        agent: RuntimeAgent,
        context: BrainContext,
    ) -> object:
        """
        Execute code review capability.
        """

        return self.executor.execute(
            capability=AgentCapability.CODE_REVIEW,
            agent=agent,
            context=context,
        )

    def detect_bugs(
        self,
        *,
        agent: RuntimeAgent,
        context: BrainContext,
    ) -> object:
        """
        Execute bug detection capability.
        """

        return self.executor.execute(
            capability=AgentCapability.BUG_DETECTION,
            agent=agent,
            context=context,
        )

    def security_review(
        self,
        *,
        agent: RuntimeAgent,
        context: BrainContext,
    ) -> object:
        """
        Execute security review capability.
        """

        return self.executor.execute(
            capability=AgentCapability.SECURITY_REVIEW,
            agent=agent,
            context=context,
        )

    def validate(
        self,
        agent: RuntimeAgent,
    ) -> bool:
        """
        Validate reviewer runtime ability.
        """

        if agent.role != self.ROLE:
            return False

        return all(
            agent.supports(
                capability,
            )
            for capability in self.CAPABILITIES
        )
