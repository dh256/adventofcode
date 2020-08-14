import pytest
from Door import Door

def test_find_password():
    door_id = "abc"
    door = Door(door_id)
    assert(door.find_password() == "18f47a30")

def test_find_password2():
    door_id = "abc"
    door = Door(door_id)
    assert(door.find_password2() == "05ace8e3")