"""
ShadBot Agent Platform

Code Template Engine
"""

from __future__ import annotations


class CodeTemplateEngine:
    """
    Generates code templates based on context.
    """

    def render(
        self,
        *,
        template: str,
        variables: dict[str, object],
    ) -> str:
        """
        Render template.
        """

        return template.format(
            **variables,
        )
