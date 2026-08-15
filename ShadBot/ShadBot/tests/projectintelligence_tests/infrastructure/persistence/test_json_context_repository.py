from pathlib import Path
from uuid import uuid4

from projectintelligence.domain.context.project_context import (
    ProjectContext,
)
from projectintelligence.infrastructure.persistence.json.json_context_repository import (
    JsonContextRepository,
)


def test_json_context_repository_saves_context(tmp_path: Path) -> None:
    repository = JsonContextRepository(tmp_path)

    context = ProjectContext(
        project_id=uuid4(),
        snapshot_id=uuid4(),
    )

    repository.save(context)

    assert (tmp_path / f"{context.context_id}.json").exists()
