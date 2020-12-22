from FerrySeats import FerrySeats

ferry_seats = FerrySeats("test1.txt")
occ_seats = ferry_seats.calculate_occupied_seats(mode=FerrySeats.ADJACENT_MODE)
print(f'Part 1: {occ_seats}')

ferry_seats2 = FerrySeats("input.txt")
occ_seats2 = ferry_seats2.calculate_occupied_seats(mode=FerrySeats.VISIBLE_MODE)
print(f'Part 2: {occ_seats2}')
