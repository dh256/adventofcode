from enum import Enum   

class Area():
    '''
    # = WALL
    G = GOBLIN
    E = ELF
    . = EMPTY SPACE
    '''
    rows = 32
    cols = 32
    def __init__(self):
        self.caves = []    
        self.Units = Units()

    def addUnit(self,position,unitType):
        self.Units.add(Unit(position,unitType))

    def buildLine(self,row,line):
        newLine = []
        for col, c in enumerate(line):
            if c in ['E','G']:
                unitType = UnitType.ELF if c == 'E' else UnitType.GOBLIN
                self.addUnit(Position(col,row),unitType)
            newLine.append(c)
        self.caves.append(newLine)

    def build(self,filename):
        with open(filename,"r") as fileInput:
            for row, line in enumerate(fileInput):
                self.buildLine(row,line.strip('\n'))

    def __repr__(self):
        output = ""
        for row in self.caves:
            for col in row:
                output += col
            output += '\n'
        return output

    def adjancentSquares(self,unit):
        adjacent_left = adjacent_down = adjacent_up = adjacent_right = None 
        # adjacent_left
        if unit.Position.x > 0:
            if caves[unit.Position.y][unit.Position.x-1] == '.':
                adjacent_left = Position(unit.Position.x - 1, unit.Position.y)

        # adjacent_right
        if unit.Position.x < self.cols - 1:
            if caves[unit.Position.y][unit.Position.x+1] == '.':
                adjacent_right = Position(unit.Position.x + 1, unit.Position.y)

        # adjancent_down
        if unit.Position.y < self.rows - 1:
            if caves[unit.Position.y+1][unit.Position.x] == '.':
                adjacent_down = Position(unit.Position.x, unit.Position.y + 1)

        # adjancent_up
        if unit.Position.y > 0:
            if caves[unit.Position.y-1][unit.Position.x] == '.':
                adjacent_down = Position(unit.Position.x, unit.Position.y - 1)

        return(adjacent_up,adjacent_down,adjacent_left,adjacent_right)

    def anyAdjacentSquares(self,unit):
        adjacentSquares = self.adjancentSquares(unit)
        return not adjacentSquares[0] == None and adjacentSquares[1] == None and adjacentSquares[2] == None and adjacentSquares[3] == None

    def inRange(self,currUnit):
        '''
        Identify all units that are in range of the given unit
        This is any unit of the opposite type who has an empty adjacent square
        empty is any square up,down,left,right of a unit that is an empty square
        '''
        targets = [unit for unit in self.unit if unit.type == currUnit.opposite() and not unit.destroyed and self.anyAdjacentSquares(unit)]
        

class UnitType(Enum):
    ELF = 0,
    GOBLIN = 1

    def __repr__(self):
        if self.value == UnitType.ELF:
            return 'E'
        else:
            return 'G'

class Position():
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def distance(self,pos2):
        '''
        Not quite right - this is the direct distance
        Need to take into account blockers such as walls and other units
        '''
        dist = abs(self.x - pos2.x) + abs(self.y - pos2.y)
        return dist

    def adjancent(self):
        if self.y >= 1: 
            adjacent_up = Position(self.x,self.y-1)
        else:
            adjacent_up = None

        if self.y < Area.rows - 1:
            adjacent_down = Position(self.x,self.y+1)
        else:
            adjacent_down = None

        if self.x > 0:
            adjacent_left = Position(self.x-1,self.y)
        else:
            adjacent_left = None

        if self.x < Area.cols - 1:
            adjacent_right = Position(self.x+1,self.y)
        else:
            adjacent_right = None

        return(adjacent_up,adjacent_right,adjacent_down,adjacent_left)

class Unit():
    def __init__(self,position,type):
        self.position = position
        self.type = type
        self.destroyed = False

    def opposite(self):
        if self.type == UnitType.ELF:
            return UnitType.GOBLIN
        else
            return UnitType.ELF

    def __repr__(self):
        return str(self.type)

class Units():
    def __init__(self):
        self.units = []

    def add(self,unit):
        self.units.append(unit)

# solve puzzle
area = Area()
area.build("inputfiles/day15.txt")
print(area)