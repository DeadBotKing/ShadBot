"""
ShadBot Agent Platform

Runtime Observer Agent Ability
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

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
class RuntimeObserverAbility:
    """
    Built-in ability for runtime observer agents.

    Responsibilities:

    - runtime monitoring
    - execution observation
    - system health analysis
    - log inspection
    - metrics collection

    This ability is read-only.
    It observes system state and produces insights.
    """

    executor: CapabilityExecutor

    ROLE = AgentRole.RUNTIME_OBSERVER

    CAPABILITIES = frozenset(
        {
            AgentCapability.BUG_DETECTION,
            AgentCapability.SECURITY_REVIEW,
        }
    )

    def supports(
        self,
        capability: AgentCapability,
    ) -> bool:
        """
        Check supported capability.
        """

        return capability in self.CAPABILITIES

    def observe_runtime(
        self,
        *,
        agent: RuntimeAgent,
        context: BrainContext,
    ) -> object:
        """
        Observe runtime execution state.
        """

        return self.executor.execute(
            capability=AgentCapability.BUG_DETECTION,
            agent=agent,
            context=context,
        )

    def inspect_security(
        self,
        *,
        agent: RuntimeAgent,
        context: BrainContext,
    ) -> object:
        """
        Execute runtime security inspection.
        """

        return self.executor.execute(
            capability=AgentCapability.SECURITY_REVIEW,
            agent=agent,
            context=context,
        )

    def collect_runtime_report(
        self,
        *,
        agent: RuntimeAgent,
        context: BrainContext,
    ) -> dict[str, Any]:
        """
        Execute complete runtime observation cycle.
        """

        runtime_state = self.observe_runtime(
            agent=agent,
            context=context,
        )

        security_state = self.inspect_security(
            agent=agent,
            context=context,
        )

        return {
            "runtime_state": runtime_state,
            "security_state": security_state,
        }

    def validate(
        self,
        agent: RuntimeAgent,
    ) -> bool:
        """
        Validate runtime observer ability binding.
        """

        if agent.role != self.ROLE:
            return False

        return all(
            agent.supports(
                capability,
            )
            for capability in self.CAPABILITIES
        )
