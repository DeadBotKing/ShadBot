"""
ShadBot Project Intelligence

Knowledge Serializer
"""

from __future__ import annotations

from typing import Any

from projectintelligence.application.export.base_serializer import (
    BaseSerializer,
)
from projectintelligence.domain.knowledge.project_knowledge import (
    ProjectKnowledge,
)


class KnowledgeSerializer(BaseSerializer):
    """
    Serializes ProjectKnowledge into JSON-safe data.
    """

    def serialize(
        self,
        value: ProjectKnowledge,
    ) -> dict[str, Any]:
        """
        Convert ProjectKnowledge into dictionary.
        """

        return {
            "knowledge_id": str(
                value.knowledge_id,
            ),
            "project_id": str(
                value.project_id,
            ),
            "languages": list(
                value.languages,
            ),
            "frameworks": list(
                value.frameworks,
            ),
            "dependency_map": dict(
                value.dependency_map,
            ),
            "architecture_description": value.architecture_description,
            "technologies": list(
                value.technologies,
            ),
            "project_conventions": list(
                value.project_conventions,
            ),
            "coding_rules": list(
                value.coding_rules,
            ),
            "known_constraints": list(
                value.known_constraints,
            ),
            "historical_changes": list(
                value.historical_changes,
            ),
            "intelligence_notes": list(
                value.intelligence_notes,
            ),
            "findings": list(
                value.findings,
            ),
        }
