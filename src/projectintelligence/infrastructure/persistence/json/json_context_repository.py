"""
ShadBot Project Intelligence

JSON Project Context Repository
"""

from __future__ import annotations

import json
from dataclasses import asdict
from pathlib import Path
from uuid import UUID

from projectintelligence.application.contracts.persistence.context_repository import (
    IContextRepository,
)
from projectintelligence.domain.context.project_context import (
    ProjectContext,
)


class JsonContextRepository(IContextRepository):
    """
    JSON implementation of project context persistence.
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
        context: ProjectContext,
    ) -> None:

        file_path = self.storage_path / (
            f"{context.context_id}.json"
        )

        data = asdict(context)

        data["context_id"] = str(
            context.context_id,
        )

        data["project_id"] = str(
            context.project_id,
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
        context_id: UUID,
    ) -> ProjectContext | None:

        file_path = self.storage_path / (
            f"{context_id}.json"
        )

        if not file_path.exists():
            return None

        # reconstruction will be implemented
        # after persistence tests are added

        return None