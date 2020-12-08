#! python3
# accumulator.py - Read the bootcode, and find the accumulator value
# Advent Of Code 2020 - Day 7
import re
from copy import deepcopy

filename = "input.txt"


def secondTime(instruction, bootDct):
    """
    Used in part1
    :param instruction: A list of bootcode from the textfile
    :param bootDct: A dictionary of the bootcode lines, each line with a unique ID
    :return: True if the task has run before, False if not
    """
    if bootDct.get(instruction) > 1:
        return True
    else:
        return False


def handleCorrupted(lines):
    """
    Used only in part2
    :param lines: The bootcode in a list
    :return: The total value of acc or None if we need to run the function again
    """
    visitedIndexes = set()
    index = acc = 0
    while True:
        # If we hit the last line, return the value
        if index == len(lines):
            return acc
        # If we hit the same value again, return None as we are repeating ourselves
        if index in visitedIndexes:
            return None
        visitedIndexes.add(index)           # Add the value to ensure we only loop unique lines
        theLine = lines[index]
        aJob, number = theLine.split(' ')   # Split the line into task and value
        number = int(number)
        if aJob == 'acc':
            acc += number
            index += 1
        elif aJob == 'jmp':
            index += number
        elif aJob == 'nop':
            index += 1


def part1():
    bootDict = {}
    # Loop through the input file, on each loop, add each line to a list
    with open(filename, "r") as f:
        instructions = f.read().splitlines()
    # From the list of lines, add a unique ID to each list element
    # Then add that new line to a dictionary, and give it zero
    # This value of 0 will be used to check how many times a line is run
    for x in range(len(instructions)):
        instructions[x] = str(x) + ':' + instructions[x]
        bootDict[instructions[x]] = 0
    accum = 0
    i = 0
    exit = False
    # Run until the a task has run twice
    while exit is False:
        # Split each line into parts
        theRegex = re.compile(r'(\d*):(\w*)\s(\+|\-)(\d*)')
        matchObj = theRegex.search(instructions[i])
        ID, job, operator, value = matchObj.groups()
        value = int(value)
        # Check if the current task has already been run twice
        if secondTime(instructions[i], bootDict) is False:
            # Complete each tasks action
            if job == "nop":
                i += 1
            elif job == "acc":
                if operator == '+':
                    accum += value
                elif operator == '-':
                    accum -= value
                i += 1
            elif job == "jmp":
                if operator == '+':
                    i += value
                elif operator == '-':
                    i -= value
            # The task has been run, increase it by one
            bootDict[instructions[i]] += 1
        else:
            break   # Task already ran, so ending the loop
    return accum


def part2():
    data = []
    # Store each line in a list
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()
            data.append(line)

    # Loop through a list of each line, but add an unique ID to each line
    for i, eachLine in enumerate(data):
        newList = deepcopy(data)
        # Replace the jmp or nop with the other
        if eachLine.startswith('jmp'):
            newList[i] = eachLine.replace('jmp', 'nop')
        elif eachLine.startswith('nop'):
            newList[i] = eachLine.replace('nop', 'jmp')
        else:
            continue
        # Pass the new list to the program, if it returns a value, show the value
        totalAcc = handleCorrupted(newList)
        if totalAcc:
            return totalAcc


# print(instructions)
# print(bootDict)
print('Part 1 Accumulator = ' + str(part1()))
print('Part 2Accumulator = ' + str(part2()))
