import unittest
from Fractions import Fractions
class FractionsTest(unittest.TestCase):

    def  test_baseFractionsFunctions(self):
        a = Fractions(2, 6)
        b = Fractions(2, -3)
        self.assertEqual('1/3', str(a))
        self.assertEqual('-2/3', str(b), 'Всему пиздец')

    def test_zeroFraction(self):
        a = Fractions(0, 2)
        self.assertEqual('0', str(a))

    def test_baseSumTest(self):
        a = Fractions(1, 3)
        b = Fractions(2, 9)
        c = Fractions(15, 2)
        self.assertEqual('5/9', str(a + b))
        self.assertEqual('47/6', str(a + c))
        self.assertEqual('139/18', str(b + c))

    def test_advansedSumTest(self):
        a = Fractions(-1, 3)
        b = Fractions(0, 9)
        c = Fractions(-5, -2)
        self.assertEqual('-1/3', str(a + b))
        self.assertEqual('13/6', str(a + c))
        self.assertEqual('5/2', str(b + c))

    def test_multTest(self):
        a = Fractions(1, 3)
        b = Fractions(-2, 9)
        c = Fractions(15, 2)
        self.assertEqual('-2/27', str(a * b))
        self.assertEqual('5/2', str(a * c))
        self.assertEqual('-5/3', str(b * c))

    def test_divisionTest(self):
        a = Fractions(1, 3)
        b = Fractions(-2, 9)
        c = Fractions(15, 2)
        self.assertEqual('-3/2', str(a / b))
        self.assertEqual('2/45', str(a / c))
        self.assertEqual('-4/135', str(b / c))
if __name__ == '__main__':
    unittest.main()
