"""Test code.
"""
import math
import unittest

from fastvector import Vector2D


class VectorTests(unittest.TestCase):
    def setUp(self):
        self.v1 = Vector2D(0, 0)
        self.v2 = Vector2D(-1, 1)
        self.v3 = Vector2D(2.5, -2.5)

    def test_init(self):
        """ Tests exceptions for the constructor
        """
        self.assertRaises(TypeError, Vector2D, 0, "a")
        self.assertRaises(TypeError, Vector2D, "B", 1)
    
    def test_comparison(self):
        """ Tests the comparison operators.
        """
        # Test equality
        self.assertNotEqual(self.v1, self.v2)
        expected_result = Vector2D(-1, 1)
        self.assertEqual(self.v2, expected_result)
        # Test less
        result = self.v1 + self.v2
        self.assertLess(result, self.v3)
        # Test greater
        self.assertGreater(self.v3, result)
    
    def test_abs(self):
        """ Tests the abs value.
        """
        result = abs(self.v2)
        expected_result = math.sqrt(2.0)
        self.assertAlmostEqual(result, expected_result)

    def test_str(self):
        """ Tests the abs value.
        """
        result = str(self.v1)
        expected_result = '(0, 0)'
        self.assertEqual(result, expected_result)

    def test_bool(self):
        """ Tests the abs value.
        """
        result = bool(self.v1)
        expected_result = False
        self.assertEqual(result, expected_result)
        result = bool(self.v2)
        expected_result = True
        self.assertEqual(result, expected_result)
    
    def test_add(self):
        """ Tests the addition operator.
        """
        result = self.v1 + self.v2
        expected_result = Vector2D(-1, 1)
        self.assertEqual(result, expected_result)

    def test_sub(self):
        """ Tests the subtraction operator.
        """
        result = self.v2 - self.v3
        expected_result = Vector2D(-3.5, 3.5)
        self.assertEqual(result, expected_result)

    def test_mul(self):
        """ Tests the multiplication operator.
        """
        # Valid multiplication
        result1 = self.v1 * 5
        expected_result1 = Vector2D(0.0, 0.0)
        self.assertEqual(result1, expected_result1)
        result2 = self.v1 * self.v2
        expected_result2 = 0.0
        self.assertEqual(result2, expected_result2)
        # Invalid multiplication
        self.assertRaises(TypeError, self.v1.__mul__, "a")

    def test_div(self):
        """ Tests the multiplication operator.
        """
        # Valid division
        result = self.v3 / 5
        expected_result = Vector2D(0.5, -0.5)
        self.assertEqual(result, expected_result)
        # Invalid division
        self.assertRaises(TypeError, self.v1.__truediv__, "a")
        self.assertRaises(ValueError, self.v1.__truediv__, 0)

    def test_check_vector_types(self):
        """ Tests the abs value.
        """
        self.assertRaises(TypeError, Vector2D.check_vector_types, 1337)
        self.assertRaises(TypeError, Vector2D.check_vector_types, 13.73)
        self.assertRaises(TypeError, Vector2D.check_vector_types, "1337")

if __name__ == "__main__":
    unittest.main()
