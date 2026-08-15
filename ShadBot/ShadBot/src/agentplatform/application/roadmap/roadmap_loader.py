"""
ShadBot Agent Platform

Roadmap loader.
"""

from __future__ import annotations

from pathlib import Path

import yaml


class RoadmapLoader:
    """
    Loads project roadmap files.
    """

    def load(
        self,
        project_path: Path,
    ) -> dict[str, object]:
        """
        Load roadmap.yaml from project.
        """

        roadmap_file = project_path / "tasks" / "roadmap.yaml"

        if not roadmap_file.exists():
            return {}

        with roadmap_file.open(
            "r",
            encoding="utf-8",
        ) as file:
            data = yaml.safe_load(file)

        if not isinstance(
            data,
            dict,
        ):
            return {}

        return data
