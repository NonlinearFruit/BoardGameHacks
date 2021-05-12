import unittest
from dice_throne import *

class DiceResultsTests(unittest.TestCase):

    def test_returns_proper_count_for_the_number_of_dice(self):
        result = dice_results()

        self.assertEqual(len(DIE)**DIE_COUNT, len(result))

    def test_returns_some_of_the_expected_dice_combinations(self):
        result = dice_results()

        self.assertIn([5, 5, 5, 5, 5], result)
        self.assertIn([1, 1, 1, 2, 2], result)
        self.assertIn([1, 2, 3, 4, 5], result)
        self.assertIn([2, 3, 4, 5, 6], result)

    def test_returns_proper_count_when_a_fixed_dice_is_provided(self):
        fixed = [1]

        result = dice_results(fixed)

        self.assertEqual(len(DIE)**(DIE_COUNT-len(fixed)), len(result))

    def test_returns_some_of_the_expected_dice_combinations_when_a_fixed_dice_is_provided(self):
        fixed = [1]

        result = dice_results(fixed)

        self.assertIn([1, 5, 5, 5, 5], result)
        self.assertIn([1, 1, 1, 2, 2], result)
        self.assertIn([1, 2, 3, 4, 5], result)

    def test_returns_none_of_the_unexpected_dice_combinations_when_a_fixed_dice_is_provided(self):
        fixed = [1]

        result = dice_results(fixed)

        self.assertNotIn([5, 5, 5, 5, 5], result)
        self.assertNotIn([6, 5, 4, 3, 2], result)

    def test_sorts_results(self):
        fixed = [6,5,4,6]

        result = dice_results(fixed)

        for combo in result:
            self.assertTrue(combo[0] <= combo[1])

class PowerCountTests(unittest.TestCase):

    def test_returns_zero_when_no_dice(self):
        diceResults = []
        power = [[1]]

        result = power_count(power, diceResults)

        self.assertEqual(0, result)

    def test_returns_zero_when_no_power(self):
        diceResults = [[1], [2]]
        power = []

        result = power_count(power, diceResults)

        self.assertEqual(0, result)

    def test_returns_one_when_one_match(self):
        diceResults = [[1]]
        power = [[1]]

        result = power_count(power, diceResults)

        self.assertEqual(1, result)

    def test_returns_zero_when_no_match(self):
        diceResults = [[1]]
        power = [[2]]

        result = power_count(power, diceResults)

        self.assertEqual(0, result)

    def test_returns_two_when_two_matches(self):
        diceResults = [[1], [2]]
        power = [[1], [2]]

        result = power_count(power, diceResults)

        self.assertEqual(2, result)

    def test_returns_correct_count_when_multiple_dice_results(self):
        diceResults = [[1], [1]]
        power = [[1]]

        result = power_count(power, diceResults)

        self.assertEqual(2, result)

    def test_returns_correct_count_when_a_power_matches_the_same_dice_result_multiple_times(self):
        diceResults = [[1]]
        power = [[1], [1]]

        result = power_count(power, diceResults)

        self.assertEqual(1, result)

    def test_works_with_realistic_match(self):
        diceResults = [(1,3,4,6,2), (2,6,6,7,2)]
        power = [(2,6,6,7,2)]

        result = power_count(power, diceResults)

        self.assertEqual(1, result)

    def test_works_with_subset_power(self):
        diceResults = [(1,2,3,4,6)]
        power = [(2,3)]

        result = power_count(power, diceResults)

        self.assertEqual(1, result)

    def test_rejects_subset_power_with_duplicates_that_has_no_match(self):
        diceResults = [(1,2,3,4,6)]
        power = [(2,2)]

        result = power_count(power, diceResults)

        self.assertEqual(0, result)

class CharacterToPowerListDictionaryTests(unittest.TestCase):

    def test_creates_a_record_for_each_power(self):
        die = "Bullet"
        value = 1
        power = "Revolver"
        character = dict(Dice = dict(), Powers = dict())
        character["Dice"][die] = [value]
        character["Powers"][power] = [die]

        result = character_to_power_list_dictionary(character)

        self.assertEqual(1, len(result))
        self.assertIn(power, result)

    def test_converts_string_into_combo(self):
        die = "Bullet"
        value = [1]
        power = "Revolver"
        character = dict(Dice = dict(), Powers = dict())
        character["Dice"][die] = value
        character["Powers"][power] = [die]

        result = character_to_power_list_dictionary(character)

        self.assertEqual(1, len(result[power]))
        self.assertIn(value, result[power])

    def test_converts_string_into_multi_combo(self):
        die = "Bullet"
        value = [1, 2]
        power = "Revolver"
        character = dict(Dice = dict(), Powers = dict())
        character["Dice"][die] = value
        character["Powers"][power] = [die]

        result = character_to_power_list_dictionary(character)

        self.assertEqual(2, len(result[power]))
        self.assertIn([1], result[power])
        self.assertIn([2], result[power])

    def test_converts_multi_string_into_multi_combo(self):
        die1 = "Bullet"
        die2 = "Dash"
        power = "Revolver"
        character = dict(Dice = dict(), Powers = dict())
        character["Dice"][die1] = [1, 2]
        character["Dice"][die2] = [3, 4]
        character["Powers"][power] = [die1, die2]

        result = character_to_power_list_dictionary(character)

        self.assertEqual(4, len(result[power]))
        self.assertIn([1, 3], result[power])
        self.assertIn([1, 4], result[power])

    def test_converts_multi_string_into_sorted_combos(self):
        die = "Bullet"
        value = [1, 2]
        power = "Revolver"
        character = dict(Dice = dict(), Powers = dict())
        character["Dice"][die] = value
        character["Powers"][power] = [die, die]

        result = character_to_power_list_dictionary(character)

        self.assertNotIn([2, 1], result[power])

    def test_removes_duplicates(self):
        die = "Bullet"
        value = [1, 2]
        power = "Revolver"
        character = dict(Dice = dict(), Powers = dict())
        character["Dice"][die] = value
        character["Powers"][power] = [die, die]

        result = character_to_power_list_dictionary(character)

        self.assertEqual(3, len(result[power]))

    def test_allows_for_multiple_powers(self):
        die = "Bullet"
        value = [1, 2]
        character = dict(Dice = dict(), Powers = dict())
        character["Dice"][die] = value
        character["Powers"]["Revolver 1"] = [die]
        character["Powers"]["Revolver 2"] = [die, die]
        character["Powers"]["Revolver 3"] = [die, die, die]

        result = character_to_power_list_dictionary(character)

        self.assertEqual(3, len(result))

    def test_allows_for_powers_directly_made_of_combos(self):
        power = "Revolver"
        combos = [[1,2,3], [4,5,6]]
        character = dict(Powers = dict())
        character["Powers"][power] = combos

        result = character_to_power_list_dictionary(character)

        self.assertEqual(combos, result[power])

class ChangeOfSuccess(unittest.TestCase):

    def test_handles_when_result_count_is_zero(self):
        powerCount = 1
        resultCount = 0
        rollsLefts = 1

        chance = chance_of_success(powerCount, resultCount, rollsLefts)

        self.assertEqual(0, chance)

    def test_handles_when_power_count_is_zero(self):
        powerCount = 0
        resultCount = 1
        rollsLefts = 1

        chance = chance_of_success(powerCount, resultCount, rollsLefts)

        self.assertEqual(0, chance)

    def test_handles_when_rolls_left_is_zero(self):
        powerCount = 1
        resultCount = 1
        rollsLefts = 0

        chance = chance_of_success(powerCount, resultCount, rollsLefts)

        self.assertEqual(0, chance)

    def test_returns_the_ratio_of_power_to_result_when_rolls_left_is_one(self):
        resultCount = 10
        rollsLefts = 1
        for powerCount in range(resultCount):
            chance = chance_of_success(powerCount, resultCount, rollsLefts)

            self.assertEqual(powerCount/(resultCount+0.0), chance)

    def test_one_when_large_number_of_rolls_lefts(self):
        powerCount = 1
        resultCount = 1
        rollsLefts = 10

        chance = chance_of_success(powerCount, resultCount, rollsLefts)

        self.assertEqual(1, chance)

    def test_zero_when_large_number_of_rolls_lefts(self):
        powerCount = 0
        resultCount = 1
        rollsLefts = 10

        chance = chance_of_success(powerCount, resultCount, rollsLefts)

        self.assertEqual(0, chance)

    def test_calculates_lower_success_bound_when_two_rolls_left(self):
        powerCount = 1
        resultCount = 2
        rollsLefts = 2

        chance = chance_of_success(powerCount, resultCount, rollsLefts)

        self.assertEqual(0.5 + (1 - 0.5)*0.5, chance)

    def test_calculates_lower_success_bound_when_three_rolls_left(self):
        powerCount = 1
        resultCount = 2
        rollsLefts = 3

        chance = chance_of_success(powerCount, resultCount, rollsLefts)

        self.assertEqual(.5 + .25 + .125, chance)

if __name__ == '__main__':
    unittest.main()
