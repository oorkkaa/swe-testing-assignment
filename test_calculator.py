import unittest
from calculator_logic import add, subtract, multiply, divide

class TestCalculator(unittest.TestCase):

    #4 operations
    def test_add(self):
        self.assertEqual(add(2, 3), 5)

    def test_subtract(self):
        self.assertEqual(subtract(10, 5), 5)

    def test_multiply(self):
        self.assertEqual(multiply(3, 4), 12)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5.0)

    #4 edge cases
    def test_edge_div_by_zero(self):
        self.assertEqual(divide(5, 0), "Error: Division by zero")

    def test_edge_negative_numbers(self):
        self.assertEqual(add(-5, -5), -10)

    def test_edge_decimals(self):
        self.assertAlmostEqual(add(0.1, 0.2), 0.3, places=7)

    def test_edge_large_numbers(self):
        self.assertEqual(multiply(1000000, 1000000), 1000000000000)

if __name__ == '__main__':
    unittest.main()