# setup.py command | New command
# setup.py sdist   | python - m build
# setup.py test	   | pytest
# setup.py install | pip install
# setup.py develop | pip install - e
from Cython.Build import cythonize
from setuptools import Extension
from setuptools import setup


CYTHON_EXTENSIONS = [
    Extension(
        name="fastvector.cython_computations",
        sources=["fastvector/cython_computations.pyx"]
    )
]

EXT_MODULES = cythonize(CYTHON_EXTENSIONS, language_level="3")

with open("requirements.txt") as fp:
    install_requires = fp.read().strip().split("\n")

metadata = dict(
    install_requires=install_requires,
    ext_modules=EXT_MODULES,
)


def setup_package() -> None:
    setup(**metadata)


if __name__ == "__main__":
    setup_package()
