from enum import IntEnum

class Headings(IntEnum):
    NORTH=0
    EAST=1
    SOUTH=2
    WEST=3


class Directions:
    def __init__(self, file_name):
        with open(file_name,"r") as input_file:
            diretion_str = input_file.readline()
            self.directions = diretion_str.split(', ') 

    '''
    Returns distance (blocks) to Easter Bunny HQ
    '''
    def easter_bunny_hq(self,part2=False):
        locations_visited = [(0,0)]
        locations_visited_twice_found = False
        heading = Headings.NORTH         
        northing = 0
        easting = 0
        for direction in self.directions:
            turn = direction[0]
            move = int(direction[1:])
            if turn == "R":
                heading = (heading + 1) % 4
            else: 
                heading = (heading - 1) % 4

            for _ in range(0,move):
                if heading == Headings.NORTH:
                    northing += 1
                elif heading == Headings.SOUTH:
                    northing -= 1
                elif heading == Headings.EAST:
                    easting += 1
                elif heading == Headings.WEST:
                    easting -= 1

                if part2:
                    if (northing,easting) in locations_visited:
                        locations_visited_twice_found = True
                        break
                    else:
                        locations_visited.append((northing,easting))
            
            if locations_visited_twice_found:
                break

        return abs(easting) + abs(northing)