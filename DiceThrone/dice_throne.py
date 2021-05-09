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
    return list(itertools.product(*dice))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("character", help="Name Of The Character To Use", nargs='?', type=str)
    parser.add_argument("-d", "--dice", help="Currently Saved Dice", nargs='+', type=int)
    parser.add_argument("-r", "--rolls-left", help="Number Of Rerolls Remaining", type=int)
    args = parser.parse_args()
    character = load_character(args.character)
    diceResults = dice_results(args.dice)
    print(diceResults)
