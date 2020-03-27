from Point2D import Point2D

class Simulation:
    NORTH = "^"
    SOUTH = "v"
    EAST = ">"
    WEST = "<"

    def __init__(self, filename, start_pos=Point2D(0,0)):
         with open(filename, "r") as data:
            self.directions = data.read().strip('\n')
            self.start_pos = start_pos
            self.houses_visited = {start_pos: 1}

    def run(self):
        curr_pos = self.start_pos
        for direction in self.directions:
            if direction == Simulation.NORTH:
                curr_pos.y += 1

            elif direction == Simulation.SOUTH:
                curr_pos.y -= 1

            elif direction == Simulation.EAST:
                curr_pos.x += 1

            elif direction == Simulation.WEST:
                curr_pos.x -= 1

            else:
                raise("Invalid input")

            if curr_pos in self.houses_visited:
                self.houses_visited[curr_pos] = self.houses_visited[curr_pos] + 1
            else:
                self.houses_visited[curr_pos] = 1
            
    def houses_visited_more_than(self, num):
        return len(list(filter(lambda x : x > num, self.houses_visited.values())))
