import pytest
from Password import Password

test_data = {
        (111111,True),
        (223450,False),
        (123789,False),
        (223456,True),
        (112232,False)
    }

@pytest.mark.parametrize("code,expected",test_data)
def test_valid_password(code,expected):
    assert(Password(code).valid() == expected)

test_data2 = {
        (111111,False),
        (223450,False),
        (123789,False),
        (223456,True),
        (111122,True),
        (112233,True),
        (333566,True)
    }

@pytest.mark.parametrize("code,expected",test_data2)
def test_valid_password2(code,expected):
    assert(Password(code).valid2() == expected)