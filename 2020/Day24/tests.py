import pytest
from HexGrid import HexGrid

test_data = [("test1.txt",10)]

@pytest.mark.parametrize("input_file,black_tiles",test_data)
def test_process(input_file,black_tiles):
    grid=HexGrid(input_file)
    assert(grid.process() == black_tiles)