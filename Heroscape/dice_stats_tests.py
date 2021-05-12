import unittest
from dice_stats import *

class ExpectedSkullsTests(unittest.TestCase):

    def test_expected_skulls_works(self):
        result = True
        table = { 0:0, 1:0.5, 2:1, 100:50 }
        for countDice in table.keys():
            result = result and expectedSkulls(countDice) == table[countDice]
        self.assertTrue(result)

class StandardDeviationSkullsTests(unittest.TestCase):

    def test_standard_deviation_skulls_works(self):
        result = True
        result = result and standardDeviationSkulls(5) == 1.118033988749895
        result = result and standardDeviationSkulls(1) == .5
        self.assertTrue(result)

    def test_standard_deviation_shields_works(self):
        result = True
        result = result and standardDeviationShields(5) == 1.0540925533894596
        result = result and standardDeviationShields(1) == 0.4714045207910317
        self.assertTrue(result)

    def test_standard_deviation_works(self):
        result = True
        result = result and standardDeviation(numpy.poly1d([.5, .5])) == .5
        result = result and standardDeviation(numpy.poly1d([1./6, 1./6, 1./6, 1./6, 1./6, 1./6, 0])) == 1.707825127659933
        self.assertTrue(result)

class ExpectedValueTests(unittest.TestCase):

    def test_expected_value_works(self):
        result = True
        result = result and expectedValue(numpy.poly1d([.5,.5])) == .5
        result = result and expectedValue(numpy.poly1d([1./6, 1./6, 1./6, 1./6, 1./6, 1./6, 0])) == 3.5
        self.assertTrue(result)

class ExpectedShieldsTests(unittest.TestCase):

    def test_expected_shields_works(self):
        result = True
        table = { 0:0, 3:1, 9:3, 27:9 }
        for countDice in table.keys():
            result = result and expectedShields(countDice) == table[countDice]
        self.assertTrue(result)

class PrintStatsTests(unittest.TestCase):

    def test_print_stats_works(self):
        result = True
        result = result and printStats(numpy.poly1d([.5])) == "0 50.0\n"
        result = result and printStats(numpy.poly1d([.1, .6, .3])) == "2 10.0\n1 60.0\n0 30.0\n"
        self.assertTrue(result)

class GetWoundPolynomialTests(unittest.TestCase):

    def test_get_wound_polynomial_works(self):
        result = True
        result = result and getWoundPolynomial(0,9)[0] == 0.9999999999999996
        result = result and getWoundPolynomial(1,1)[0] == 0.6666666666666666
        result = result and getWoundPolynomial(1,1)[1] == 0.3333333333333333
        result = result and getWoundPolynomial(2,1)[0] == 0.41666666666666663
        result = result and getWoundPolynomial(2,1)[1] == 0.41666666666666663
        result = result and getWoundPolynomial(2,1)[2] == 0.16666666666666666
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()
