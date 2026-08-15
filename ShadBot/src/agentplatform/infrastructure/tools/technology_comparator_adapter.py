"""
ShadBot Agent Platform

Technology comparator adapter.
"""

from __future__ import annotations

from agentplatform.domain.tools import (
    ToolContract,
    ToolType,
)

from .technology_comparator import TechnologyComparator


class TechnologyComparatorAdapter(ToolContract):
    """
    Adapter for technology comparison.
    """

    def __init__(self) -> None:
        self._tool = TechnologyComparator()

    @property
    def tool_type(self) -> ToolType:
        return ToolType.TECHNOLOGY_COMPARISON

    def execute(
        self,
        payload: dict[str, object],
    ) -> dict[str, object]:

        criteria = payload.get(
            "criteria",
            [],
        )

        if not isinstance(
            criteria,
            list,
        ):
            criteria = []

        return self._tool.execute(
            str(
                payload.get(
                    "option_a",
                    "",
                ),
            ),
            str(
                payload.get(
                    "option_b",
                    "",
                ),
            ),
            criteria,
        )
