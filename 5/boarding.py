#! python3
# boarding.py - From the input, find the seat number
# Advent Of Code 2020 - Day 5

filename = "input.txt"
seatIDs = []
tickets = []

for ticket in open(filename, 'r'):
    ticket = ticket.replace("\n", "")
    # tickets.append(line)

    # Fill a list of rows from 0-127, and a list of columns from 0-7
    row, col = [x for x in range(128)], [y for y in range(8)]
    # Split the ticket into the 7 row digits, and the 3 column digits
    ticketRow, ticketCol = ticket[:7], ticket[7:]

    # Each loop, pass it the row list, and find out if its it needs to be split by upper or lower half
    for i in ticketRow:
        if i == "F":
            # Get the lower half of the numbers, store it in a list to pass it around again
            row = row[:len(row) // 2]    # From lowest number, half the list
        if i == "B":
            # Get the upper half of the numbers, store it in a list to pass it around again
            row = row[len(row) // 2:]   # From the highest number halved, to the end
    # Each loop, pass it the list of columns, check if it needs split by the upper or lower half
    # Then pass the split list again, repeating the process
    for j in ticketCol:
        if j == "L":
            # Get the lower half of the numbers, from lowest number, to half the list
            col = col[:len(col) // 2]
        if j == "R":
            # Get the upper half of the numbers, from half the list to the top
            col = col[len(col) // 2:]
    seatID = (row[0] * 8) + col[0]
    seatIDs.append(seatID)
maxID = 0
for seat in seatIDs:
    if seat > maxID:
        maxID = seat
print('Max seat ID = ' + str(maxID))

# Part 2 - Find the users seat ID
sortedSeats = sorted(seatIDs)       # Sort the seatIDs in order
# Create a list of seatIDs, that go from the lowest seatID to highest seatID
# Sum the total of this list, then subtract this from the sum of our seatIDs
# This will return what number is missing from the list
shouldBe = [x for x in range(sortedSeats[0], sortedSeats[-1]+1)]
yourID = sum(shouldBe) - sum(sortedSeats)
print('Your seat ID = ' + str(yourID))

