#! python3
# trajectory.py - Traverse the input.txt, listing each Tree that is encountered.
# Advent Of Code 2020 - Day 3
filename = 'input.txt'
data = []

# Store file contents into a list
for line in open(filename):
    line = line.replace("\n", "")
    data.append(line)


def countTrees(data, right, down):
    """
    Counts the number of times a tree (#) is detected at the positions,
    going right x times across a string of data, then down y line of data
    :param data: The list of data to check for trees
    :param right: How many characters to move across ecah row
    :param down: How many times to move down a row of data
    :return: The amount of trees counted
    """
    treeCount = 0               # Stores the amount of trees detected
    # Loop the data, increasing by the down value every time
    for x in range(0, len(data), down):
        # Gets how many to move along
        # Then gets the remainder from the line and how much to move along
        move = ((x/down) * right) % (int(len(data[x])))
        # Checks if the current line of data, at the 'move' position is a Tree
        if data[x][int(move)] == "#":
            treeCount += 1
    return treeCount


t1 = countTrees(data, 1, 1)
t2 = countTrees(data, 3, 1)
t3 = countTrees(data, 5, 1)
t4 = countTrees(data, 7, 1)
t5 = countTrees(data, 1, 2)
print(t1*t2*t3*t4*t5)
