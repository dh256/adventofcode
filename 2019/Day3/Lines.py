class Instruction:
    def __init__(self,direction,points):
        self.direction = direction
        self.points = points

    def __repr__(self):
        return f'{self.direction}{self.points}'

class Line:
    def __init__(self,str):
        self.instructions = []
        instructions = str.split(',')
        for instruction in instructions:
            direction = instruction[0]
            points = int(instruction[1:])   
            self.instructions.append(Instruction(direction,points))       
    
class Lines:
    def __init__(self,filename):
        with open(filename,"r") as lines_data:
            self.lines = [Line(line.strip('\n')) for line in lines_data]

