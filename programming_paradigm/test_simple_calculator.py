import unittest
from simple_calculator import SimpleCalculator


class TestCalculator(unittest.TestCase):

    
    def test_add_positive(self):
        result = add(4, 5)
        self.assertEquals(result, 9)


    def test_add_negative(self):
        result = add(4, -5)
        self.assertEquals(result, -1)

    def test_add_float(self):
        result = add(4.0, 5.7)
        self.assertEquals(result, 9.7)
    