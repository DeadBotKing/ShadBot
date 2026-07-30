"""
ShadBot Project Intelligence

Resume Serializer
"""

from __future__ import annotations

from typing import Any

from projectintelligence.application.export.base_serializer import (
    BaseSerializer,
)
from projectintelligence.domain.resume.project_resume import (
    ProjectResume,
)


class ResumeSerializer(BaseSerializer):
    """
    Serializes ProjectResume into JSON-safe data.
    """

    def serialize(
        self,
        value: ProjectResume,
    ) -> dict[str, Any]:
        """
        Convert ProjectResume into dictionary.
        """

        return {
            "project_id": str(
                value.project_id,
            ),
            "metadata": {
                "resume_id": str(
                    value.metadata.resume_id,
                ),
                "snapshot_id": str(
                    value.metadata.snapshot_id,
                ),
                "generated_at": value.metadata.generated_at.isoformat(),
                "generator_version": value.metadata.generator_version,
            },
            "state": {
                "current_phase": value.state.current_phase,
                "status": value.state.status,
            },
            "summary": {
                "overview": value.summary.overview,
            },
            "completed_work": [
                item.title
                for item in value.completed_work
            ],
            "pending_work": [
                item.title
                for item in value.pending_work
            ],
            "recommendations": [
                item.title
                for item in value.recommendations
            ],
        }