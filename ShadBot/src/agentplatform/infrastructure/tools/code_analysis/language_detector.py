"""
ShadBot Agent Platform

Code Language Detector
"""

from pathlib import Path


class LanguageDetector:
    """
    Detects programming language.
    """

    EXTENSIONS = {
        ".py": "python",
        ".js": "javascript",
        ".ts": "typescript",
        ".java": "java",
        ".cs": "csharp",
        ".cpp": "cpp",
        ".go": "go",
    }

    def detect(
        self,
        path: str,
    ) -> str:

        suffix = Path(path).suffix.lower()

        return self.EXTENSIONS.get(
            suffix,
            "unknown",
        )
