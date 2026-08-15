"""
ShadBot Agent Platform

Tool Metadata Value Object
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass(frozen=True, slots=True)
class ToolMetadata:
    """
    Describes tool identity and execution information.
    """

    display_name: str

    category: str

    description: str

    version: str

    provider: str

    input_schema: dict[str, Any] = field(
        default_factory=dict,
    )

    output_schema: dict[str, Any] = field(
        default_factory=dict,
    )

    tags: tuple[str, ...] = ()

    constraints: dict[str, Any] = field(
        default_factory=dict,
    )
