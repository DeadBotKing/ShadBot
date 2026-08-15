"""
ShadBot Project Intelligence

Language Extension Registry
"""

from __future__ import annotations

from pathlib import Path


class ExtensionRegistry:
    """
    Maps file extensions to programming languages.
    """

    _EXTENSIONS: dict[str, str] = {
        ".py": "Python",
        ".pyi": "Python",
        ".ipynb": "Jupyter Notebook",
        ".js": "JavaScript",
        ".mjs": "JavaScript",
        ".cjs": "JavaScript",
        ".ts": "TypeScript",
        ".tsx": "TypeScript",
        ".jsx": "JavaScript",
        ".java": "Java",
        ".kt": "Kotlin",
        ".kts": "Kotlin",
        ".cs": "C#",
        ".cpp": "C++",
        ".cc": "C++",
        ".cxx": "C++",
        ".hpp": "C++",
        ".hh": "C++",
        ".c": "C",
        ".h": "C",
        ".go": "Go",
        ".rs": "Rust",
        ".swift": "Swift",
        ".php": "PHP",
        ".rb": "Ruby",
        ".html": "HTML",
        ".htm": "HTML",
        ".css": "CSS",
        ".scss": "SCSS",
        ".sass": "SASS",
        ".json": "JSON",
        ".yaml": "YAML",
        ".yml": "YAML",
        ".toml": "TOML",
        ".xml": "XML",
        ".sql": "SQL",
        ".md": "Markdown",
        ".rst": "reStructuredText",
        ".sh": "Shell",
        ".ps1": "PowerShell",
        ".dockerfile": "Dockerfile",
    }

    def detect(
        self,
        file_path: Path,
    ) -> str | None:
        """
        Detect the language for a single file.
        """

        if file_path.name.lower() == "dockerfile":
            return "Dockerfile"

        return self._EXTENSIONS.get(file_path.suffix.lower())
