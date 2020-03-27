# Day2 Part 2

def differByOneChar(boxid1, boxid2):
    """
    Loop through each boxid comparing characters in same position
    If chars are the same append char to result and continue
    If chars differ increment diffChars by 1. If diffchars > 1 then break out of loop otherwise continue
    """
    index = 0
    diffChars = 0
    result = ""
    while index < len(boxid1):
        if boxid1[index] != boxid2[index]:
            diffChars += 1
            if diffChars > 1: 
                break
        else:
            result += boxid1[index]
        index += 1

    #if only one different char found return result otherwise return None
    if diffChars == 1:
        return result
    else:
        return None

# read boxids into a list
def getBoxIds():
    with open("day2.txt", "r") as input:
        boxIds = [line.rstrip('\n') for line in input]
        return boxIds

def findDifferByOne(boxIds):
    """
    Start with first box id - compare with 2nd, 3rd, 4th .. up to end
    Then goto 2nd box id and compare with 3rd, 4th, 5th up to end
    Stop if two box id differ by one found and display result 
    """
    startIndex = 0
    endIndex = len(boxIds) - 1
    while startIndex <= endIndex:
        masterBoxId = boxIds[startIndex]
        currIndex = startIndex + 1
        while currIndex <= endIndex:
            differByOne = differByOneChar(masterBoxId, boxIds[currIndex])
            if differByOne != None:
                print(f"Result: {differByOne}")
                return
            currIndex += 1
        startIndex += 1

#solve puzzzle
boxIds = getBoxIds()
findDifferByOne(boxIds)
