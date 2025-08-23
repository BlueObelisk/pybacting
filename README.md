# pybacting

[![Tests](https://github.com/BlueObelisk/pybacting/actions/workflows/tests.yml/badge.svg)](https://github.com/BlueObelisk/pybacting/actions/workflows/tests.yml)
[![PyPI](https://img.shields.io/pypi/v/pybacting)](https://pypi.org/project/pybacting/)
![PyPI - License](https://img.shields.io/pypi/l/pybacting)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/pybacting)
[![Documentation Status](https://readthedocs.org/projects/pybacting/badge/?version=latest)](https://pybacting.readthedocs.io/en/latest/?badge=latest)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![DOI](https://zenodo.org/badge/390711946.svg)](https://zenodo.org/badge/latestdoi/390711946)

Python wrapper around [Bacting](https://github.com/egonw/bacting).

## Usage

Based on the example from the Bacting page, you can do:

```python
from pybacting import cdk

print(cdk.fromSMILES("COC"))
```

Or you can use some of the more pythonic functions that wrap the functions
exposed through the `pybacting.cdk` object:

```python
import pybacting

print(pybacting.from_smiles("COC"))
```

## Installation

Before installing, you'll need to make sure Maven (`mvn`) and Java 17 are available on your
path. If you're on mac, use `brew install maven`.

```shell
$ pip install pybacting
```

Install the latest code from GitHub:

```shell
$ pip install git+https://github.com/BlueObelisk/pybacting
```

Download and install from source in development mode:

```shell
$ git clone https://github.com/BlueObelisk/pybacting
$ cd pybacting
$ pip install --editable .
```
