"""
ShadBot Project Intelligence

Agent Context Export Serializer
"""

from __future__ import annotations

from typing import Any

from projectintelligence.application.export.base_serializer import (
    BaseSerializer,
)
from projectintelligence.domain.handoff.agent_context_package import (
    AgentContextPackage,
)


class AgentContextExportSerializer(BaseSerializer):
    """
    Serializes AgentContextPackage into JSON-safe data.
    """

    def serialize(
        self,
        value: AgentContextPackage,
    ) -> dict[str, Any]:
        """
        Convert AgentContextPackage into dictionary.
        """

        return {
            "metadata": {
                "context_id": str(
                    value.metadata.context_id,
                ),
                "version": value.metadata.version,
                "contract_version": value.metadata.contract_version,
                "created_at": value.metadata.created_at.isoformat(),
            },
            "project_id": str(
                value.project_id,
            ),
            "summary": value.summary,
            "technologies": list(
                value.technologies,
            ),
            "frameworks": list(
                value.frameworks,
            ),
            "languages": list(
                value.languages,
            ),
            "dependencies": dict(
                value.dependencies,
            ),
            "architecture_description": value.architecture_description,
            "conventions": list(
                value.conventions,
            ),
            "constraints": list(
                value.constraints,
            ),
            "recommendations": list(
                value.recommendations,
            ),
            "current_state": value.current_state,
        }
