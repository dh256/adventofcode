import pytest

from FerrySeats import FerrySeats

test_data = [("test1.txt",FerrySeats.ADJACENT_MODE,37),
            ("test1.txt",FerrySeats.VISIBLE_MODE,26)]

@pytest.mark.parametrize("file_name,mode,occ_seats",test_data)
def test_calculate_occupied_seats(file_name,mode,occ_seats):
    ferry_seats = FerrySeats(file_name)
    assert ferry_seats.calculate_occupied_seats(mode) == occ_seats
