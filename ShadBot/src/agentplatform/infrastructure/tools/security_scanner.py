"""
ShadBot Agent Platform

Security scanner tool.
"""

from __future__ import annotations

from pathlib import Path


class SecurityScanner:
    """
    Performs static security checks.
    """

    def scan(
        self,
        path: Path,
    ) -> dict[str, object]:
        """
        Scan project for basic security issues.
        """

        issues: list[str] = []

        suspicious_patterns = [
            "password=",
            "secret=",
            "api_key=",
            "private_key=",
        ]

        for file_path in path.rglob("*.py"):
            try:
                content = file_path.read_text(
                    encoding="utf-8",
                )
            except UnicodeDecodeError:
                continue

            lowered = content.lower()

            for pattern in suspicious_patterns:
                if pattern in lowered:
                    issues.append(
                        f"{file_path}: contains {pattern}",
                    )

        return {
            "status": "PASS" if not issues else "FAIL",
            "issues": issues,
        }
