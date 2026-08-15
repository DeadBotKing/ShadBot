"""
ShadBot Agent Platform

Code Generation Context
"""

from __future__ import annotations

from dataclasses import dataclass
from uuid import UUID


@dataclass(frozen=True, slots=True)
class CodeGenerationContext:
    """
    Context required for code generation.
    """

    project_id: UUID

    target_path: str

    language: str

    framework: str | None

    requirements: str

    existing_context: dict[str, object]
