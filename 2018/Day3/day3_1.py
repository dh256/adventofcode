
class Rectangle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

class Claim:
    def __init__(self, elf, rect):
        self.elf = elf
        self.rect = rect

def overlap(grid, claim):
    #PART2: for each elf - look at their claims. Any claimed cells with more than elf means an overlap 
    for x in range(claim.rect.x, claim.rect.x + claim.rect.width):
        for y in range(claim.rect.y, claim.rect.y + claim.rect.height):
            if len(grid[(x,y)]) > 1:
                return True    
    return False


def processLine(line):
    """
    1st part: Knock off the hash and get elf number
    2nd part: @ symbol ignore
    3rd part: Knock off trailing : and split on , to get x,y coord
    4th part: split on x to get x,y size
    Note: could do above with RegExp?
    """
    line = line.rstrip('\n')
    parts = line.split(' ')
    elf = int(parts[0][1:])

    loc = parts[2].split(":")[0].split(",")
    x = int(loc[0])
    y = int(loc[1])

    size = parts[3].split("x")
    width = int(size[0])
    height = int(size[1])

    rect = Rectangle(x,y,width,height)
    claim = Claim(elf, rect)
    return claim

def processFile(fileName):
    with open(fileName, "r") as input:
        claims = [processLine(line) for line in input]
        return claims

def fillGrid(): 
    #use a dictionary where key is the coord of a grid cell and value is a list of elf ids who have a claim on grid cell
    grid = {}
    for claim in claims:
        for x in range(claim.rect.x, claim.rect.x + claim.rect.width):
            for y in range(claim.rect.y, claim.rect.y + claim.rect.height):
                if (x,y) in grid:
                    #elf already claimed cell, append to list
                    grid[(x,y)].append(claim.elf)
                else:
                    #no elf has a claim add new list
                    grid[(x,y)] = [claim.elf]
    return grid

def part1():
    #PART 1: Multiple Occupancy cells are all those with more than one entry in list
    multOcc = 0
    for coord, cell in grid.items():
        if len(cell) > 1: multOcc += 1
    print("Multiple Occupancy: ", multOcc)

def part2():
    #PART2: for each elf - look at their claims. If there are any cells with more than elf then have an overlap
    for claim in claims:
        if not overlap(grid, claim): 
            print(claim.elf," no overlap")

#run the puzzle
claims = processFile("day3.txt")
grid = fillGrid()
part1()
part2()






