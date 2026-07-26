"""
ShadBot Project Intelligence

Git Context Mapper
"""

from __future__ import annotations

from projectintelligence.application.git.models.git_context import (
    GitContext,
)
from projectintelligence.domain.git.git_repository_state import (
    GitRepositoryState,
)


class GitContextMapper:
    """
    Maps application GitContext into domain GitRepositoryState.
    """

    def map(
        self,
        git_context: GitContext,
    ) -> GitRepositoryState:
        """
        Convert Git analysis result into domain state.
        """

        changed_files = [
            change.path
            for change in git_context.changes
        ]

        added_files = [
            change.path
            for change in git_context.changes
            if change.change_type.value == "added"
        ]

        deleted_files = [
            change.path
            for change in git_context.changes
            if change.change_type.value == "deleted"
        ]

        modified_files = [
            change.path
            for change in git_context.changes
            if change.change_type.value == "modified"
        ]

        return GitRepositoryState(
            project_id=git_context.current_commit.project_id
            if git_context.current_commit
            and hasattr(git_context.current_commit, "project_id")
            else None,
            branch_name=git_context.status.current_branch,
            current_commit=(
                git_context.current_commit.hash
                if git_context.current_commit
                else ""
            ),
            commit_history=[
                commit.hash
                for commit in git_context.recent_commits
            ],
            changed_files=changed_files,
            added_files=added_files,
            deleted_files=deleted_files,
            modified_files=modified_files,
            is_clean=not git_context.status.is_dirty,
        )