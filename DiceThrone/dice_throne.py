import yaml
import argparse
import itertools

DIE = [1, 2, 3, 4, 5, 6]
DIE_COUNT = 5

def load_character(character):
    with open(character+'.yml', 'r') as file:
       return yaml.safe_load(file)

def dice_results(fixedDice = None):
    dice = []
    if not fixedDice:
        fixedDice = []
    for die in fixedDice:
        dice.append([die])
    numberOfDiceToRoll = DIE_COUNT - len(fixedDice)
    for die in range(numberOfDiceToRoll):
        dice.append(DIE)
    return [sorted(combo) for combo in itertools.product(*dice)]

def power_count(powerList, diceResults):
    count = 0
    for dice in diceResults:
        for power in powerList:
            if all(dice.count(value) >= power.count(value) for value in power):
                count += 1
                break
    return count

def character_to_power_list_dictionary(character):
    result = dict()
    for powerName in character["Powers"]:
        options = []
        power = character["Powers"][powerName]
        if type(power[0]) is not list:
            for value in power:
                options.append(character["Dice"][value])
            result[powerName] = [sorted(thing) for thing in itertools.product(*options)]
        else:
            result[powerName] = power
    return result

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("character", help="Name Of The Character To Use", nargs='?', type=str)
    parser.add_argument("-d", "--dice", help="Currently Saved Dice", nargs='+', type=int)
    parser.add_argument("-r", "--rolls-left", help="Number Of Rerolls Remaining", type=int)
    args = parser.parse_args()
    character = load_character(args.character)
    diceResults = dice_results(args.dice)
    diceResultsCount = len(diceResults)
    powerListDictionary = character_to_power_list_dictionary(character)
    for power, powerList in powerListDictionary.items():
        powerCount = power_count(powerList, diceResults)
        print(power+" :: "+str(powerCount)+" / "+str(diceResultsCount))
