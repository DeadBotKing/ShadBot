"""
ShadBot Agent Platform

Agent Context Access
"""

from __future__ import annotations

from uuid import UUID

from agentplatform.application.context import (
    BrainContextFactory,
)
from agentplatform.domain.context import (
    BrainContext,
)


class AgentContextAccess:
    """
    Provides brain context access for agents.
    """

    def __init__(
        self,
        context_factory: BrainContextFactory,
    ) -> None:

        self._context_factory = context_factory

    def build(
        self,
        project_id: UUID,
    ) -> BrainContext:
        """
        Build context for agent execution.
        """

        return self._context_factory.create(
            project_id,
        )
