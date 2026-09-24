import unittest

from bounds import clamp


class ClampRangeTest(unittest.TestCase):
    def test_below_range_returns_lower(self):
        self.assertEqual(clamp(-5, 0, 10), 0)

    def test_above_range_returns_upper(self):
        self.assertEqual(clamp(15, 0, 10), 10)

    def test_within_range_returns_value(self):
        self.assertEqual(clamp(5, 0, 10), 5)

    def test_exact_lower_boundary(self):
        self.assertEqual(clamp(0, 0, 10), 0)

    def test_exact_upper_boundary(self):
        self.assertEqual(clamp(10, 0, 10), 10)

    def test_floats(self):
        self.assertEqual(clamp(0.5, 0.0, 1.0), 0.5)
        self.assertEqual(clamp(-0.1, 0.0, 1.0), 0.0)
        self.assertEqual(clamp(1.1, 0.0, 1.0), 1.0)

    def test_negative_range(self):
        self.assertEqual(clamp(-20, -10, -1), -10)
        self.assertEqual(clamp(0, -10, -1), -1)
        self.assertEqual(clamp(-5, -10, -1), -5)


class ClampInvalidTest(unittest.TestCase):
    def test_reversed_range_raises_value_error(self):
        with self.assertRaises(ValueError):
            clamp(5, 10, 0)

    def test_reversed_range_raises_even_when_value_outside(self):
        with self.assertRaises(ValueError):
            clamp(-100, 10, 0)
        with self.assertRaises(ValueError):
            clamp(100, 10, 0)

    def test_equal_bounds_return_bound(self):
        self.assertEqual(clamp(3, 7, 7), 7)
        self.assertEqual(clamp(7, 7, 7), 7)
        self.assertEqual(clamp(9, 7, 7), 7)


if __name__ == "__main__":
    unittest.main()
