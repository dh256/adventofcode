import pytest
from Day7 import Day7

test_data=[ ("tests/test1.txt","x",123),
            ("tests/test1.txt","y",456),
            ("tests/test1.txt","d",72),
            ("tests/test1.txt","e",507),
            ("tests/test1.txt","f",492),
            ("tests/test1.txt","g",114),
            ("tests/test1.txt","h",65412)]

@pytest.mark.parametrize('file_name,wire,value',test_data)
def test_part1(file_name: str,wire: str,value: int):
    day7 = Day7(file_name)
    assert(day7.part1(wire) == value)