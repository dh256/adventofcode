from Encryption import Encryption

card_public_key = 10441485
door_public_key = 1004920

door_loop_size = Encryption.calc_loop_size(door_public_key)
encryption_key = Encryption.calc_private_key(card_public_key,door_loop_size)
print(f'Encryption Key from card: {encryption_key}')
