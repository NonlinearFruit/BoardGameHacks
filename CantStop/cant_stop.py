import itertools
import sys
import json

def pretty_print(thing):
    print(printStats(thing))

def printStats(results):
    result = ""
    for die, probability in results.items():
        result += str(die) + " " + str(probability*100) + "\n"
    return result

def get_die_results():
    die = [1, 2, 3, 4, 5, 6]
    results = []
    for a in die:
        for b in die:
            for c in die:
                for d in die:
                    results.append([a,b,c,d])
    return results

def get_sum_combonations_for_each_die_roll():
    dieResults = get_die_results()
    results = []
    for dieResult in dieResults:
        combos = []
        combos.append(sorted([dieResult[0] + dieResult[1], dieResult[2]+dieResult[3]]))
        combos.append(sorted([dieResult[0] + dieResult[2], dieResult[1]+dieResult[3]]))
        combos.append(sorted([dieResult[0] + dieResult[3], dieResult[2]+dieResult[1]]))
        results.append([list(x) for x in set(tuple(x) for x in combos)])
    return results

def table_of_probabilities():
    keys = range(2,13)
    sums = dict.fromkeys(keys, 0)
    for sumCombos in get_sum_combonations_for_each_die_roll():
        for key in keys:
            for sumCombo in sumCombos:
                if key in sumCombo:
                    sums[key] += 1
                    break
    total = len(get_die_results()) + 0.0
    for key in keys:
        sums[key] = sums[key] / total
    print('Probability of Getting A Sum')
    pretty_print(sums)

def ways_to_not_have_one_sum(x):
    keys = [a for a in range(2,13) if a != x]
    sums = dict.fromkeys(keys, 0)
    count = 0.0
    for sumCombos in get_sum_combonations_for_each_die_roll():
        for sumCombo in sumCombos:
            if x in sumCombo:
                break
        else:
            for key in keys:
                for sumCombo in sumCombos:
                    if key in sumCombo:
                        sums[key] += 1
                    break
            count += 1
    total = len(get_die_results()) + 0.0
    for key in keys:
        sums[key] = sums[key] / count
    print(str(count)+'/'+str(total)+' ways to not get a sum of '+str(x))
    print('  Expect '+str(expected_value(count/total))+' consecuative rolls that contain a '+str(x))
    print('\nProbability Of Getting A Sum Given A Sum Of '+str(x)+' Is Not Possible')
    pretty_print(sums)

def ways_to_not_have_two_sums(x, y):
    keys = [a for a in range(2,13) if a != x and a != y]
    sums = dict.fromkeys(keys, 0)
    count = 0.0
    for sumCombos in get_sum_combonations_for_each_die_roll():
        for sumCombo in sumCombos:
            if x in sumCombo or y in sumCombo:
                break
        else:
            for key in keys:
                for sumCombo in sumCombos:
                    if key in sumCombo:
                        sums[key] += 1
                    break
            count += 1
    total = len(get_die_results()) + 0.0
    for key in keys:
        sums[key] = sums[key] / count
    print(str(count)+'/'+str(total)+' ways to not get a sum of '+str(x)+' OR '+str(y))
    print('  Expect '+str(expected_value(count/total))+' consecuative rolls that contain a '+str(x)+' OR '+str(y))
    print('\nProbability Of Getting A Sum Given A Sum Of '+str(x)+' And A Sum Of '+str(y)+' Is Not Possible')
    pretty_print(sums)

def ways_to_not_have_three_sums(x, y, z):
    keys = [a for a in range(2,13) if a != x and a != y and a != z]
    sums = dict.fromkeys(keys, 0)
    count = 0.0
    for sumCombos in get_sum_combonations_for_each_die_roll():
        for sumCombo in sumCombos:
            if x in sumCombo or y in sumCombo or z in sumCombo:
                break
        else:
            for key in keys:
                for sumCombo in sumCombos:
                    if key in sumCombo:
                        sums[key] += 1
                    break
            count += 1
    total = len(get_die_results()) + 0.0
    for key in keys:
        sums[key] = sums[key] / count
    print(str(count)+'/'+str(total)+' ways to not get a sum of '+str(x)+' OR '+str(y)+' OR '+str(z))
    print('  Expect '+str(expected_value(count/total))+' consecuative rolls that contain a '+str(x)+' OR '+str(y)+' OR '+str(z))
    print('\nProbability Of Getting A Sum Given A Sum Of '+str(x)+' And A Sum Of '+str(y)+' And A Sum Of '+str(z)+' Is Not Possible')
    pretty_print(sums)

def possible_sums(a, b, c, d):
    combos = [a + b, c + d, a + c, b + d, a + d, c + b]
    results = sorted(list(set(combos)))
    print('All the sum combos for '+str(a)+', '+str(b)+', '+str(c)+' and '+str(d))
    print(results)

def expected_value(probability_of_not_continuing):
    return 1.0/probability_of_not_continuing - 1

if __name__ == '__main__':
    countOfNumbers = len(sys.argv) - 1
    if countOfNumbers == 0:
        table_of_probabilities()
    elif countOfNumbers == 1:
        ways_to_not_have_one_sum(int(sys.argv[1]))
    elif countOfNumbers == 2:
        ways_to_not_have_two_sums(int(sys.argv[1]), int(sys.argv[2]))
    elif countOfNumbers == 3:
        ways_to_not_have_three_sums(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]))
    elif countOfNumbers == 4:
        possible_sums(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]))
