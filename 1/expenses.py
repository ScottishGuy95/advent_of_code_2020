#! python3
# expenses.py - Returns the result of multiplying of list of values, that when added together, equal 2020
# Advent Of Code 2020 - Day 1
import itertools

# Variables
filename = 'input.txt'
target = 2020
group = 3
values = set()


def getMultiplicationOfPair(numbers, goal, repeat):
    """
    Finds a group of numbers that sum to a given target number
    :param numbers: A iterable group of numbers
    :param goal: Value that the sum of numbers must reach
    :param repeat: How many numbers to group at one time
    :return: A list of numbers that sum to a target
    """
    # Loop through the data, pairing each possible combination of values
    pairs = list(itertools.product(numbers, repeat=repeat))

    # Loop through the pairs, finding the pair that equal the given goal
    for y in range(len(pairs)):
        if sum(pairs[y]) == goal:
            print('Values that sum to ' + str(target) + ': ' + str(pairs[y]))
            return pairs[y]
    else:
        return None


# Read the input file, storing all values in a list
for line in open(filename):
    if "\n" in line:
        # Removes the added newline character if it exists
        line = line.replace("\n", "")
    values.add(int(line))

# Returns a group of values that sum to the given target
result = getMultiplicationOfPair(values, target, group)
if result is not None:              # If there are no numbers, returns None
    multiply = 1
    for x in result:
        multiply = multiply * x
    print('Multiplication of values: ' + str(multiply))
else:
    print("No values that can sum to the target of: " + str(target))
