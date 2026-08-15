"""
ShadBot Project Intelligence

Language Statistics
"""

from __future__ import annotations

from collections import Counter


class LanguageStatistics:
    """
    Collects language statistics from detected languages.
    """

    def collect(
        self,
        languages: list[str | None],
    ) -> dict[str, int]:
        """
        Count occurrences of each detected language.
        """

        counter = Counter(language for language in languages if language is not None)

        return dict(counter)

    def unique_languages(
        self,
        statistics: dict[str, int],
    ) -> list[str]:
        """
        Return detected languages sorted by frequency.
        """

        return [
            language
            for language, _ in sorted(
                statistics.items(),
                key=lambda item: item[1],
                reverse=True,
            )
        ]
