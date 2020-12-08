#! python3
# bags.py - # TODO: Add explanation
# Advent Of Code 2020 - Day 7

filename = "input.txt"
shinyGoldBags = []  # Stores the bags that can hold a 'shiny gold' bag
with open(filename, "r") as f:
    rules = f.read().splitlines()


# How many bags have "shiny gold"
def part1(theBag):
    for rule in rules:
        # Check if the inner bags have a 'shiny gold' bag in it
        outerBag = rule.split(" bags contain")[0]
        innerBags = rule.split(" bags contain")[1]
        # print(outerBag);print(innerBags)
        if theBag in innerBags:
            # print('found GOLD SHINY in ', innerBags)
            # If they do, check if the parent bag (outerBag) has already been noted, if not, add it to the list
            if outerBag not in shinyGoldBags:
                # print('Adding parent bag: ', outerBag)
                shinyGoldBags.append(outerBag)
                # Now call part1 again, but this time passing it the outerBag to check for a 'shiny gold' bag
                part1(outerBag)


def part2(theBag):

    for rule in rules:
        # Split the inner and outer bags, and remove all spaces and fullstops
        outer, inner = rule.replace(".", "").replace(" ", "").split("contain")
        # print(outer);print(inner)
        # Check if the 'shinybag' is in the inner bags
        if theBag.replace(" ", "") in outer:
            # print('Gold bag found!')
            # If there are no innerbags to check, then just return 1
            if "noother" in inner:
                return 1
            total = 0
            # Loop through the innerbag
            for innerBag in inner.split(","):
                # Multiply the number of inner bags to the result of passing innerBag to the function again
                total += int(innerBag[0]) * part2(innerBag[1:])
            return total + 1


part1("shiny gold")
print('Part 1: ' + str(len(shinyGoldBags)))
# print(shinyGoldBags)

print('Part 2: ' + str(part2("shiny gold")-1))
