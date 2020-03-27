# Day 2 - Part 1
input = open("day2.txt", "r")
twos = 0
threes = 0
for line in input:
    # count the number of occurrences of each letter
    print("Processing: ", line)
    letterCount = {}
    for letter in line:
        if letter in letterCount:
            letterCount[letter] += 1
        else:
            letterCount[letter] = 1

    # count whether any two or three occurrences of any letter
    countTwos = False
    countThrees = False
    for x, y in letterCount.items():
        if y == 2: countTwos = True
        if y == 3: countThrees = True

    # if any add to running total
    if countTwos: twos += 1
    if countThrees: threes += 1 

# Multiply the number of 2s and 3s and display answer
print("Checksum: ", twos * threes)