"""
ShadBot Agent Platform

Documentation analyzer tool.
"""

from __future__ import annotations

from pathlib import Path


class DocumentationAnalyzer:
    """
    Analyze project documentation.
    """

    def execute(
        self,
        path: Path,
    ) -> dict[str, object]:
        """
        Analyze documentation files.
        """

        documents: list[str] = []

        for pattern in (
            "README*",
            "*.md",
            "*.rst",
        ):
            documents.extend(
                str(item) for item in path.rglob(pattern) if item.is_file()
            )

        return {
            "documents": documents,
            "count": len(documents),
            "missing": [],
        }
