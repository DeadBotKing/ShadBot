"""
ShadBot Agent Platform

Project evolution JSON repository.
"""

from __future__ import annotations

import json
from dataclasses import asdict
from pathlib import Path
from typing import Any

from agentplatform.domain.intelligence import (
    ProjectEvolution,
)


class EvolutionRepository:
    """
    Persistent storage for project evolution history.

    Storage belongs to target project.
    """

    FILE_NAME = "evolution_history.json"

    def append(
        self,
        project_path: Path,
        evolution: ProjectEvolution,
    ) -> None:
        """
        Append new evolution record.
        """

        directory = project_path / ".shadbot" / "intelligence"

        directory.mkdir(
            parents=True,
            exist_ok=True,
        )

        file_path = directory / self.FILE_NAME

        history = []

        if file_path.exists():
            with file_path.open(
                "r",
                encoding="utf-8",
            ) as file:
                history = json.load(
                    file,
                )

        history.append(
            self._serialize(
                evolution,
            )
        )

        with file_path.open(
            "w",
            encoding="utf-8",
        ) as file:
            json.dump(
                history,
                file,
                indent=4,
                ensure_ascii=False,
            )

    def load(
        self,
        project_path: Path,
    ) -> list[dict[str, Any]]:
        """
        Load evolution history.
        """

        file_path = project_path / ".shadbot" / "intelligence" / self.FILE_NAME

        if not file_path.exists():
            return []

        with file_path.open(
            "r",
            encoding="utf-8",
        ) as file:
            return json.load(
                file,
            )

    @staticmethod
    def _serialize(
        evolution: ProjectEvolution,
    ) -> dict[str, object]:
        """
        Convert evolution object to JSON.
        """

        return EvolutionRepository._convert(
            asdict(
                evolution,
            )
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
                str(key): EvolutionRepository._convert(
                    item,
                )
                for key, item in value.items()
            }

        if isinstance(
            value,
            tuple,
        ):
            return [
                EvolutionRepository._convert(
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
