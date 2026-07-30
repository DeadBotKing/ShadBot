"""
ShadBot Project Intelligence

State Serializer
"""

from __future__ import annotations

from typing import Any

from projectintelligence.application.export.base_serializer import (
    BaseSerializer,
)
from projectintelligence.domain.resume.project_state import (
    ProjectState,
)


class StateSerializer(BaseSerializer):
    """
    Serializes ProjectState into JSON-safe data.
    """

    def serialize(
        self,
        value: ProjectState,
    ) -> dict[str, Any]:
        """
        Convert ProjectState into dictionary.
        """

        return {
            "current_phase": value.current_phase,
            "current_sub_phase": value.current_sub_phase,
            "architecture_version": value.architecture_version,
            "completed_components": value.completed_components,
            "pending_components": value.pending_components,
            "total_components": value.total_components,
            "completion_percentage": value.completion_percentage,
        }