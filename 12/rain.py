#! python3
# seating.py - Handles moving the ship during the storm
# Advent Of Code 2020 - Day 12

filename = "input.txt"
actions = []
compass = {'N': 0, 'E': 0, 'S': 0, 'W': 0}
directions = 'ESWN'


# Read the input file, adding each line to a list
for line in open(filename, 'r'):
    line = line.replace("\n", "")  # Removes the newline that is added in the text file
    actions.append(line)


def changeDir(turn, angle):
    """
    Adjusts the current angle of the boat
    :param turn: The direction to affect
    :param angle: The angle of how much to turn by
    :return: The new angle value
    """
    # Converts each argument to the corrent type
    turn = str(turn)
    angle = int(angle)
    if turn == 'L':             # If Left, set the negative of the angle, and divide by 90 to get 3/2/1/0
        return int(-angle / 90)
    elif turn == 'R':
        return int(angle / 90)  # If Left, set the negative of the angle, and divide by 90 to get 3/2/1/0


def part1(theActions, aCompass, theDirections):
    facing = theDirections[0]                       # Sets starting direction as East
    for action in theActions:
        # Splits the action into its Letter and its Value
        ltr = action[0]
        value = int(action[1:])
        if ltr in theDirections:                    # Check if the letter is one of the directions - ESWN
            aCompass[ltr] += value                  # Increase that direction bu its value
        elif ltr in 'LR':                           # If the letter is left or right
            # Get the current position of 'facing' from the list
            # Add that to the resulting angle from changeDir
            # Use modulus 4 to get the final position
            facing = theDirections[(theDirections.find(facing) + changeDir(ltr, value)) % 4]
        elif ltr == 'F':                            # If the letter is Forward
            aCompass[facing] += value               # Increase the facing direction by the given value
    # Find the manhattan distance
    return abs(aCompass['N'] - aCompass['S']) + (abs(aCompass['E'] - aCompass['W']))


def part2():
    return 2


print('Part 1: ' + str(part1(actions, compass, directions)))
print('Part 2: ' + str(part2()))
