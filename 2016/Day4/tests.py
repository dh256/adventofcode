import pytest
from Rooms import Rooms

test_data = [("test1.txt",1514)]
test_data2 = [("test2.txt","very encrypted name",343)]


@pytest.mark.parametrize("file,sector_id_sum",test_data)
def test_sector_id_sum(file,sector_id_sum):
    rooms = Rooms(file)
    assert(rooms.sector_id_sum() == sector_id_sum)

@pytest.mark.parametrize("file,decrypted_room_name,sector_id",test_data2)
def test_decrypt_room_name(file,decrypted_room_name,sector_id):
    rooms = Rooms(file)
    decrytped = rooms.decrypt_room_names()
    assert(decrytped[0][0] == decrypted_room_name and decrytped[0][1] == sector_id)

