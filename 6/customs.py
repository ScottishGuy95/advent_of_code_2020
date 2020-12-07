#! python3
# customs.py - Works out how many people answered yes to a questionnaire
# Advent Of Code 2020 - Day 6

filename = "input.txt"


def part1(groups):
    count = 0
    for data in groups:
        count += len(set(data.replace("\n", "")))
    return count


def part2(groups):
    count = 0
    for data in groups:
        people = data.split("\n")   # Split string into list (abc becomes [a,b,c]
        # Loop through the characters in the list
        for answer in people[0]:    # people0 = [a,b,c]
            # Loop through the characters in the list, check if the current character matches the other characters
            # If there's a match, add it to theYes list
            theYes = [answer for person in people if answer in person]
            # Check how many people there were in the group,
            # then check if everyone in that group said yes to the same questions
            # If they did, increase count by one.
            if len(theYes) == len(people):
                count += 1
    return count


# Loop through the data, splitting each line, then splitting the data by blank lines, adding the answers to a list
with open(filename) as f:
    questions = f.read().split("\n\n")

print("Part 1: " + str(part1(questions)))
print("Part 2: " + str(part2(questions)))
