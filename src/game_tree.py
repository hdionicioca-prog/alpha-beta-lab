"""Game tree examples for the Minimax and Alpha-Beta laboratory."""
from typing import TypeAlias

GameTree: TypeAlias = int | list["GameTree"]

def sample_tree() -> GameTree:
    """Árbol pequeño de prueba. Resultado esperado: 5."""
    return [
        [3, 5],
        [2, 9],
    ]

def medium_tree() -> GameTree:
    """Árbol mediano donde Alfa-Beta puede podar ramas. Resultado esperado: 6."""
    return [
        [[3, 5], [6, 9]],
        [[1, 2], [0, -1]],
        [[7, 4], [8, 6]],
    ]

def ordered_tree_for_pruning() -> GameTree:
    """Árbol ordenado favorablemente para maximizar las podas. Resultado esperado: 10."""
    return [
        [[10, 9], [8, 7]],
        [[6, 5], [4, 3]],
        [[2, 1], [0, -1]],
    ]