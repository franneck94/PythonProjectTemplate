# FastVector

![Python](https://img.shields.io/badge/python-3.9+-blue)
![License](https://camo.githubusercontent.com/890acbdcb87868b382af9a4b1fac507b9659d9bf/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f6c6963656e73652d4d49542d626c75652e737667)
[![Build](https://github.com/franneck94/Python-Project-Template/actions/workflows/test.yml/badge.svg?branch=master)](https://github.com/franneck94/Python-Project-Template/actions/workflows/test.yml)
[![codecov](https://codecov.io/gh/franneck94/Python-Project-Template-Eng/branch/master/graph/badge.svg)](https://codecov.io/gh/franneck94/Python-Project-Template-Eng)
[![Documentation](https://img.shields.io/badge/ref-Documentation-blue)](https://franneck94.github.io/Python-Project-Template-Eng/)

## Template For Python Projects

This is a template for Python projects. What you get:

- Source code and test code is seperated in different directories.
- External libraries installed and managed by [Pip](https://pypi.org/project/pip/) and [setuptools](https://setuptools.pypa.io/en/latest/) in a pyproject.toml.
- Setup for tests using [Pytest](https://docs.pytest.org/en/stable/) and coverage with [Pytest-Cov](https://github.com/pytest-dev/pytest-cov).
- Continuous testing with [Github-Actions](https://github.com/features/actions/) including [pre-commit](https://github.com/pre-commit/pre-commit).
- Code coverage reports, including automatic upload to [Codecov](https://codecov.io).
- Code documentation with [Mkdocs](https://www.mkdocs.org/).

## Structure

``` text
├── pyproject.toml
├── ... other config files ...
├── docs
│   ├── api.md
│   └── index.md
├── examples
│   └── ...
├── fastvector
│   ├── __init__.py
│   ├── vector.py
│   └── version.py
└── tests
    ├── __init__.py
    └── test_vector.py
```

### Commands

```bash
# Build and Install (local)
pip install -e .  # OR
pip install -e ../Python-Project-Template  # OR
pip install -e ../Python-Project-Template[all]
```

```bash
# Test
pytest tests  # OR
pytest .  # OR
pytest
```

```bash
# Code Coverage
pytest --cov=fastvector tests --cov-report=html
```
