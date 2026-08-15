"""
ShadBot Agent Platform

Import Analyzer
"""

import ast


class ImportAnalyzer:
    """
    Extracts imports from Python source.
    """

    def analyze(
        self,
        source: str,
    ) -> list[str]:

        tree = ast.parse(
            source,
        )

        imports: list[str] = []

        for node in ast.walk(tree):

            if isinstance(
                node,
                ast.Import,
            ):
                imports.extend(alias.name for alias in node.names)

            if isinstance(
                node,
                ast.ImportFrom,
            ):
                if node.module:
                    imports.append(node.module)

        return imports
