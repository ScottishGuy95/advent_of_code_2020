#! python3
# passports.py - From the input, counting the valid passports
# Advent Of Code 2020 - Day 4
import re, sys

filename = 'input.txt'
validPassports = 0


# Create a function that accepts a dictionary, checking if all of the keys required are there
# Against a list of required fields (8 normally or 7 if north pole)
# If true, return true
def checkFields(dic):
    expecting = sorted(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid'])
    keys = sorted(list(dic.keys()))
    if expecting == keys:
        return True
    else:
        if len(keys) == len(expecting)-1 and 'cid' not in keys:
            return True
        else:
            return False


def getValidPassports(passportDict):
    rules = []      # Stores the true, false state for each rule
    for k, v in passportDict.items():
        if k == 'byr':
            if len(v) == 4 and 1920 <= int(v) <= 2002:
                rules.append(True)             # Add 1 if valid
        elif k == 'iyr':
            if len(v) == 4 and 2010 <= int(v) <= 2020:
                rules.append(True)
        elif k == 'eyr':
            if len(v) == 4 and 2020 <= int(v) <= 2030:
                rules.append(True)
        elif k == 'hgt':
            number = int(''.join(filter(str.isdigit, v)))
            measure = ''.join(filter(str.isalpha, v))
            if measure == "cm":
                if 150 <= number <= 193:
                    rules.append(True)
            if measure == "in":
                if 59 <= number <= 76:
                    rules.append(True)
        elif k == 'hcl':
            require = re.compile(r'[A-Zg-z]')
            if str(v).startswith("#") and len(v[1:]) == 6:
                colour = v[1:]
                if not require.search(colour):
                    rules.append(True)
        elif k == 'ecl':
            validEyes = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
            if v in validEyes:
                rules.append(True)
        elif k == 'pid':
            if len(str(v)) == 9:
                rules.append(True)
    if len(rules) == 7 or len(rules) == 8:
        if False not in rules:
            return True
        else:
            return False


# Read the input, storing each 'passport' as its own line in a list, separated by the blank lines
messyPassports = []
with open(filename) as f:
    messyPassports.append(f.read())

splitPassports = []
allPassports = messyPassports[0].split("\n\n")
for passport in allPassports:
    splitPassports.append(passport.replace('\n', ' '))

for passport in splitPassports:
    field = passport.split(" ")
    fields = dict(s.split(":") for s in field)
    # valid = checkFields(fields)   - Part 1
    valid = checkFields(fields)
    if valid:
        if getValidPassports(fields):
            validPassports += 1

print(validPassports)

# Print return of the passport function
