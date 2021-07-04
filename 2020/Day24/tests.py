import pytest
from HexGrid import HexGrid

test_data1 = [("test1.txt",10)]
test_data2 = [("test1.txt",1,15),("test1.txt",2,12),("test1.txt",50,566),("test1.txt",100,2208)]

@pytest.mark.parametrize("input_file,black_tiles",test_data1)
def test_process_instructions(input_file,black_tiles):
    grid=HexGrid(input_file)
    grid.process_instructions()
    assert(grid.black_tiles == black_tiles)

@pytest.mark.parametrize("input_file,days,black_tiles",test_data2)
def test_flip_tiles(input_file,days,black_tiles):
    grid=HexGrid(input_file)
    grid.process_instructions()
    grid.flip_tiles(days)
    assert(grid.black_tiles == black_tiles)
