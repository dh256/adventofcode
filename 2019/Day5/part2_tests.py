# Set of manual tests
from Computer import Computer

test_data = [
    #"3,9,8,9,10,9,4,9,99,-1,8",   # output 1 if input is 8, else 0
    #"3,9,7,9,10,9,4,9,99,-1,8",   # output 1 if input < 8, else 0
    #"3,3,1108,-1,8,3,4,3,99",     # output 1 if input is 8, else 0
    #"3,3,1107,-1,8,3,4,3,99",    # output 1 if input < 8, else 0
    "3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9",  # output 0 if input is 0, else 1
    "3,3,1105,-1,9,1101,0,0,12,4,12,99,1" # output 0 if input is 0, else 1
]

for program in test_data:    
    computer = Computer(program)
    computer.run_program()
    