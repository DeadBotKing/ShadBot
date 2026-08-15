"""
ShadBot Project Intelligence

Change Context Builder
"""

from __future__ import annotations

from projectintelligence.application.git.models.git_context import (
    GitContext,
)
from projectintelligence.domain.snapshot.project_snapshot import (
    ProjectSnapshot,
)


class ChangeContextBuilder:
    """
    Builds change context from project snapshot and git intelligence.
    """

    def build(
        self,
        snapshot: ProjectSnapshot,
        git_context: GitContext,
    ) -> dict[str, object]:
        """
        Build change context.
        """

        return {
            "git_status": {
                "is_repository": git_context.status.is_repository,
                "is_dirty": git_context.status.is_dirty,
                "ahead": git_context.status.ahead,
                "behind": git_context.status.behind,
                "current_branch": git_context.status.current_branch,
            },
            "current_commit": (
                {
                    "hash": git_context.current_commit.hash,
                    "short_hash": git_context.current_commit.short_hash,
                    "author": git_context.current_commit.author,
                    "message": git_context.current_commit.message,
                    "date": git_context.current_commit.date,
                }
                if git_context.current_commit
                else None
            ),
            "changed_files": [
                {
                    "path": change.path,
                    "type": change.change_type.value,
                    "staged": change.is_staged,
                }
                for change in git_context.changes
            ],
            "snapshot_quality_issues": snapshot.quality_issues,
            "test_status": snapshot.test_status,
            "recent_commits": [
                {
                    "hash": commit.hash,
                    "short_hash": commit.short_hash,
                    "author": commit.author,
                    "message": commit.message,
                    "date": commit.date,
                }
                for commit in git_context.recent_commits
            ],
        }
