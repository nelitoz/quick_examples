import calc
import unittest


class TestCalc(unittest.TestCase):
    def test_add(self):
        result = calc.add(10, 5)
        self.assertEqual(15, result)

        #another simple way
        self.assertEqual(calc.add(1, -1), 0)
        self.assertEqual(calc.add(-1, 2), 1)
        self.assertEqual(calc.add(-1, -1), -2)

    def test_substract(self):
        self.assertEqual(calc.substract(1, 1), 0)
        self.assertEqual(calc.substract(10, 5), 5)
        self.assertEqual(calc.substract(-1, -1), 0)
        self.assertEqual(calc.substract(-5, 2), -7)

    def test_multiply(self):
        self.assertEqual(calc.multiply(3, 3), 9)
        self.assertEqual(calc.multiply(-3, 3), -9)
        self.assertEqual(calc.multiply(-3, -3), 9)
        self.assertEqual(calc.multiply(0, 3), 0)

    def test_divide(self):
        self.assertEqual(calc.divide(3, 3), 1)
        self.assertEqual(calc.divide(-3, 3), -1)
        self.assertEqual(calc.divide(4, 5), 0.8)

        self.assertRaises(ValueError, calc.divide, 10, 0)

        #same test as above but with context manager
        with self.assertRaises(ValueError):
            calc.divide(10, 0)
        
if __name__ == "__main__":
    unittest.main()