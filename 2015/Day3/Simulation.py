from Point2D import Point2D

class Simulation:
    def __init__(self, filename: str):
         with open(filename, "r") as data:
            self.directions = data.read().strip('\n')
            
    def run(self,part=1) -> int:
        self.presents: dict[Point2D, int] = {}
        santa_curr_pos = Point2D(0,0)
        robot_curr_pos = Point2D(0,0)
        self.presents[Point2D(0,0)] = part
        for index, direction in enumerate(self.directions, start=0):    
            if part == 1 or (part == 2 and index % 2 == 0):
                santa_curr_pos = santa_curr_pos.move(direction)
                self.presents[santa_curr_pos] = self.presents.get(santa_curr_pos,0) + 1
            else:
                robot_curr_pos = robot_curr_pos.move(direction)
                self.presents[robot_curr_pos] = self.presents.get(robot_curr_pos,0) + 1
                
        return len(list(filter(lambda x : x >= 1, self.presents.values())))
        

        