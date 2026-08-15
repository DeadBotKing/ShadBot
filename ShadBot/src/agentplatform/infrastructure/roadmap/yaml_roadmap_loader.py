"""
ShadBot Agent Platform

YAML roadmap loader.
"""

from __future__ import annotations

from pathlib import Path

import yaml

from agentplatform.application.roadmap.roadmap_parser import (
    ProjectPhase,
)


class YamlRoadmapLoader:
    """
    Loads project roadmap definitions.
    """

    def load(
        self,
        project_path: Path,
    ) -> list[ProjectPhase]:
        """
        Load roadmap.yaml from project.
        """

        roadmap_file = project_path / "roadmap.yaml"

        if not roadmap_file.exists():
            return []

        with roadmap_file.open(
            "r",
            encoding="utf-8",
        ) as file:
            data = yaml.safe_load(file)

        if not isinstance(data, dict):
            return []

        raw_phases = data.get(
            "phases",
            [],
        )

        if not isinstance(
            raw_phases,
            list,
        ):
            return []

        phases: list[ProjectPhase] = []

        for item in raw_phases:
            if not isinstance(
                item,
                dict,
            ):
                continue

            phases.append(
                ProjectPhase(
                    id=str(item.get("id", "")),
                    name=str(item.get("name", "")),
                    status=str(item.get("status", "pending")),
                )
            )

        return phases
