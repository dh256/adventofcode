from Door import Door

door_id = "ugkcyxxp"
door = Door(door_id)

# Part1
password = door.find_password()
print(f'Part 1 Password = {password}')

password = door.find_password2()
print(f'Part 2 Password = {password}')