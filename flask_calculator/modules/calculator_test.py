import unittest
from modules.calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_add_1_and_2__returns_3(self):
        self.assertEqual(3, self.calculator.add(1, 2))

    def test_subtract_10_and_5__returns_5(self):
        self.assertEqual(5, self.calculator.subtract(10, 5))

    def test_multiply_3_and_4__returns_12(self):
        self.assertEqual(12, self.calculator.multiply(3, 4))

    def test_divide_21_and_3__returns_7(self):
        self.assertEqual(7, self.calculator.divide(21, 3))
    