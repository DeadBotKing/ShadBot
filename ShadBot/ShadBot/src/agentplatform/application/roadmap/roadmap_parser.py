"""
ShadBot Agent Platform

Roadmap parser.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class ProjectPhase:
    """
    Project execution phase.
    """

    id: str

    name: str

    status: str


class RoadmapParser:
    """
    Converts roadmap data into domain objects.
    """

    def parse(
        self,
        data: dict[str, object],
    ) -> list[ProjectPhase]:
        """
        Parse roadmap phases.
        """

        phases = data.get(
            "phases",
            [],
        )

        if not isinstance(
            phases,
            list,
        ):
            return []

        result: list[ProjectPhase] = []

        for phase in phases:
            if not isinstance(
                phase,
                dict,
            ):
                continue

            result.append(
                ProjectPhase(
                    id=str(
                        phase.get(
                            "id",
                            "",
                        )
                    ),
                    name=str(
                        phase.get(
                            "name",
                            "",
                        )
                    ),
                    status=str(
                        phase.get(
                            "status",
                            "",
                        )
                    ),
                )
            )

        return result
