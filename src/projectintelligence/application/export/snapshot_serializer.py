"""
ShadBot Project Intelligence

Snapshot Serializer
"""

from __future__ import annotations

from typing import Any

from projectintelligence.application.export.base_serializer import (
    BaseSerializer,
)
from projectintelligence.domain.snapshot.project_snapshot import (
    ProjectSnapshot,
)


class SnapshotSerializer(BaseSerializer):
    """
    Serializes ProjectSnapshot into JSON-safe data.
    """

    def serialize(
        self,
        value: ProjectSnapshot,
    ) -> dict[str, Any]:
        """
        Convert ProjectSnapshot into dictionary.
        """

        return {
            "snapshot_id": str(
                value.snapshot_id,
            ),
            "project_id": str(
                value.project_id,
            ),
            "workspace": str(
                value.workspace,
            ),
            "detected_languages": list(
                value.detected_languages,
            ),
            "detected_frameworks": list(
                value.detected_frameworks,
            ),
            "dependencies": dict(
                value.dependencies,
            ),
        }