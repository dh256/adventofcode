import pytest
from Computer import Computer

test_data = {('1,0,0,0,99',0,2),('2,3,0,3,99',3,6),('2,4,4,5,99,0',5,9801),('1,1,1,4,99,5,6,0,99',0,30)}

@pytest.mark.parametrize("program,address,expected_value", test_data)
def test_int_list(program,address,expected_value):
    computer = Computer(program)
    computer.initialise_memory()
    computer.run_program()
    assert(computer.memory[address] == expected_value)