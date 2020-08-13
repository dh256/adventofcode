from Rooms import Rooms

rooms = Rooms("input.txt")

# Part 1
print(f'Valid Rooms Sector Id Sum = {rooms.sector_id_sum()}')

# Part 2
decrypted_rooms = rooms.decrypt_room_names()
for dr in decrypted_rooms:
    if dr[0] == "northpole object storage":
        print(f'Sector Id of North Pole Object Storage = {dr[1]}')

