import pytest
from Puzzle import Puzzle

test_data = [("test1.txt",7,3,6)]

@pytest.mark.parametrize("file_name,screen_width,screen_height,lit_pixels",test_data)
def test_run(file_name,screen_width,screen_height,lit_pixels):
    puzzle = Puzzle(file_name,screen_width=screen_width,screen_height=screen_height)
    assert(puzzle.run() == lit_pixels)