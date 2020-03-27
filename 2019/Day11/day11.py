from Computer import Computer, StopReason
from Point2D import Point2D

with open("input.txt","r") as program_data:
    program = program_data.readline().strip('\n')
    
    grid = dict()
    startPoint = Point2D(0,0)
    direction = 

    # PART 1
    computer = Computer(program,[0])
    output = computer.run_program()
    print(output[0])