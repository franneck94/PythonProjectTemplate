# setup.py install | pip install .
# setup.py develop | pip install -e .
from setuptools import setup


def main() -> None:
    with open("requirements.txt") as fp:
        install_requires = fp.read().strip().split("\n")

    metadata = dict(install_requires=install_requires)
    setup(**metadata)


if __name__ == "__main__":
    main()
