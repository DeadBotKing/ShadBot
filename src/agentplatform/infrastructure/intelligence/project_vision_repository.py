"""
ShadBot Agent Platform

Project vision JSON repository.
"""

from __future__ import annotations

import json
from dataclasses import asdict
from pathlib import Path
from typing import Any

from agentplatform.domain.intelligence import (
    ProjectVision,
)


class ProjectVisionRepository:
    """
    Persistent storage for project vision.

    Storage location belongs to target project.
    """

    FILE_NAME = "project_vision.json"

    def save(
        self,
        project_path: Path,
        vision: ProjectVision,
    ) -> None:
        """
        Save project vision.
        """

        directory = project_path / ".shadbot" / "intelligence"

        directory.mkdir(
            parents=True,
            exist_ok=True,
        )

        file_path = directory / self.FILE_NAME

        with file_path.open(
            "w",
            encoding="utf-8",
        ) as file:
            json.dump(
                self._serialize(
                    vision,
                ),
                file,
                indent=4,
                ensure_ascii=False,
            )

    def load(
        self,
        project_path: Path,
    ) -> dict[str, Any]:
        """
        Load stored project vision.
        """

        file_path = project_path / ".shadbot" / "intelligence" / self.FILE_NAME

        if not file_path.exists():
            return {}

        with file_path.open(
            "r",
            encoding="utf-8",
        ) as file:
            return json.load(
                file,
            )

    def exists(
        self,
        project_path: Path,
    ) -> bool:
        """
        Check vision existence.
        """

        return (project_path / ".shadbot" / "intelligence" / self.FILE_NAME).exists()

    @staticmethod
    def _serialize(
        vision: ProjectVision,
    ) -> dict[str, object]:
        """
        Convert vision to JSON-safe structure.
        """

        data = asdict(
            vision,
        )

        return ProjectVisionRepository._convert(
            data,
        )

    @staticmethod
    def _convert(
        value: object,
    ) -> object:
        """
        Recursive JSON conversion.
        """

        if isinstance(
            value,
            dict,
        ):
            return {
                str(key): ProjectVisionRepository._convert(
                    item,
                )
                for key, item in value.items()
            }

        if isinstance(
            value,
            tuple,
        ):
            return [
                ProjectVisionRepository._convert(
                    item,
                )
                for item in value
            ]

        if hasattr(
            value,
            "isoformat",
        ):
            return value.isoformat()

        return value
