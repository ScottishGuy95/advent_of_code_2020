#! python3
# password.py - Reads the given password policy file, returning the number of valid passwords
# Advent Of Code 2020 - Day 2
import re

filename = 'input.txt'
database = []
validPass = []


def onlyOneTrue(*args):
    return sum(args) == 1


# Store file contents into a list
for line in open(filename, 'r'):
    line = line.replace("\n", "")       # Removes the newline that is added in the text file
    database.append(line)
print(len(database))

# Use regex to split the line into the policy/password parts
passRegex = re.compile(r'(\d*)-(\d*)\s(\w):\s(\w*)')
for policy in database:
    matchObj = passRegex.search(policy)
    pos1, pos2, letter, password = matchObj.groups()
    pos1Valid = False
    pos2Valid = False
    if len(password) >= int(pos1) >= 0:
        if len(password) >= int(pos2) >= 0:
            if password[int(pos1)-1] == letter:
                pos1Valid = True
            if password[int(pos2)-1] == letter:
                pos2Valid = True
            result = onlyOneTrue(pos1Valid, pos2Valid)
            if result:
                validPass.append(policy)
            else:
                continue
print(len(validPass))

# Part 2




