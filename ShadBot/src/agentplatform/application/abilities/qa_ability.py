"""
ShadBot Agent Platform

QA Agent Ability
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
class QAAbility:
    """
    Built-in ability for QA agents.

    Responsible for:
    - test execution
    - quality validation
    - regression detection
    - execution analysis
    """

    executor: CapabilityExecutor

    ROLE = AgentRole.QA

    CAPABILITIES = frozenset(
        {
            AgentCapability.TEST_GENERATION,
            AgentCapability.BUG_DETECTION,
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

    def run_tests(
        self,
        *,
        agent: RuntimeAgent,
        context: BrainContext,
    ) -> object:
        """
        Execute testing capability.

        QA agent uses this to execute
        project validation tests.
        """

        return self.executor.execute(
            capability=AgentCapability.TEST_GENERATION,
            agent=agent,
            context=context,
        )

    def detect_regression(
        self,
        *,
        agent: RuntimeAgent,
        context: BrainContext,
    ) -> object:
        """
        Detect regressions and failures.
        """

        return self.executor.execute(
            capability=AgentCapability.BUG_DETECTION,
            agent=agent,
            context=context,
        )

    def validate(
        self,
        agent: RuntimeAgent,
    ) -> bool:
        """
        Validate QA runtime ability.
        """

        if agent.role != self.ROLE:
            return False

        return all(
            agent.supports(
                capability,
            )
            for capability in self.CAPABILITIES
        )
