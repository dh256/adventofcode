from Mirrors import Mirrors
import pytest

# ('tests/input.txt',405)

test_data=[('tests/input1.txt',0),
           ('tests/input2.txt',100),
           ('tests/input3.txt',100),
           ('tests/input4.txt',200),
           ('tests/input5.txt',200),
           ('tests/input6.txt',0),
           ('tests/input7.txt',400),
           ('tests/input8.txt',1),
           ('tests/input9.txt',5)]

@pytest.mark.parametrize('file_name,result',test_data)
def test_part1(file_name, result):
    mirrors = Mirrors(file_name)
    assert(mirrors.part1() == result)

