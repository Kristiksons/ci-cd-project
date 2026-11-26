
import sys
import unittest
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
DEV_PATH = PROJECT_ROOT / "DEV" / "ci-cd-project"

sys.path.insert(0, str(DEV_PATH))

from calculator import add, subtract, multiply, divide


class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(5, 3), 8)

    def test_subtract(self):
        self.assertEqual(subtract(10, 4), 6)

    def test_multiply(self):
        self.assertEqual(multiply(4, 3), 12)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            divide(10, 0)

    def test_negative_numbers(self):
        self.assertEqual(add(-5, -3), -8)

    def test_decimal_numbers(self):
        self.assertAlmostEqual(multiply(2.5, 2), 5.0)


if __name__ == "__main__":
    unittest.main()
