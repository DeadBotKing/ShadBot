"""
ShadBot Project Intelligence

Change Context Builder
"""

from __future__ import annotations

from projectintelligence.domain.snapshot.project_snapshot import (
    ProjectSnapshot,
)


class ChangeContextBuilder:
    """
    Builds change context from a project snapshot.
    """

    def build(
        self,
        snapshot: ProjectSnapshot,
    ) -> dict[str, object]:
        """
        Build change context.
        """

        return {
            "git_branch": snapshot.git_branch,
            "git_commit": snapshot.git_commit,
            "changed_files": snapshot.changed_files,
            "changed_file_count": len(snapshot.changed_files),
            "test_status": snapshot.test_status,
            "quality_issues": snapshot.quality_issues,
        }
