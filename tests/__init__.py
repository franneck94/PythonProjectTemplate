'''Test code suite.
'''
import unittest

from .test_computations import ComputationsTests  # noqa: F401
from .test_vector import VectorTests  # noqa: F401


def main_tests() -> None:
    unittest.main()


if __name__ == '__main__':
    main_tests()
