"""
ShadBot Project Intelligence

Snapshot JSON Mapper
"""

from __future__ import annotations

from dataclasses import asdict
from pathlib import Path
from uuid import UUID

from projectintelligence.domain.snapshot.project_snapshot import (
    ProjectSnapshot,
)


class SnapshotJsonMapper:
    """
    Maps ProjectSnapshot objects to JSON-serializable dictionaries
    and reconstructs them back into domain objects.

    This mapper isolates serialization concerns from repository
    implementations and allows multiple persistence technologies
    (JSON, SQL Server, SQLite, etc.) to share the same mapping rules.
    """

    @staticmethod
    def to_dict(
        snapshot: ProjectSnapshot,
    ) -> dict:
        data = asdict(snapshot)

        data["snapshot_id"] = str(snapshot.snapshot_id)
        data["project_id"] = str(snapshot.project_id)
        data["workspace"] = str(snapshot.workspace)

        return data

    @staticmethod
    def from_dict(
        data: dict,
    ) -> ProjectSnapshot:
        return ProjectSnapshot(
            project_id=UUID(data["project_id"]),
            workspace=Path(data["workspace"]),
            snapshot_id=UUID(data["snapshot_id"]),
            created_at=datetime.fromisoformat(data["created_at"]),
            file_count=data["file_count"],
            directory_count=data["directory_count"],
            file_hashes=data["file_hashes"],
            detected_languages=data["detected_languages"],
            detected_frameworks=data["detected_frameworks"],
            dependencies=data["dependencies"],
            architecture_tree=data["architecture_tree"],
            git_commit=data["git_commit"],
            git_branch=data["git_branch"],
            changed_files=data["changed_files"],
            test_status=data["test_status"],
            quality_issues=data["quality_issues"],
        )
