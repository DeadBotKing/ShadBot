"""
ShadBot Agent Platform

Code Generation Service
"""

from __future__ import annotations

from .code_generator_tool import (
    CodeGeneratorTool,
)


class CodeGenerationService:
    """
    Application service for code generation.
    """

    def __init__(
        self,
        generator: CodeGeneratorTool,
    ) -> None:

        self._generator = generator

    def generate(
        self,
        request: dict[str, object],
    ) -> dict[str, object]:

        return self._generator.execute(
            request,
        )
