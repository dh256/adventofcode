from Bathroom import Bathroom

bathroom = Bathroom("input.txt")
keycode1 = bathroom.get_keycode(True)
print(f'Part 1 keycode = {keycode1}')

keycode2 = bathroom.get_keycode(False)
print(f'Part 2 keycode = {keycode2}')