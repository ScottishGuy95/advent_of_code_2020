#! python3
# shuttle.py - The waiting time for each bus
# Advent Of Code 2020 - Day 13

filename = "input.txt"
data = []

# Read the input file, adding each line to a list
for line in open(filename, 'r'):
    line = line.replace("\n", "")  # Removes the newline that is added in the text file
    data.append(line)
timestamp = int(data[0])
IDs = [int(x) for x in data[1].split(',') if x != 'x']
IDs = dict((id, 0) for id in IDs)


def part1(time, ids):
    for bus in ids:
        bus = bus
        ids[bus] = (bus - time) % bus
    # print(ids)
    # The first bus is the bus with the lowest value
    # So Loop through all keys/values, and find the key that has the lowest value
    first = [key for key, value in ids.items() if value == min(ids.values())]   # First possible bus
    first = int(first[0])           # Turn the list value into an int
    wait = ids[first]               # The time that you need to wait from arrival to bus departure
    result = first * wait
    return result


def part2():
    return 2


print('Part 1: ' + str(part1(timestamp, IDs)))
print('Part 2: ' + str(part2()))
