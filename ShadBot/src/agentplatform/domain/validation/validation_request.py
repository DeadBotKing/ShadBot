"""
ShadBot Agent Platform

Validation request contract.
"""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(frozen=True, slots=True)
class ValidationRequest:
    """
    Input contract for validation.
    """

    target: object

    metadata: dict[str, object] = field(
        default_factory=dict,
    )
