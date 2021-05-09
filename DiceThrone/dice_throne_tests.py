import unittest
from dice_throne import *

class DiceResultsTests(unittest.TestCase):

    def test_returns_proper_count_for_the_number_of_dice(self):
        result = dice_results()

        self.assertEqual(len(DIE)**DIE_COUNT, len(result))

    def test_returns_some_of_the_expected_dice_combinations(self):
        result = dice_results()

        self.assertIn((5, 5, 5, 5, 5), result)
        self.assertIn((1, 2, 1, 2, 1), result)
        self.assertIn((1, 2, 3, 4, 5), result)
        self.assertIn((6, 5, 4, 3, 2), result)

    def test_returns_proper_count_when_a_fixed_dice_is_provided(self):
        fixed = [1]

        result = dice_results(fixed)

        self.assertEqual(len(DIE)**(DIE_COUNT-len(fixed)), len(result))

    def test_returns_some_of_the_expected_dice_combinations_when_a_fixed_dice_is_provided(self):
        fixed = [1]

        result = dice_results(fixed)

        self.assertIn((1, 5, 5, 5, 5), result)
        self.assertIn((1, 2, 1, 2, 1), result)
        self.assertIn((1, 2, 3, 4, 5), result)
        self.assertIn((1, 5, 4, 3, 2), result)

    def test_returns_none_of_the_unexpected_dice_combinations_when_a_fixed_dice_is_provided(self):
        fixed = [1]

        result = dice_results(fixed)

        self.assertNotIn((5, 5, 5, 5, 5), result)
        self.assertNotIn((6, 5, 4, 3, 2), result)

if __name__ == '__main__':
    unittest.main()
