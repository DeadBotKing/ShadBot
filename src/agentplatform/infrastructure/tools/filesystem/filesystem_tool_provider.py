"""
ShadBot Agent Platform

Filesystem Tool Provider
"""

from __future__ import annotations

from dataclasses import dataclass

from .directory_creator import DirectoryCreator
from .directory_reader import DirectoryReader
from .file_creator import FileCreator
from .file_deleter import FileDeleter
from .file_metadata import FileMetadataReader
from .file_reader import FileReader
from .file_search import FileSearch
from .file_writer import FileWriter


@dataclass(slots=True)
class FileSystemToolProvider:
    """
    Provides filesystem tools.
    """

    reader: FileReader
    writer: FileWriter
    creator: FileCreator
    deleter: FileDeleter

    directory_reader: DirectoryReader
    directory_creator: DirectoryCreator

    search: FileSearch
    metadata: FileMetadataReader

    @classmethod
    def create(cls) -> "FileSystemToolProvider":

        return cls(
            reader=FileReader(),
            writer=FileWriter(),
            creator=FileCreator(),
            deleter=FileDeleter(),
            directory_reader=DirectoryReader(),
            directory_creator=DirectoryCreator(),
            search=FileSearch(),
            metadata=FileMetadataReader(),
        )
