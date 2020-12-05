from BoardingPass import BoardingPass, BoardingPasses

boarding_passes = BoardingPasses("input.txt")
highest_seat_id = boarding_passes.highest_seat_id()
print(highest_seat_id)

# print out a list of empty seats and their ids
my_seat_id = boarding_passes.find_my_seat()
print(my_seat_id)