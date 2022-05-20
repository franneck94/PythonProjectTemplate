# FastVector

![Python](https://img.shields.io/badge/python-3.7+-blue)
![License](https://camo.githubusercontent.com/890acbdcb87868b382af9a4b1fac507b9659d9bf/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f6c6963656e73652d4d49542d626c75652e737667)
[![Build](https://github.com/franneck94/Python-Project-Template/workflows/ci-test/badge.svg)](https://github.com/franneck94/Python-Project-Template/actions?query=workflow%3Aci-test)
[![codecov](https://codecov.io/gh/franneck94/python-project-template/branch/master/graph/badge.svg)](https://codecov.io/gh/franneck94/python-project-template)
[![Documentation](https://img.shields.io/badge/ref-Documentation-blue)](https://franneck94.github.io/Python-Project-Template/)

## Template For Python Projects

This is a template for Python projects. What you get:

- Source code and test code is seperated in different directories.
- External libraries installed and managed by [Pip](https://pypi.org/project/pip/).
- Setup for tests using [Pytest](https://docs.pytest.org/en/stable/).
- Bechmark tests using [Pytest-Benchmark](https://github.com/ionelmc/pytest-benchmark)
- Continuous testing with [Github-Actions](https://github.com/features/actions/).
- Code coverage reports, including automatic upload to [Codecov](https://codecov.io).
- Code documentation with [Mkdocs](https://www.mkdocs.org/).
- Example of own Python package with the use of [Cython](https://cython.org/)
- Optional: Use of [VSCode](https://code.visualstudio.com/) with the Python and UnitTest extension.

## Structure

``` text
├── setup.py
├── setup.cfg
├── pyproject.toml
├── ... other config files ...
├── tests
│   ├── __init__.py
│   ├── test_vector.py
│   ├── test_computations.py
│   └── conftest.py
├── docs
│   ├── api.md
│   └── index.md
├── fastvector
│   ├── __init__.py
│   ├── vector.py
│   ├── dtypes.py
│   ├── version.py
│   └── cython_computations.pyx
│   └── computations.py
└── benchmarks
│   ├── __init__.py
│   └── test_computations.py
└── tests
    ├── __init__.py
    ├── test_computations.py
    └── test_vector.py
```

### Commands

```bash
# Build and Install (local)
pip install -e .
```

```bash
# Test
pytest tests
```

```bash
# Code Coverage
pytest --cov=fastvector tests --cov-report=html
```

```bash
# Benchmarks
pytest --benchmark-columns=min,max,mean,stddev --benchmark-sort=mean benchmarks
```
