"""
ShadBot Agent Platform

Project Intelligence context adapter.
"""

from __future__ import annotations

from typing import Any

from projectintelligence.domain.handoff.agent_context_package import (
    AgentContextPackage,
)


class ProjectIntelligenceAdapter:
    """
    Converts Project Intelligence output
    into Agent Platform execution context data.
    """

    def convert(
        self,
        package: AgentContextPackage,
    ) -> dict[str, Any]:
        """
        Convert agent context package into
        agent-consumable dictionary.
        """

        evolution: dict[str, Any] | None = None

        if package.evolution:
            evolution = {
                "recent_changes": list(
                    package.evolution.recent_changes,
                ),
                "added_files": list(
                    package.evolution.added_files,
                ),
                "removed_files": list(
                    package.evolution.removed_files,
                ),
                "modified_files": list(
                    package.evolution.modified_files,
                ),
                "impact_summary": package.evolution.impact_summary,
            }

        return {
            "project_id": str(package.project_id),
            "summary": package.summary,
            "technologies": list(package.technologies),
            "frameworks": list(package.frameworks),
            "languages": list(package.languages),
            "dependencies": dict(package.dependencies),
            "architecture_description": package.architecture_description,
            "conventions": list(package.conventions),
            "constraints": list(package.constraints),
            "recommendations": list(package.recommendations),
            "current_state": package.current_state,
            "evolution": evolution,
            "metadata": {
                "context_id": str(package.metadata.context_id),
                "version": package.metadata.version,
                "created_at": package.metadata.created_at.isoformat(),
            },
        }
