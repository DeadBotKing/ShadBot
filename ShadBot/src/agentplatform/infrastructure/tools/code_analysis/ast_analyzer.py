"""
ShadBot Agent Platform

AST Analyzer
"""

import ast


class ASTAnalyzer:
    """
    Provides AST information.
    """

    def analyze(
        self,
        source: str,
    ) -> dict[str, int]:

        tree = ast.parse(
            source,
        )

        result = {
            "nodes": 0,
            "functions": 0,
            "classes": 0,
        }

        for node in ast.walk(tree):

            result["nodes"] += 1

            if isinstance(
                node,
                ast.FunctionDef,
            ):
                result["functions"] += 1

            if isinstance(
                node,
                ast.ClassDef,
            ):
                result["classes"] += 1

        return result
