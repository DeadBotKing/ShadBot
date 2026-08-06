"""
ShadBot Agent Platform

Agent Context Injector
"""

from __future__ import annotations

from uuid import UUID

from agentplatform.domain.context import (
    BrainContext,
)

from .context_access import AgentContextAccess
from .runtime_agent import RuntimeAgent


class AgentContextInjector:
    """
    Injects brain context into runtime agents.
    """

    def __init__(
        self,
        context_access: AgentContextAccess,
    ) -> None:

        self._context_access = context_access

    def inject(
        self,
        agent: RuntimeAgent,
        project_id: UUID,
    ) -> BrainContext:
        """
        Build and attach context to agent.
        """

        context = self._context_access.build(
            project_id,
        )

        agent.context = context

        return context
