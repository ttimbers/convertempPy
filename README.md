## convertempPy 

![](https://github.com/ttimbers/convertempPy/workflows/build/badge.svg) [![codecov](https://codecov.io/gh/ttimbers/convertempPy/branch/master/graph/badge.svg)](https://codecov.io/gh/ttimbers/convertempPy) ![Release](https://github.com/ttimbers/convertempPy/workflows/Release/badge.svg)

[![Documentation Status](https://readthedocs.org/projects/convertemppy/badge/?version=latest)](https://convertemppy.readthedocs.io/en/latest/?badge=latest)

Easily convert between temperatures: Celsius, Kelvin & Fahrenheit! This is a toy package developed for demonstration in the [UBC MDS DSCI 524 (Collaborative Software Development) course](https://github.com/UBC-MDS/DSCI_524_collab-sw-dev). 

### Installation:

```
pip install -i https://test.pypi.org/simple/ convertempPy
```

### Features
Contains functions for all permutations of conversions between Celsius, Kelvin and Fahrenheit. This package is an example for the UBC MDS DSCI 524 (Collaborative Software Development) course.

### Dependencies

- Python 3 or greater

### Usage

Example usage:
```
>>> from convertempPy import convertempPy as tmp
>>> tmp.fahr_to_celsius(32)
```

```
0
```

### Documentation
The official documentation is hosted on Read the Docs: <https://convertempPy.readthedocs.io/en/latest/>

### Credits
This package was created with Cookiecutter and the UBC-MDS/cookiecutter-ubc-mds project template, modified from the [pyOpenSci/cookiecutter-pyopensci](https://github.com/pyOpenSci/cookiecutter-pyopensci) project template and the [audreyr/cookiecutter-pypackage](https://github.com/audreyr/cookiecutter-pypackage).
