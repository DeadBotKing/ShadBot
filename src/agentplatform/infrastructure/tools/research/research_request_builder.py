"""
ShadBot Agent Platform

Research Request Builder
"""

from __future__ import annotations

from .research_operation import (
    ResearchOperation,
)


class ResearchRequestBuilder:
    """
    Builds research execution requests.
    """

    def build(
        self,
        *,
        operation: ResearchOperation,
        query: str,
        sources: tuple[str, ...] = (),
    ) -> dict[str, object]:

        return {
            "operation": operation.value,
            "query": query,
            "sources": sources,
        }
