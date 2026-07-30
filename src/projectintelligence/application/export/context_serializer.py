"""
ShadBot Project Intelligence

Context Serializer
"""

from __future__ import annotations

from typing import Any

from projectintelligence.application.export.base_serializer import (
    BaseSerializer,
)
from projectintelligence.domain.context.project_context import (
    ProjectContext,
)


class ContextSerializer(BaseSerializer):
    """
    Serializes ProjectContext into JSON-safe data.
    """

    def serialize(
        self,
        value: ProjectContext,
    ) -> dict[str, Any]:
        """
        Convert ProjectContext into dictionary.
        """

        return {
            "context_id": str(
                value.context_id,
            ),
            "project_id": str(
                value.project_id,
            ),
            "snapshot_id": str(
                value.snapshot_id,
            ),
            "technology_context": list(
                value.technology_context,
            ),
            "architecture_context": list(
                value.architecture_context,
            ),
            "dependency_context": list(
                value.dependency_context,
            ),
            "change_context": list(
                value.change_context,
            ),
            "constraint_context": list(
                value.constraint_context,
            ),
            "agent_instructions": list(
                value.agent_instructions,
            ),
            "reasoning_metadata": dict(
                value.reasoning_metadata,
            ),
            "git_state": (
                None
                if value.git_state is None
                else {
                    "branch_name": value.git_state.branch_name,
                }
            ),
        }