"""
ShadBot Agent Platform

Complexity Analyzer
"""

import ast


class ComplexityAnalyzer:
    """
    Calculates basic cyclomatic complexity.
    """

    def calculate(
        self,
        source: str,
    ) -> int:

        tree = ast.parse(
            source,
        )

        complexity = 1

        for node in ast.walk(tree):

            if isinstance(
                node,
                (
                    ast.If,
                    ast.For,
                    ast.While,
                    ast.Try,
                    ast.With,
                ),
            ):
                complexity += 1

        return complexity
