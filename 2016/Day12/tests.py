import pytest 
from Computer import Computer

test_data = [("test1.txt",42)]

@pytest.mark.parametrize("filename,reg_a_value",test_data)
def test_execute_code(filename,reg_a_value):
    computer = Computer(filename)
    assert(computer.execute() == reg_a_value)
