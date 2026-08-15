"""
ShadBot Agent Platform

Source Analyzer Tool
"""

from __future__ import annotations

from pathlib import Path


class SourceAnalyzer:
    """
    Reads and analyzes source files.
    """

    def analyze(
        self,
        path: str,
    ) -> dict[str, object]:

        file = Path(path)

        if not file.exists():
            raise FileNotFoundError(path)

        content = file.read_text(
            encoding="utf-8",
        )

        return {
            "path": str(file),
            "lines": len(content.splitlines()),
            "characters": len(content),
            "extension": file.suffix,
        }
