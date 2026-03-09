"""Trivial tests for :mod:`pybacting`."""

import unittest

from scyjava import to_python

import pybacting
from pybacting import qudt


class TestImport(unittest.TestCase):
    """Test importing :mod:`pybacting`."""

    def test_from_smiles(self) -> None:
        """Test loading via cdk."""
        mol = pybacting.from_smiles("COOC")
        self.assertIsNotNone(mol)

    def test_from_iupac(self) -> None:
        """Test loading via opsin."""
        mol = pybacting.from_iupac_name("benzene")
        self.assertIsNotNone(mol)

    def test_inchi(self) -> None:
        """Test getting InChI."""
        mol = pybacting.from_iupac_name("methane")
        self.assertEqual("InChI=1S/CH4/h1H4", pybacting.get_inchi(mol))
        self.assertEqual("VNWKTOKETHGBQD-UHFFFAOYSA-N", pybacting.get_inchi_key(mol))

    def test_qudt_manager_name(self) -> None:
        """Test getting the qudt manager name.

        .. seealso:: https://egonw.github.io/bacting-api/net/bioclipse/managers/QUDTManager.html
        """
        self.assertIsInstance(to_python(qudt.getManagerName()), str)
