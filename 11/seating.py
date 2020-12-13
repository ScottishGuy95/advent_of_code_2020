#! python3
# seating.py -
# Advent Of Code 2020 - Day 11

filename = "test.txt"
floor = '.'
empty = 'L'
use = '#'
seats = []
# Read the input file, adding each line to a list
for line in open(filename, 'r'):
    line = line.replace("\n", "")       # Removes the newline that is added in the text file
    seats.append(line)
print(seats)


def part1(seats):
    return 1


def part2():
    return 2


print('Part 1: ' + str(part1(seats)))
print('Part 2: ' + str(part2()))
