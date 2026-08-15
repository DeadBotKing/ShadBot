"""
ShadBot Project Intelligence

Agent Context Serializer
"""

from __future__ import annotations

from projectintelligence.domain.handoff.agent_context_package import (
    AgentContextPackage,
)


class AgentContextSerializer:
    """
    Serializes Agent Context packages
    into transport-ready payloads.
    """

    def serialize(
        self,
        package: AgentContextPackage,
    ) -> dict[str, object]:
        """
        Convert agent context package into JSON-compatible structure.
        """

        return {
            "metadata": {
                "context_id": str(
                    package.metadata.context_id,
                ),
                "version": package.metadata.version,
                "contract_version": (package.metadata.contract_version),
                "created_at": (package.metadata.created_at.isoformat()),
            },
            "project_id": str(
                package.project_id,
            ),
            "summary": package.summary,
            "technologies": list(
                package.technologies,
            ),
            "frameworks": list(
                package.frameworks,
            ),
            "languages": list(
                package.languages,
            ),
            "dependencies": dict(
                package.dependencies,
            ),
            "architecture_description": (package.architecture_description),
            "conventions": list(
                package.conventions,
            ),
            "constraints": list(
                package.constraints,
            ),
            "recommendations": list(
                package.recommendations,
            ),
            "current_state": package.current_state,
            "evolution": (
                {
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
                    "impact_summary": (package.evolution.impact_summary),
                }
                if package.evolution
                else None
            ),
        }
