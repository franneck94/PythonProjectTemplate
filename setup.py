# Version 1: python setup.py install <=> pip install .
# Version 2: python setup.py develop <=> pip install -e .
from Cython.Build import cythonize
from setuptools import Extension
from setuptools import setup


CLASSIFIERS = """\
License :: OSI Approved
Programming Language :: Python :: 3
Topic :: Software Development
Operating System :: Microsoft :: Windows
Operating System :: POSIX
Operating System :: Unix
Operating System :: MacOS
"""

DISTNAME = "fastvector"
AUTHOR = "Jan Schaffranek"
AUTHOR_EMAIL = "jan.schaffranek@email.com"
DESCRIPTION = "This is a simple vector python package."
LICENSE = "MIT"
README = "This is a simple vector python package."

VERSION = "0.1.0"
ISRELEASED = False

PYTHON_MIN_VERSION = "3.7"
PYTHON_REQUIRES = f">={PYTHON_MIN_VERSION}"

INSTALL_REQUIRES = ["numpy", "scipy", "Cython"]

PACKAGES = ["fastvector", "tests"]

CYTHON_EXTENSIONS = [
    Extension(
        name="fastvector.cython_computations",
        sources=["fastvector/cython_computations.pyx"]
    )
]

EXT_MODULES = cythonize(CYTHON_EXTENSIONS, language_level="3")

metadata = dict(
    name=DISTNAME,
    version=VERSION,
    long_description=README,
    packages=PACKAGES,
    python_requires=PYTHON_REQUIRES,
    install_requires=INSTALL_REQUIRES,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    description=DESCRIPTION,
    classifiers=[CLASSIFIERS],
    license=LICENSE,
    ext_modules=EXT_MODULES,
)


def setup_package() -> None:
    setup(**metadata)


if __name__ == "__main__":
    setup_package()
