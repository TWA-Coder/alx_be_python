import unittest
from simple_calculator import SimpleCalculator


class TestCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    
    def test_addition_positive(self):

        self.assertEqual(self.calc.add(4, 5), 9)


    def test_addition_negative(self):

        self.assertEqual(self.calc.add(4, -5), -1)

    def test_addition_float(self):

        self.assertEqual(self.calc.add(4.0, 5.7), 9.7)

    def test_subtract_positive(self):

        self.assertEqual(self.calc.subtract(9, 4), 5)

    def test_subtract_negative(self):

        self.assertEqual(self.calc.subtract(-9, 4), -13)

    def test_subtract_zero(self):

        self.assertEqual(self.calc.subtract(0, 4), -4)

    def test_multiply_zero(self):

        self.assertEqual(self.calc.multiply(0, 4), 0)

    def test_multiply_positive(self):
    
        self.assertEqual(self.calc.multiply(5, 4), 20)

    def test_multiply_negative(self):

        self.assertEqual(self.calc.multiply(-6, 4), -24)

    def test_divide_zero(self):

        self.assertEqual(self.calc.divide(4, 0), None)

    def test_divide_negative(self):

        self.assertEqual(self.calc.divide(-8, 4), -2)



    
    
    