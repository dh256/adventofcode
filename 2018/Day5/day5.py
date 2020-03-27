import re

def processFile(fileName):
    with open(fileName, "r") as input:
        polymer = [line for line in input]
        return polymer

def oppPolarity(unit1, unit2):
    return abs(ord(unit1) - ord(unit2)) == 32

def react(polymer):
    charIndex = 0
    while charIndex < len(polymer) - 1:
        if oppPolarity(polymer[charIndex],polymer[charIndex+1]):
            if charIndex > 0:
                polymer = polymer[0:charIndex] + polymer[charIndex+2:]
                charIndex -= 1
            else:
                polymer = polymer[charIndex+2:]
                
        else:
            charIndex += 1
    return polymer

def removeUnit(polymer, unit):
    exp = unit + "|" + unit.lower()
    newPolymer = re.sub(exp, "", polymer)
    return newPolymer

# solve puzzle
polymer = processFile("day5.txt")[0]

# PART 1
newPolymer = react(polymer)
print("Units left:",len(newPolymer))

# Part 2
distr = {}
for unit in range(65,91):   
    newPolymer = removeUnit(polymer, chr(unit))
    newPolymer = react(newPolymer)
    distr[chr(unit)] = len(newPolymer)

distr = sorted(distr.items(), key=lambda x: x[1], reverse=False)
print("Removing unit",distr[0][0],"leaves",distr[0][1],"units after reaction")
