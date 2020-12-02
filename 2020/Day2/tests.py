from Passwords import Passwords
from Passwords import Passwords
import pytest

test_data_p1 = [("test.txt",2)]
test_data_p2 = [("test.txt",1)]

@pytest.mark.parametrize("input_file,valid",test_data_p1)
def test_num_valid1(input_file,valid):
    passwords = Passwords(input_file)
    assert(passwords.num_valid_part1() == valid)

@pytest.mark.parametrize("input_file,valid",test_data_p2)
def test_num_valid2(input_file,valid):
    passwords = Passwords(input_file)
    assert(passwords.num_valid_part2() == valid)