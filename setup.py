from Cython.Build import cythonize  # pylint: disable=E0401
from setuptools import Extension
from setuptools import setup

from fastvector import __version__


def get_readme() -> str:
    with open("README.md") as f:
        return f.read()


def get_license() -> str:
    with open("LICENSE") as f:
        return f.read()


CLASSIFIERS = """\
License :: OSI Approved
Programming Language :: Python :: 3.7 :: 3.8
Topic :: Software Development
Operating System :: Microsoft :: Windows
Operating System :: POSIX
Operating System :: Unix
Operating System :: MacOS
"""

DISTNAME = "fastvector"
AUTHOR = "Jan Schaffranek"
AUTHOR_EMAIL = "jan.schaffranek@email.com"
DESCRIPTION = "This is a simple vector package."
LICENSE = get_license()
README = get_readme()

VERSION = __version__
ISRELEASED = True

PYTHON_MIN_VERSION = "3.7"
PYTHON_MAX_VERSION = "3.8"
SCIPY_VERSION = "1.5.0"
NUMPY_VERSION = "1.18.5"
CYTHON_VERSION = "0.29.21"

INSTALL_REQUIRES = [
    "numpy=={}".format(NUMPY_VERSION),
    "scipy=={}".format(SCIPY_VERSION),
    "Cython=={}".format(CYTHON_VERSION),
]

CYTHON_EXTENSION = [
    Extension(
        name="fastvector.cython_computations",
        sources=["fastvector/cython_computations.pyx"],
    ),
]

metadata = dict(
    name=DISTNAME,
    version=VERSION,
    long_description=README,
    packages=["fastvector", "tests"],
    ext_modules=cythonize(CYTHON_EXTENSION, language_level="3"),
    python_requires=">={}, <={}".format(
        PYTHON_MIN_VERSION, PYTHON_MAX_VERSION),
    install_requires=INSTALL_REQUIRES,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    description=DESCRIPTION,
    classifiers=[CLASSIFIERS],
    license=LICENSE,
)


def setup_package() -> None:
    setup(**metadata)


if __name__ == "__main__":
    setup_package()
