"""
ShadBot Agent Platform

JSON based project memory repository.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Iterable
from uuid import UUID

from agentplatform.domain.memory import (
    MemoryEntry,
)


class JsonMemoryRepository:
    """
    Persistent JSON memory storage.

    Memory belongs to the target project workspace.
    """

    DIRECTORY_NAME = ".shadbot"

    MEMORY_DIRECTORY = "memory"

    MEMORY_FILE = "memories.json"

    def __init__(
        self,
        project_root: Path,
    ) -> None:

        self._project_root = project_root

        self._memory_path = project_root / self.DIRECTORY_NAME / self.MEMORY_DIRECTORY

        self._file = self._memory_path / self.MEMORY_FILE

        self._ensure_storage()

    def save(
        self,
        entry: MemoryEntry,
    ) -> None:
        """
        Persist memory entry.
        """

        records = self._load()

        records.append(
            entry.to_dict(),
        )

        self._write(
            records,
        )

    def save_many(
        self,
        entries: Iterable[MemoryEntry],
    ) -> None:
        """
        Persist multiple memories.
        """

        records = self._load()

        records.extend(entry.to_dict() for entry in entries)

        self._write(
            records,
        )

    def get_project_memory(
        self,
        project_id: UUID,
    ) -> list[MemoryEntry]:
        """
        Retrieve project memories.
        """

        result: list[MemoryEntry] = []

        for item in self._load():

            if item.get(
                "project_id",
            ) != str(project_id):
                continue

            result.append(
                MemoryEntry(
                    project_id=UUID(
                        item["project_id"],
                    ),
                    content=str(
                        item["content"],
                    ),
                    source=str(
                        item["source"],
                    ),
                    confidence=float(
                        item.get(
                            "confidence",
                            1.0,
                        ),
                    ),
                    memory_id=UUID(
                        item["memory_id"],
                    ),
                )
            )

        return result

    def clear_project(
        self,
        project_id: UUID,
    ) -> None:
        """
        Remove project memories.
        """

        records = [
            item
            for item in self._load()
            if item.get(
                "project_id",
            )
            != str(project_id)
        ]

        self._write(
            records,
        )

    def _ensure_storage(
        self,
    ) -> None:

        self._memory_path.mkdir(
            parents=True,
            exist_ok=True,
        )

        if not self._file.exists():

            self._write(
                [],
            )

    def _load(
        self,
    ) -> list[dict[str, object]]:

        if not self._file.exists():
            return []

        with self._file.open(
            "r",
            encoding="utf-8",
        ) as file:

            data = json.load(
                file,
            )

        if not isinstance(
            data,
            list,
        ):
            return []

        return data

    def _write(
        self,
        records: list[dict[str, object]],
    ) -> None:

        with self._file.open(
            "w",
            encoding="utf-8",
        ) as file:

            json.dump(
                records,
                file,
                indent=4,
                ensure_ascii=False,
            )
