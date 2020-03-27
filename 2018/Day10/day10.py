class Point:
    def __init__(self, startPosition, velocity):
        self.currentPosition = startPosition
        self.velocity = velocity


class Sky:
    def __init__(self, inputRecords):
        self.time = 0
        self.points = [Point(inputRecord[0], inputRecord[1]) for inputRecord in inputRecords]

    def move(self,reverse=False):
        for point in self.points:
            if not reverse:
                point.currentPosition.x += point.velocity.x 
                point.currentPosition.y += point.velocity.y
            else:
                point.currentPosition.x += (point.velocity.x * -1)
                point.currentPosition.y += (point.velocity.y * -1)

    def displayGridLimits(self):
        maxX = max(self.points, key = lambda item:item.currentPosition.x).currentPosition.x
        minX = min(self.points, key = lambda item:item.currentPosition.x).currentPosition.x
        maxY = max(self.points, key = lambda item:item.currentPosition.y).currentPosition.y
        minY = min(self.points, key = lambda item:item.currentPosition.y).currentPosition.y
        return (minX, minY, maxX, maxY)

    def size(self):
        limits = self.displayGridLimits()
        size = (limits[2]-limits[0]) * (limits[3] - limits[1])
        return size

    def possibleLetters(self):
        """
        Sort points by x axis and look for any contiguos points
        That is any points with same x value whose y value is within 1 of point

        This method works but still not as efficient as simply stopping at the point sky stops converging.
        Notice that letters displayed at point sky is smallest size
        """
        sortedPointsX = list(sorted(self.points, key = lambda item:(item.currentPosition.x, item.currentPosition.y)))
        xPossible = False
        xcontiguosPoints = 0
        for index in range(1, len(sortedPointsX)-1):
            if sortedPointsX[index-1].currentPosition.x == sortedPointsX[index].currentPosition.x and abs(sortedPointsX[index-1].currentPosition.y - sortedPointsX[index].currentPosition.y) == 1:
                xcontiguosPoints += 1            
                if xcontiguosPoints > 2:
                    xPossible = True
                    break;
            else:
                xcontiguosPoints = 0

        sortedPointsY = list(sorted(self.points, key = lambda item:(item.currentPosition.y, item.currentPosition.x)))
        yPossible = False
        ycontiguosPoints = 0
        for index in range(1, len(sortedPointsY)-1):
            if sortedPointsY[index-1].currentPosition.y == sortedPointsY[index].currentPosition.y and abs(sortedPointsY[index-1].currentPosition.x - sortedPointsY[index].currentPosition.x) == 1:
                ycontiguosPoints += 1            
                if ycontiguosPoints > 2:
                    yPossible = True
                    break;
            else:
                ycontiguosPoints = 0

        return xPossible and yPossible

    def display(self):
        limits = self.displayGridLimits()
        display = []
        for _ in range(limits[1],limits[3]+1):
            line = ['.'] * (limits[2] - limits[0] + 1)
            display.append(line)

        for point in self.points:
            line = display[point.currentPosition.y-limits[1]]
            line[point.currentPosition.x-limits[0]] = "#"
        return display

class Position:
    def __init__(self, coords):
        self.x = int(coords[0])
        self.y = int(coords[1])

class Velocity:
    def __init__(self, changes):
        self.x = int(changes[0])
        self.y = int(changes[1]) 

def processLine(line):
    # find < and  > chars and extract everything between positions split on ", " to get x and y
    openIndices = [i for i, c in enumerate(line) if c == '<']
    closeIndices = [i for i, c in enumerate(line) if c == '>']

    startCoords = line[openIndices[0]+1:closeIndices[0]]
    startPosition = Position(startCoords.split(', '))

    velocityChanges = line[openIndices[1]+1:closeIndices[1]]
    velocity = Velocity(velocityChanges.split(', '))
    
    return (startPosition,velocity)

def processFile(filename):
    # extract position and velocity from 
    # input is a list of Position,Velocity tuples
    with open(filename, "r") as input:
        inputRecords = [processLine(line.strip()) for line in input]
        return inputRecords    


# solve puzzle
inputRecords = processFile("day10.txt")
sky = Sky(inputRecords)
time = 0 
prevSkySize = sky.size()
while True:
    sky.move()
    time += 1
    sky.time = time
    newSkySize = sky.size()
    if newSkySize > prevSkySize:  
        print(f'Time: {time-1}:')
        sky.move(reverse=True)      # move back 1 step
        display = sky.display()     
        for line in display:
            output = ""
            for c in line:
                output += c
            print(output)  
        break
    else:
        prevSkySize = newSkySize
