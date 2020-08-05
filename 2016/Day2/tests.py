import pytest
from Bathroom import Bathroom

test_data = [("test1.txt",True,"1985"),("test1.txt",False,"5DB3")]

@pytest.mark.parametrize("file,part1,expected_keycode",test_data)
def test_get_keycode(file,part1,expected_keycode):
    bathroom = Bathroom(file)
    keycode = bathroom.get_keycode(part1)
    assert(keycode == expected_keycode)

