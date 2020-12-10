#! python3
# adapter.py - Analyse the voltage numbers from the available adapters
# Advent Of Code 2020 - Day 10
from collections import defaultdict

filename = "input.txt"
jolts = []

# Read the input file, adding each line to a list
for line in open(filename, 'r'):
    line = line.replace("\n", "")       # Removes the newline that is added in the text file
    jolts.append(int(line))
jolts = sorted(jolts)


def part1(jolts):
    adapter = 0
    differences = []
    for x in jolts:                                 # Loop through each jolt available
        if x <= (adapter + 3):                      # Check if this current jolt is in the range of 1-3 jolts above
            differences.append(abs(x - adapter))    # Add the difference between the jolts
            adapter = x                             # Set the adapter to the current jolt
    jolt1 = [value for value in differences if value == 1]      # If the difference is 1, add to jolt1 list
    jolt3 = [value for value in differences if value == 3]      # If the difference is 3, add to jolt3 list
    return len(jolt1) * (len(jolt3) + 1)    # Add 1 at end, as adapter can do up to plus 3 jolts


def part2(jolts):
    paths = defaultdict(int)       # Create a defaultDict, that auto initialises a key:value pair
    paths[0] = 1                   # Create the first key:value pair with a value of 1
    for j in sorted(jolts):                 # Loop ever element in the given list of jolts
        # Set the key to the addition of all 3 possible jolts (as each can increase by 1 or 2 or 3)
        paths[j] = paths[j-1] + paths[j-2] + paths[j-3]
    return paths[max(jolts)]        # Get the last key (which is the max value in the jolts list) and return its value


print('Part 1: ' + str(part1(jolts)))
print('Part 2: ' + str(part2(jolts)))
