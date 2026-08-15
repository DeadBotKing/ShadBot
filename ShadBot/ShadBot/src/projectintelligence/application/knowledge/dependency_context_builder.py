"""
ShadBot Project Intelligence

Dependency Context Builder
"""

from __future__ import annotations

from projectintelligence.domain.snapshot.project_snapshot import (
    ProjectSnapshot,
)


class DependencyContextBuilder:
    """
    Builds dependency context from a project snapshot.
    """

    def build(
        self,
        snapshot: ProjectSnapshot,
    ) -> dict[str, object]:
        """
        Build dependency context.
        """

        return {
            "dependencies": snapshot.dependencies,
            "dependency_count": len(snapshot.dependencies),
        }
