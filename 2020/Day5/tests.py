import pytest
from BoardingPass import BoardingPass,BoardingPasses

test_data = [("test1.txt",70,7,567),("test2.txt",14,7,119),("test3.txt",102,4,820)]
test_data2 = [("test4.txt",820)]

@pytest.mark.parametrize("file_name,row,col,seat_id",test_data)
def test_boarding_pass(file_name,row,col,seat_id):
    passes = BoardingPasses(file_name)
    assert(passes.boarding_passes[0].row == row)
    assert(passes.boarding_passes[0].col == col)
    assert(passes.boarding_passes[0].seat_id == seat_id)

@pytest.mark.parametrize("file_name,seat_id",test_data2)
def test_highest_seat_idx(file_name,seat_id):
    passes = BoardingPasses(file_name)
    assert(passes.highest_seat_id() == seat_id)

