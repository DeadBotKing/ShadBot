"""
ShadBot Agent Platform

Code extraction tool.
"""

from __future__ import annotations

import re


class CodeExtractor:
    """
    Extracts source code from LLM responses.
    """

    def extract(
        self,
        response: str,
    ) -> str:
        """
        Extract code blocks from response.
        """

        matches = re.findall(
            r"```(?:python)?\s*(.*?)```",
            response,
            re.DOTALL,
        )

        if matches:
            return str(matches[0]).strip()

        return response.strip()
