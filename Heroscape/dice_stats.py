#!/usr/bin/env python
# -*- coding: utf-8 -*-
# https://math.stackexchange.com/questions/1646101/distribution-of-the-sum-of-n-loaded-dice-rolls
import sys
import numpy

attack = numpy.poly1d([.5, .5])
defense = numpy.poly1d([1./3, 2./3])

def expectedSkulls(countDice):
    return countDice / 2.0

def standardDeviationSkulls(countDice):
    expected = expectedSkulls(countDice)
    return standardDeviation(attack**countDice, expected)

def expectedShields(countDice):
    return countDice / 3.0

def standardDeviationShields(countDice):
    expected = expectedShields(countDice)
    return standardDeviation(defense**countDice, expected)

def expectedValue(polynomial):
    value = 0
    for index, coefficient in enumerate(polynomial):
        degree = polynomial.order - index
        value += degree * coefficient
    return value

def standardDeviation(polynomial, expected = None):
    squareSum = 0
    if expected == None:
        expected = expectedValue(polynomial)
    for index, coefficient in enumerate(polynomial):
        degree = polynomial.order - index
        squareSum += (degree - expected)**2 * coefficient
    return squareSum**.5

def printStats(polynomial):
    result = ""
    for index, coefficient in enumerate(polynomial):
        degree = polynomial.order - index
        result += str(degree) + " " + str(coefficient*100) + "\n"
    return result

def getWoundPolynomial(countAttackDice, countDefenseDice):
    attackPoly = attack**countAttackDice
    defensePoly = defense**countDefenseDice
    coefficients = [0] * (max(attackPoly.order, defensePoly.order)+1)
    for attackIndex, attackCoefficient in enumerate(attackPoly):
        skulls = attackPoly.order - attackIndex
        for defenseIndex, defenseCoefficient in enumerate(defensePoly):
            sheilds = defensePoly.order - defenseIndex
            wounds = max(skulls - sheilds, 0)
            probability = attackCoefficient * defenseCoefficient
            coefficients[wounds] += probability
    return numpy.poly1d(numpy.trim_zeros(list(reversed(coefficients))))

if __name__ == "__main__":
    whatDice = sys.argv[1]
    howManyDice = int(sys.argv[2])
    dice = attack

    if whatDice.lower() == "defense":
        dice = defense
        howManyDice = int(sys.argv[2])
        print(printStats(dice**howManyDice))
    elif whatDice.lower() == "attack":
        dice = attack
        howManyDice = int(sys.argv[2])
        print(printStats(dice**howManyDice))
    elif whatDice.lower() == "wound":
        attackDice = int(sys.argv[2])
        defenseDice = int(sys.argv[3])
        print(printStats(getWoundPolynomial(attackDice, defenseDice)))
    elif whatDice.lower() == "stats":
        attackDice = int(sys.argv[2])
        defenseDice = int(sys.argv[3])
        woundPoly = getWoundPolynomial(attackDice, defenseDice)
        print("Skulls: " + str(round(expectedSkulls(attackDice), 2)) + " ± " + str(round(standardDeviationSkulls(attackDice), 2)))
        print("Shields: " + str(round(expectedShields(defenseDice), 2)) + " ± " + str(round(standardDeviationShields(defenseDice), 2)))
        print("Wounds: " + str(round(expectedValue(woundPoly), 2)) + " ± " + str(round(standardDeviation(woundPoly), 2)))
