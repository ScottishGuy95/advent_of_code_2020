#! python3
# EncodingError.py - Find the weakness in the XMAS encryption
# Advent Of Code 2020 - Day 9
from itertools import combinations

filename = "input.txt"
preambleLen = 25

# Read the input file, adding each line to a list
with open(filename, "r") as f:
    data = f.read().splitlines()


def isSum(preamble, check):
    # Loops every possible pair of values from the preamble
    for combo in combinations(preamble, 2):
        # Check if the sum or a pair, is in the preamble or if it is the same value as the check value
        if sum(combo) in preamble or int(check) == sum(combo):
            return False
        else:
            continue
    # If the check value cannot be found again via a sum(), it is the encoded error
    return check


def part1(preambleLen):
    # Loop the from the first value after the preamble to the end
    for x in range(preambleLen, len(data)-1):
        preamble = [int(value) for value in data[x-preambleLen:x]]   # Get the first 25 values
        # print()
        # print(preamble)
        # print('checking ', str(data[x]))
        # Pass the current preamble and the current value to check to the function isSum
        result = isSum(preamble, data[x])
        # If isSum returns any value, that is the value that cannot be summed into the preamble, so return it
        if result is not False:
            return result
        else:       # The value to check was found in the preamble, so try the next value
            continue


def part2(invalid):
    # Take the invalid result from the result of part1
    index = 0                               # Create an index value for the while loop
    sumList = []                            # A list to store each of the lines from data
    while index < len(data):
        # Loop from the current line to the last line
        for value in data[index:]:
            sumList.append(int(value))      # Add the current line to the list
            # Check if the sum of this list, is greater than the given invalid number
            if sum(sumList) > int(invalid):
                index += 1
                sumList = []
                break
            # Check if the sum of the list is the same as the invalid number
            if sum(sumList) == int(invalid):
                # Get the smallest and largest and add them together
                # Returning the 'encryption weakness'
                return min(sumList) + max(sumList)


print('Part 1: ' + str(part1(preambleLen)))
print('Part 2: ' + str(part2(part1(preambleLen))))
