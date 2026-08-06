"""
ShadBot Agent Platform

File Metadata Tool
"""

from pathlib import Path


class FileMetadataReader:
    """
    Reads file metadata.
    """

    def read(
        self,
        path: str,
    ) -> dict[str, object]:

        file = Path(path)

        stat = file.stat()

        return {
            "name": file.name,
            "size": stat.st_size,
            "modified": stat.st_mtime,
            "suffix": file.suffix,
        }
