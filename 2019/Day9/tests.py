import pytest
from Computer import Computer

def test_run1():
    with open("test1.txt","r") as program_data:
        program = program_data.readline().strip('\n')
        computer = Computer(program,[0])
        output = computer.run_program()
        out_str = ""
        for output_val in output[0]:
            out_str += f'{output_val},'
        out_str = out_str[:-1]
        assert(out_str == program)

def test_run2():
    with open("test2.txt","r") as program_data:
        program = program_data.readline().strip('\n')
        computer = Computer(program,[0,1])
        output = computer.run_program()
        assert(len(f'{output[0][0]}') == 16)

def test_run3():
    with open("test3.txt","r") as program_data:
        program = program_data.readline().strip('\n')
        computer = Computer(program,[0,1])
        output = computer.run_program()
        assert(output[0] == [1125899906842624])
