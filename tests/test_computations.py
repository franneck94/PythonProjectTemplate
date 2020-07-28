"""Test vectorND computations code.
"""
import unittest

from fastvector import VectorND
from fastvector.computations import (cython_clip_vector,
                                     naive_cython_clip_vector,
                                     python_clip_vector)


class ComputationsTests(unittest.TestCase):
    def setUp(self):
        self.v1 = VectorND(2.5, -2.5)
        self.v2 = VectorND(1, -1)

    def test_python_clip_vector(self):
        result = VectorND(0, 0)
        python_clip_vector(self.v1, -1, 1, result)
        expected_result = self.v2
        self.assertEqual(result, expected_result)
        self.assertRaises(ValueError, python_clip_vector, self.v1, 1, -1, result)

    def test_naive_cython_clip_vector(self):
        result = VectorND(0, 0)
        naive_cython_clip_vector(self.v1, -1, 1, result)
        expected_result = self.v2
        self.assertEqual(result, expected_result)
        self.assertRaises(ValueError, naive_cython_clip_vector, self.v1, 1, -1, result)

    def test_cython_clip_vector(self):
        result = VectorND(0, 0)
        cython_clip_vector(self.v1, -1, 1, result)
        expected_result = self.v2
        self.assertEqual(result, expected_result)
        self.assertRaises(ValueError, cython_clip_vector, self.v1, 1, -1, result)
   
if __name__ == '__main__':
    unittest.main()
