'''
David Hanley, Dec 2019
See: https://adventofcode.com/2019/day/5
'''
from Computer import Computer

filename = "input.txt"
with open(filename,"r") as file_in:
    program = file_in.readline().strip('\n')
    computer = Computer(program)
    computer.run_program()
