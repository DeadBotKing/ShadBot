"""
ShadBot Project Intelligence

Technology Context Builder
"""

from __future__ import annotations

from projectintelligence.domain.snapshot.project_snapshot import (
    ProjectSnapshot,
)


class TechnologyContextBuilder:
    """
    Builds technology context from a project snapshot.
    """

    def build(
        self,
        snapshot: ProjectSnapshot,
    ) -> dict[str, object]:
        """
        Build technology context.
        """

        return {
            "languages": snapshot.detected_languages,
            "frameworks": snapshot.detected_frameworks,
        }
