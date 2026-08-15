"""
ShadBot Project Intelligence

Framework Signature Matcher
"""

from __future__ import annotations

from pathlib import Path

from projectintelligence.application.framework.framework_registry import (
    FrameworkSignature,
)


class SignatureMatcher:
    """
    Matches framework signatures against project files.
    """

    def matches(
        self,
        signature: FrameworkSignature,
        files: list[Path],
    ) -> bool:
        """
        Determine whether a framework signature matches
        the project files.
        """

        file_names = {file.name for file in files}

        # Required files
        for required_file in signature.required_files:
            if "*" in required_file:
                suffix = required_file.replace("*", "")

                if not any(file.name.endswith(suffix) for file in files):
                    return False

            elif required_file not in file_names:
                return False

        # Import/dependency matching will be implemented
        # in future phases.
        return True
