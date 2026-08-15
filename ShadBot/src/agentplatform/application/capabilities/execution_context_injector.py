"""
ShadBot Agent Platform

Capability Execution Context Injector
"""

from __future__ import annotations

from dataclasses import dataclass
from uuid import UUID

from agentplatform.application.context import (
    BrainContextFactory,
)
from agentplatform.domain.agents import (
    AgentCapability,
    AgentRole,
)
from agentplatform.domain.context import (
    BrainContext,
)


@dataclass(frozen=True, slots=True)
class CapabilityExecutionContext:
    """
    Complete execution context provided to capability execution.

    Contains:
    - Agent identity
    - Capability information
    - Brain context
    """

    agent_role: AgentRole

    capability: AgentCapability

    brain_context: BrainContext

    project_id: UUID


class ExecutionContextInjector:
    """
    Builds execution context for capability execution.
    """

    def __init__(
        self,
        context_factory: BrainContextFactory,
    ) -> None:

        self._context_factory = context_factory

    def inject(
        self,
        *,
        agent_role: AgentRole,
        capability: AgentCapability,
        project_id: UUID,
    ) -> CapabilityExecutionContext:
        """
        Create capability execution context.
        """

        brain_context = self._context_factory.create(
            project_id,
        )

        return CapabilityExecutionContext(
            agent_role=agent_role,
            capability=capability,
            brain_context=brain_context,
            project_id=project_id,
        )
