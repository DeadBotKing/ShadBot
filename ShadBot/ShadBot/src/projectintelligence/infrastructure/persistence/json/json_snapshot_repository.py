"""
ShadBot Project Intelligence

JSON Snapshot Repository
"""

from __future__ import annotations

import json
from datetime import datetime
from pathlib import Path
from uuid import UUID

from projectintelligence.application.ports.outbound.snapshot_repository import (
    SnapshotRepository,
)
from projectintelligence.domain.snapshot.project_snapshot import (
    ProjectSnapshot,
)
from projectintelligence.infrastructure.persistence.mapping.snapshot_json_mapper import (
    SnapshotJsonMapper,
)


class JsonSnapshotRepository(SnapshotRepository):
    """
    JSON implementation of snapshot persistence.
    """

    def __init__(
        self,
        storage_path: Path,
    ) -> None:
        self.storage_path = storage_path

        self.storage_path.mkdir(
            parents=True,
            exist_ok=True,
        )

    def save(
        self,
        snapshot: ProjectSnapshot,
    ) -> None:
        file_path = self.storage_path / f"{snapshot.snapshot_id}.json"

        data = SnapshotJsonMapper.to_dict(snapshot)

        file_path.write_text(
            json.dumps(
                data,
                indent=4,
                default=str,
            ),
            encoding="utf-8",
        )

    def update(
        self,
        snapshot: ProjectSnapshot,
    ) -> None:
        self.save(snapshot)

    def delete(
        self,
        snapshot_id: UUID,
    ) -> None:
        file_path = self.storage_path / f"{snapshot_id}.json"

        if file_path.exists():
            file_path.unlink()

    def exists(
        self,
        snapshot_id: UUID,
    ) -> bool:
        return (self.storage_path / f"{snapshot_id}.json").exists()

    def get_latest(
        self,
        project_id: UUID,
    ) -> ProjectSnapshot | None:

        snapshots = self.list_by_project(project_id)

        if not snapshots:
            return None

        return max(
            snapshots,
            key=lambda snapshot: snapshot.created_at,
        )

    def list_by_project(
        self,
        project_id: UUID,
    ) -> list[ProjectSnapshot]:

        snapshots: list[ProjectSnapshot] = []

        for file_path in self.storage_path.glob("*.json"):

            data = json.loads(
                file_path.read_text(
                    encoding="utf-8",
                ),
            )

            snapshot = SnapshotJsonMapper.from_dict(data)

            if snapshot.project_id == project_id:
                snapshots.append(snapshot)

        return snapshots

    def list_between_dates(
        self,
        project_id: UUID,
        start_date: datetime,
        end_date: datetime,
    ) -> list[ProjectSnapshot]:

        return [
            snapshot
            for snapshot in self.list_by_project(project_id)
            if start_date <= snapshot.created_at <= end_date
        ]

    def count(
        self,
        project_id: UUID,
    ) -> int:
        return len(
            self.list_by_project(project_id),
        )

    def get_by_id(
        self,
        snapshot_id: UUID,
    ) -> ProjectSnapshot | None:

        file_path = self.storage_path / f"{snapshot_id}.json"

        if not file_path.exists():
            return None

        data = json.loads(
            file_path.read_text(
                encoding="utf-8",
            ),
        )

        return SnapshotJsonMapper.from_dict(data)
