#! python3
# password.py - Reads the given password policy file, returning the number of valid passwords
# Advent Of Code 2020 - Day 2
import re

filename = 'input.txt'
database = []
validPass = []

# Store password file contents into
for line in open(filename, 'r'):
    line = line.replace("\n", "")       # Removes the newline that is added in the text file
    database.append(line)
print(len(database))

# Use regex to split the line into the policy/password parts
passRegex = re.compile(r'(\d*)-(\d*)\s(\w):\s(\w*)')
for policy in database:
    matchObj = passRegex.search(policy)
    minTime, maxTime, letter, password = matchObj.groups()
    count = 0
    for ch in password:
        if ch == letter:
            count += 1
    if count < int(minTime) or count > int(maxTime):
        continue
    else:
        validPass.append(matchObj.string)
print(len(validPass))

# Part 2 - Is available in file password2.py
