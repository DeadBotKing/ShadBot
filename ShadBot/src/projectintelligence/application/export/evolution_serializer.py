"""
ShadBot Project Intelligence

Evolution Serializer
"""

from __future__ import annotations

from typing import Any

from projectintelligence.application.export.base_serializer import (
    BaseSerializer,
)
from projectintelligence.domain.evolution.project_evolution import (
    ProjectEvolution,
)


class EvolutionSerializer(BaseSerializer):
    """
    Serializes ProjectEvolution into JSON-safe data.
    """

    def serialize(
        self,
        value: ProjectEvolution,
    ) -> dict[str, Any]:
        """
        Convert ProjectEvolution into dictionary.
        """

        return {
            "evolution_id": str(
                value.evolution_id,
            ),
            "project_id": str(
                value.project_id,
            ),
            "previous_snapshot_id": str(
                value.previous_snapshot_id,
            ),
            "current_snapshot_id": str(
                value.current_snapshot_id,
            ),
            "created_at": value.created_at.isoformat(),
            "changes": [
                {
                    "path": change.path,
                    "change_type": change.change_type.value,
                    "category": change.category,
                    "description": change.description,
                }
                for change in value.changes
            ],
        }
