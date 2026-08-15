"""
ShadBot Agent Platform

Project intelligence context provider.
"""

from __future__ import annotations

from typing import Any

from agentplatform.application.context.project_intelligence_adapter import (
    ProjectIntelligenceAdapter,
)
from projectintelligence.domain.handoff.agent_context_package import (
    AgentContextPackage,
)


class ProjectIntelligenceContextProvider:
    """
    Provides project intelligence context.
    """

    def __init__(
        self,
        adapter: ProjectIntelligenceAdapter | None = None,
        package: AgentContextPackage | None = None,
    ) -> None:

        self._adapter = adapter or ProjectIntelligenceAdapter()
        self._package = package

    def provide(
        self,
    ) -> dict[str, Any]:
        """
        Convert project intelligence output.
        """

        if self._package is None:
            return {}

        return self._adapter.convert(
            self._package,
        )
