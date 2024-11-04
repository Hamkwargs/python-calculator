import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)

    def test_add_negative(self):
        self.assertEqual(self.calc.add(-1, -2), -3)


    def test_subtract(self):
        self.assertEqual(self.calc.subtract(5, 3), 2)

    def test_subtract_negative(self):
        self.assertEqual(self.calc.subtract(3, 5), -2)


    def test_multiply(self):
        self.assertEqual(self.calc.multiply(3, 4), 12)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(0, 0), "you can not multiply by ZERO")


    def test_divide(self):
        self.assertEqual(self.calc.divide(14, 2), 7)

    def test_devide(self):
        self.assertEqual(self.calc.divide(0, 0), "you can not devide by ZERO")



    def test_modulo(self):
        self.assertEqual(self.calc.modulo(14, 2), 0)

    def test_modulo(self):
        self.assertEqual(self.calc.modulo(20, 9), 2)

    def test_modulo(self):
        self.assertEqual(self.calc.modulo(14, "a"), "Error")


        
    # Add the following test methods to the TestCalculator class:

if __name__ == '__main__':
    unittest.main()