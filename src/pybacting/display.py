"""Display functions."""

from typing import TYPE_CHECKING

from .io import Molecule, get_svg

if TYPE_CHECKING:
    import IPython.display

__all__ = [
    "mol_to_svg",
]


def mol_to_svg(mol: Molecule) -> "IPython.display.SVG":
    """Display a molecule as SVG in a Jupyter notebook."""
    from IPython.display import SVG

    return SVG(get_svg(mol))
