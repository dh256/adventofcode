import pytest
from Encryption import Encryption

test_data1 = [(5764801,17807724,8,11,14897079)]

@pytest.mark.parametrize("card_public_key,door_public_key,card_loop_size,door_loop_size,encryption_key",test_data1)
def test_encryption(card_public_key,door_public_key,card_loop_size,door_loop_size,encryption_key):
    card_loop_size1 = Encryption.calc_loop_size(card_public_key)
    door_loop_size1 = Encryption.calc_loop_size(door_public_key)
    assert(card_loop_size == card_loop_size1)
    assert(door_loop_size == door_loop_size1)

    private_key = Encryption.calc_private_key(door_public_key,card_loop_size1)
    assert(private_key == encryption_key)
    assert(encryption_key == Encryption.calc_private_key(card_public_key,door_loop_size1))
    