"""Test vectorND code.
"""
import math
import unittest

from fastvector import VectorND


class VectorTests(unittest.TestCase):
    def setUp(self):
        self.v1 = VectorND(0, 0)
        self.v2 = VectorND(-1, 1)
        self.v3 = VectorND(2.5, -2.5)

    def test_init(self):
        result = VectorND([-1, 1])
        self.assertEqual(result, self.v2)
        self.assertRaises(TypeError, VectorND, 0, "a")
        self.assertRaises(TypeError, VectorND, "B", 1)
        self.assertRaises(TypeError, VectorND, "B", 1)
        self.assertRaises(TypeError, VectorND)
    
    def test_comparison(self):
        # Test equality
        self.assertNotEqual(self.v1, self.v2)
        expected_result = VectorND(-1, 1)
        self.assertEqual(self.v2, expected_result)
        # Test less
        result = self.v1 + self.v2
        self.assertLess(result, self.v3)
        # Test greater
        self.assertGreater(self.v3, result)

    def test_call(self):
        result = self.v1()
        expected_result = repr(self.v1)
        self.assertEqual(result, expected_result)
    
    def test_abs(self):
        result = abs(self.v2)
        expected_result = math.sqrt(2.0)
        self.assertAlmostEqual(result, expected_result)

    def test_str(self):
        result = str(self.v1)
        expected_result = '(array(\'d\', [0.0, 0.0]))'
        self.assertEqual(result, expected_result)

    def test_len(self):
        result = VectorND([3, 4])
        self.assertEqual(len(result), len(self.v1))
    
    def test_item_get_set(self):
        result = VectorND([1, 2, 3])
        result[0] = -1
        expected_result = VectorND([-1, 2, 3])
        self.assertEqual(result, expected_result)
        self.assertEqual(result[0], expected_result[0])
        self.assertRaises(IndexError, VectorND.__getitem__, result, -1)
        self.assertRaises(IndexError, VectorND.__setitem__, result, -1, 1337)
    
    def test_bool(self):
        result = bool(self.v1)
        expected_result = False
        self.assertEqual(result, expected_result)
        result = bool(self.v2)
        expected_result = True
        self.assertEqual(result, expected_result)
    
    def test_add(self):
        result = self.v1 + self.v2
        expected_result = VectorND(-1, 1)
        self.assertEqual(result, expected_result)

    def test_sub(self):
        result = self.v2 - self.v3
        expected_result = VectorND(-3.5, 3.5)
        self.assertEqual(result, expected_result)

    def test_mul(self):
        # Valid multiplication
        result1 = self.v1 * 5
        expected_result1 = VectorND(0.0, 0.0)
        self.assertEqual(result1, expected_result1)
        result2 = self.v1 * self.v2
        expected_result2 = 0.0
        self.assertEqual(result2, expected_result2)
        # Invalid multiplication
        self.assertRaises(TypeError, self.v1.__mul__, "a")

    def test_div(self):
        # Valid division
        result = self.v3 / 5
        expected_result = VectorND(0.5, -0.5)
        self.assertEqual(result, expected_result)
        # Invalid division
        self.assertRaises(TypeError, self.v1.__truediv__, "a")
        self.assertRaises(ValueError, self.v1.__truediv__, 0)

    def test_check_numeric_argument(self):
        self.assertRaises(TypeError, VectorND.check_numeric_argument, "1337")

    def test_check_vector_types(self):
        self.assertRaises(TypeError, VectorND.check_vector_types, 1337)
        self.assertRaises(TypeError, VectorND.check_vector_types, 13.73)
        self.assertRaises(TypeError, VectorND.check_vector_types, "1337")


if __name__ == '__main__':
    unittest.main()
