import pytest
from Reactions import Reactions

test_data = [
    ("test1.txt",31),
    ("test2.txt",165),
    ("test3.txt",13312),
    ("test4.txt",180697),
    ("test5.txt",2210736)
]

@pytest.mark.parametrize("filename,ore",test_data)
def test_calculate_required_ore(filename,ore):
    reactions = Reactions(filename)
    req_ore = reactions.calculate_ore_required()
    assert(req_ore == ore)