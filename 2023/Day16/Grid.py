from collections import deque
from dataclasses import dataclass
from Point import Point

@dataclass
class Beam:
    pos: Point
    direction: str

class Grid:
    offsets = {'N': (0,-1),'S': (0,1), 'E': (1,0), 'W': (-1,0)}
    
    def __init__(self, file_name: str) -> None:
        with open(file_name, 'r') as input_file:
            self.grid_rows = [[*line.strip('\n')] for line in input_file]
            self.grid_cols = list(map(list, zip(*self.grid_rows)))
        
        self.rows: list[str] = []
        self.cols: list[str] = []
        self.energised: set[Point] = set()
        self.obs_visited: set[tuple[Point, str]] = set()
        self.width = len(self.grid_cols)
        self.height = len(self.grid_rows)

    def next_obstacle(self,beam: Beam) -> tuple[str, Point]:
        next_obstacle = None
        if beam.direction in ('E','W'):
            if beam.direction == 'E':
                r = range(beam.pos.x,self.width)
            else:
                r = range(beam.pos.x,-1,-1)
            
            for i in r:
                if self.grid_rows[beam.pos.y][i] in ['|','-','\\','/']:
                    next_obstacle = (self.grid_rows[beam.pos.y][i],Point(i, beam.pos.y))
                    break
            else:
                # no next obstacle
                next_obstacle = (None,Point(i,beam.pos.y))
                
        else: 
            if beam.direction == 'N':
                r = range(beam.pos.y,-1,-1)
            else:
                r = range(beam.pos.y,self.height)

            for i in r:
                if self.grid_cols[beam.pos.x][i] in ['|','-','\\','/']:
                    next_obstacle = (self.grid_cols[beam.pos.x][i],Point(beam.pos.x,i))
                    break
            else:
                # no next obstacle
                next_obstacle = (None,Point(beam.pos.x,i))

        return next_obstacle

    def energise_points(self,beam,obstacle) -> None:
        if beam.direction in ('E','W'):
            y_start = beam.pos.y
            y_end = beam.pos.y + 1
            y_inc = 1
            x_start = beam.pos.x
            if beam.direction == 'E':
                x_end = obstacle[1].x+1
                x_inc = 1
            else:   
                x_end = obstacle[1].x-1
                x_inc = -1
        elif beam.direction in ('S','N'):
            x_start = beam.pos.x
            x_end = beam.pos.x + 1
            x_inc = 1
            y_start = beam.pos.y
            if beam.direction == 'S':
                y_end = obstacle[1].y+1
                y_inc = 1
            else:
                y_end = obstacle[1].y-1
                y_inc = -1

        for x in range(x_start,x_end,x_inc):
            for y in range(y_start,y_end,y_inc):
                self.energised.add(Point(x,y))


    def process_obstacle(self, beam: Beam, obstacle) -> [Beam]:
        # check if obstacle already visited
        beams: list[Beam] = []
        if not (obstacle[1],beam.direction) in self.obs_visited:
            self.obs_visited.add((obstacle[1],beam.direction))
            if obstacle[0] == '|':
                if beam.direction in ('N', 'S'):
                    if beam.direction == 'N' and obstacle[1].y > 0:
                        beams.append(Beam(obstacle[1].offset(Grid.offsets['N']),'N'))
                    elif beam.direction == 'S' and obstacle[1].y < self.height-1:
                        beams.append(Beam(obstacle[1].offset(Grid.offsets['S']),'S'))
                else:
                    if obstacle[1].y > 0:
                        beams.append(Beam(obstacle[1].offset(Grid.offsets['N']),'N'))
                    
                    if obstacle[1].y < self.height-1:
                        beams.append(Beam(obstacle[1].offset(Grid.offsets['S']),'S'))

            elif obstacle[0] == '-':
                if beam.direction in ('E', 'W'):
                    if beam.direction == 'E' and obstacle[1].x < self.width-1:
                        beams.append(Beam(obstacle[1].offset(Grid.offsets['E']),'E'))
                    elif beam.direction == 'W' and obstacle[1].x > 0:
                        beams.append(Beam(obstacle[1].offset(Grid.offsets['W']),'W'))
                else:
                    if obstacle[1].x < self.width-1:
                        beams.append(Beam(obstacle[1].offset(Grid.offsets['E']),'E'))
                    
                    if obstacle[1].x > 0:
                        beams.append(Beam(obstacle[1].offset(Grid.offsets['W']),'W'))
                
            elif obstacle[0] == '/':
                if beam.direction == 'E':
                    if obstacle[1].y > 0:
                        beams.append(Beam(obstacle[1].offset(Grid.offsets['N']),'N'))
                elif beam.direction == 'W':
                    if obstacle[1].y < self.height-1:
                        beams.append(Beam(obstacle[1].offset(Grid.offsets['S']),'S'))
                elif beam.direction == 'N':
                    if obstacle[1].x < self.width-1:
                        beams.append(Beam(obstacle[1].offset(Grid.offsets['E']),'E'))
                elif beam.direction == 'S':
                    if obstacle[1].x > 0:
                        beams.append(Beam(obstacle[1].offset(Grid.offsets['W']),'W'))
                
            elif obstacle[0] == '\\':
                if beam.direction == 'E':
                    if obstacle[1].y < self.height-1:
                        beams.append(Beam(obstacle[1].offset(Grid.offsets['S']),'S'))
                elif beam.direction == 'W':
                    if obstacle[1].y > 0:
                        beams.append(Beam(obstacle[1].offset(Grid.offsets['N']),'N'))
                elif beam.direction == 'N':
                    if obstacle[1].x > 0:
                        beams.append(Beam(obstacle[1].offset(Grid.offsets['W']),'W'))
                elif beam.direction == 'S':
                    if obstacle[1].x < self.width-1:
                        beams.append(Beam(obstacle[1].offset(Grid.offsets['E']),'E'))        
 
        return beams

    def part1(self,start_beam: Beam = Beam(Point(0,0),'E')) -> int:
        self.energised = set()
        self.obs_visited = set()
        q = deque()
        q.append(start_beam)
        while len(q) > 0:
            beam = q.pop()
            
            # find next obstacle
            next_obs = self.next_obstacle(beam)
            
            # energise all points between beam start and obstacle position
            self.energise_points(beam,next_obs)

            # process obstacle, pushing new beam(s) onto Q
            if next_obs[0]:
                for new_beam in self.process_obstacle(beam, next_obs):
                    q.append(new_beam)

        # count energised points
        return len(self.energised)  

    def part2(self) -> int:
        tiles: list[int] = []
        # top and bottom rows
        for x in range(self.width):     
            tiles.append(self.part1(Beam(Point(x,0),'S')))
            tiles.append(self.part1(Beam(Point(x,self.height-1),'N')))

        # left and rights col
        for y in range(self.height):
            tiles.append(self.part1(Beam(Point(self.width-1,y),'W')))
            tiles.append(self.part1(Beam(Point(0,y),'E')))

        return max(tiles)