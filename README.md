![Python](https://img.shields.io/badge/python-3.5%20%7C%203.6%20%7C%203.7-blue)
![License](https://camo.githubusercontent.com/890acbdcb87868b382af9a4b1fac507b9659d9bf/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f6c6963656e73652d4d49542d626c75652e737667)
<!-- [![Release](https://img.shields.io/github/v/release/franneck94/cpp-project-template)](https://travis-ci.org/github/franneck94/Cpp-Project-Template)
[![Project Status: Active.](http://www.repostatus.org/badges/latest/active.svg)](http://www.repostatus.org/#active)
[![Travis CI](https://api.travis-ci.org/franneck94/Cpp-Project-Template.svg?branch=master)](https://travis-ci.org/github/franneck94/Cpp-Project-Template)
[![codecov](https://codecov.io/gh/franneck94/Cpp-Project-Template/branch/master/graph/badge.svg)](https://codecov.io/gh/franneck94/Cpp-Project-Template) -->

# Template For Python Projects 

This is a template for Python projects. What you get:

-   External libraries installed and managed by [Pip](https://pypi.org/project/pip/) or [Conda](https://anaconda.com/)
-   Setup for tests using [Pytest](https://docs.pytest.org/en/stable/)
-   Continuous testing with [Travis-CI](https://travis-ci.org/)
-   Code coverage reports, including automatic upload to [Codecov](https://codecov.io)
-   Code documentation with [Sphinx](https://www.sphinx-doc.org/en/master/)
-   Optional: Use of the [VSCode](https://code.visualstudio.com/) IDE with useful extensions, like the Python and UnitTest extensions

## Structure
``` text
├── setup.py
└── documentation
├── fastvector
│   └── __init__.py
│   └── vector.py
└── tests
    ├── test_vector.py
```

Sources of the package go in [fastvector/](fastvector/) and 
tests go in [tests/](tests/).
