import unittest
import unittest
import calc


class sumtest(unittest.TestCase):
    def test_sum(self):
        result = calc.sum(3, 5)
        self.assertEqual(8, result)

    def test_minus(self):
        self.assertEqual(5, calc.minus(10, 5))
