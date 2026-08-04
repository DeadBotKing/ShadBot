"""
ShadBot Agent Platform

Project analyzer tool implementation.
"""

from __future__ import annotations

from pathlib import Path


class ProjectAnalyzerTool:
    """
    Handles project intelligence analysis operations.
    """

    def analyze(
        self,
        path: str,
    ) -> dict[str, object]:
        project_path = Path(path)

        if not project_path.exists():
            raise ValueError(
                f"Project path does not exist: {path}",
            )

        files = [
            str(file.relative_to(project_path))
            for file in project_path.rglob("*")
            if file.is_file()
        ]

        directories = [
            str(directory.relative_to(project_path))
            for directory in project_path.rglob("*")
            if directory.is_dir()
        ]

        return {
            "project_path": str(project_path),
            "files": files,
            "directories": directories,
            "file_count": len(files),
            "directory_count": len(directories),
        }
