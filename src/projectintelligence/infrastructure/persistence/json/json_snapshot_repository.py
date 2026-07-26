"""
ShadBot Project Intelligence

JSON Snapshot Repository
"""

from __future__ import annotations

import json
from dataclasses import asdict
from pathlib import Path
from uuid import UUID

from projectintelligence.application.contracts.persistence.snapshot_repository import (
    ISnapshotRepository,
)
from projectintelligence.domain.snapshot.project_snapshot import (
    ProjectSnapshot,
)


class JsonSnapshotRepository(ISnapshotRepository):
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
        file_path = self.storage_path / (
            f"{snapshot.snapshot_id}.json"
        )

        data = asdict(snapshot)

        data["snapshot_id"] = str(
            snapshot.snapshot_id,
        )

        data["project_id"] = str(
            snapshot.project_id,
        )

        data["workspace"] = str(
            snapshot.workspace,
        )

        file_path.write_text(
            json.dumps(
                data,
                indent=4,
                default=str,
            ),
            encoding="utf-8",
        )

    def get_by_id(
        self,
        snapshot_id: UUID,
    ) -> ProjectSnapshot | None:

        file_path = self.storage_path / (
            f"{snapshot_id}.json"
        )

        if not file_path.exists():
            return None

        # reconstruction will be implemented
        # in the next step
        return None