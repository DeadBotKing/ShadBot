"""
ShadBot Project Intelligence

Architecture Context Builder
"""

from __future__ import annotations

from projectintelligence.domain.snapshot.project_snapshot import (
    ProjectSnapshot,
)


class ArchitectureContextBuilder:
    """
    Builds architecture context from a project snapshot.
    """

    def build(
        self,
        snapshot: ProjectSnapshot,
    ) -> dict[str, object]:
        """
        Build architecture context.
        """

        return {
            "architecture_tree": snapshot.architecture_tree,
            "file_count": snapshot.file_count,
            "directory_count": snapshot.directory_count,
        }
