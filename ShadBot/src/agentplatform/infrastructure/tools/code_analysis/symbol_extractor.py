"""
ShadBot Agent Platform

Symbol Extractor
"""

import ast


class SymbolExtractor:
    """
    Extracts classes and functions.
    """

    def extract(
        self,
        source: str,
    ) -> dict[str, list[str]]:

        tree = ast.parse(
            source,
        )

        classes = []
        functions = []

        for node in tree.body:

            if isinstance(
                node,
                ast.ClassDef,
            ):
                classes.append(node.name)

            if isinstance(
                node,
                ast.FunctionDef,
            ):
                functions.append(node.name)

        return {
            "classes": classes,
            "functions": functions,
        }
