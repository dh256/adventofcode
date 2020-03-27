from functools import reduce

gridSize = 300
gridSerialNo = 9221

def calculatePowerLevel(x,y):
    rackId = x + 10
    powerLevel = rackId * y
    powerLevel = powerLevel + gridSerialNo
    powerLevel = powerLevel * rackId
    powerLevel = (powerLevel % 1000) // 100
    powerLevel = powerLevel - 5
    return powerLevel

# fill power grid
powerGrid = []
for y in range(1,gridSize+1):
    gridX = []
    for x in range (1,gridSize+1):
        gridX.append(calculatePowerLevel(x,y))
    powerGrid.append(gridX)

def totalPowerRec(largestSquare, startX, startY, s=1, prevTotal=0):
    # if largest square exceeded or off end of grid stop iteration
    if s > largestSquare or startX+s >= gridSize or startY+s >= gridSize:
        return
    else:
        total = prevTotal
        y = startY + (s-1)
        for x in range(startX,startX + s):
            total += powerGrid[y][x] 
        x = startX + (s-1)
        for y in range(startY,startY + (s-1)):
            total += powerGrid[y][x]
        powerSquares[(startX+1,startY+1,s)] = total   # record power total
        totalPowerRec(largestSquare, startX,startY,s+1, total)    # recursively call next square
        return

# calculate matrix sum (total power) of sqare size s * s starting at y,x
def totalPower(x,y,s):
    sum = 0
    rows = powerGrid[y:y+s]
    for row in rows:
        sum += reduce(lambda a,b: a+b, row[x:x+s])
    return sum

# calclulate power total of all 3 * 3 squares for each starting point in power grid 
powerSquares = {}
s=3
print(f"Calculating power for squares {s} * {s}")
for y in range(0,(gridSize-s)+1):
    for x in range(0,(gridSize-s)+1):
        power = totalPower(x,y,s)
        powerSquares[(x+1,y+1,s)] = power  
biggestPower = sorted(powerSquares.items(), key=lambda item:item[1] , reverse=True)[0]
print(biggestPower)

# PART 2: Set largest square
# Above method too slow. Use a recursive algorithm to build up totals iteratively
largestSquare = 300
powerSquares = {}
for y in range(0,gridSize):
    print(f"Row: {y}")
    for x in range(0,gridSize):
        totalPowerRec(largestSquare,x,y)

# sort by size (reverse order) and take biggest
biggestPower = sorted(powerSquares.items(), key=lambda item:item[1] , reverse=True)[0]
print(biggestPower)
