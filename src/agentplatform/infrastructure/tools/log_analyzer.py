"""
ShadBot Agent Platform

Log analyzer tool.
"""

from __future__ import annotations

from pathlib import Path


class LogAnalyzer:
    """
    Analyzes agent platform logs.
    """

    def analyze_file(
        self,
        path: Path,
    ) -> dict[str, object]:
        """
        Analyze a log file.
        """

        if not path.exists():
            return {
                "status": "missing",
                "errors": [],
                "warnings": [],
            }

        content = path.read_text(
            encoding="utf-8",
            errors="ignore",
        )

        lines = content.splitlines()

        errors = [line for line in lines if "ERROR" in line.upper()]

        warnings = [line for line in lines if "WARNING" in line.upper()]

        return {
            "status": "analyzed",
            "total_lines": len(lines),
            "errors": errors,
            "warnings": warnings,
        }

    def analyze_directory(
        self,
        path: Path,
    ) -> dict[str, object]:
        """
        Analyze all log files in directory.
        """

        results: dict[str, object] = {}

        for file in path.rglob("*.log"):
            results[str(file)] = self.analyze_file(
                file,
            )

        return results
