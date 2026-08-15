"""
ShadBot Agent Platform

Quality validator adapter.
"""

from __future__ import annotations

from pathlib import Path

from agentplatform.domain.tools import (
    ToolContract,
    ToolType,
)

from .quality_validator import QualityValidator


class QualityValidatorAdapter(ToolContract):
    """
    Exposes quality validation as agent tool.
    """

    def __init__(self) -> None:
        self._validator = QualityValidator()

    @property
    def tool_type(self) -> ToolType:
        return ToolType.QUALITY_VALIDATOR

    def execute(
        self,
        payload: dict[str, object],
    ) -> dict[str, object]:

        return self._validator.validate(
            Path(
                str(payload.get("path", ".")),
            ),
        )
