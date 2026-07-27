"""
ShadBot Project Intelligence

JSON Project Context Repository
"""

from __future__ import annotations

import json
from dataclasses import asdict
from pathlib import Path
from uuid import UUID

from projectintelligence.application.ports.outbound.context_repository import (
    ContextRepository,
)
from projectintelligence.domain.context.project_context import (
    ProjectContext,
)
from projectintelligence.infrastructure.persistence.mapping.context_json_mapper import (
    ContextJsonMapper,
)


class JsonContextRepository(ContextRepository):
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

        file_path = self.storage_path / f"{context.context_id}.json"

        data = ContextJsonMapper.to_dict(context)

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
        context: ProjectContext,
    ) -> None:
        self.save(context)

    def delete(
        self,
        context_id: UUID,
    ) -> None:
        file_path = self.storage_path / f"{context_id}.json"

        if file_path.exists():
            file_path.unlink()

    def exists(
        self,
        context_id: UUID,
    ) -> bool:
        return (self.storage_path / f"{context_id}.json").exists()

    def get_latest(
        self,
        project_id: UUID,
    ) -> ProjectContext | None:

        contexts = self.list_by_project(project_id)

        if not contexts:
            return None

        return max(
            contexts,
            key=lambda context: context.created_at,
        )

    def get_by_snapshot(
        self,
        snapshot_id: UUID,
    ) -> ProjectContext | None:

        for file_path in self.storage_path.glob("*.json"):

            data = json.loads(
                file_path.read_text(
                    encoding="utf-8",
                ),
            )

            context = ContextJsonMapper.from_dict(data)

            if context.snapshot_id == snapshot_id:
                return context

        return None

    def list_by_project(
        self,
        project_id: UUID,
    ) -> list[ProjectContext]:

        contexts: list[ProjectContext] = []

        for file_path in self.storage_path.glob("*.json"):

            data = json.loads(
                file_path.read_text(
                    encoding="utf-8",
                ),
            )

            context = ContextJsonMapper.from_dict(data)

            if context.project_id == project_id:
                contexts.append(context)

        return contexts

    def count(
        self,
        project_id: UUID,
    ) -> int:
        return len(
            self.list_by_project(project_id),
        )

    def get_by_id(
        self,
        context_id: UUID,
    ) -> ProjectContext | None:

        file_path = self.storage_path / f"{context_id}.json"

        if not file_path.exists():
            return None

        data = json.loads(
            file_path.read_text(
                encoding="utf-8",
            ),
        )

        return ContextJsonMapper.from_dict(data)
