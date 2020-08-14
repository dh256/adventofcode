from Signal import Signal

signal = Signal("input.txt")
print(f'Part 1: {signal.get_repeating_message()}')
print(f'Part 2: {signal.get_repeating_message(False)}')
