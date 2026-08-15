from pathlib import Path
from uuid import uuid4

from projectintelligence.domain.snapshot.project_snapshot import (
    ProjectSnapshot,
)
from projectintelligence.infrastructure.persistence.json.json_snapshot_repository import (
    JsonSnapshotRepository,
)


def test_json_snapshot_repository_saves_snapshot(tmp_path: Path) -> None:
    repository = JsonSnapshotRepository(tmp_path)

    snapshot = ProjectSnapshot(
        project_id=uuid4(),
        workspace=tmp_path,
    )

    repository.save(snapshot)

    assert (tmp_path / f"{snapshot.snapshot_id}.json").exists()
