with open("input.txt", "r") as data_in:
    instructions = data_in.read().strip('\n')



position = 1
been_to_basement = False
floor = 0
for instruction in instructions:
    if instruction == '(':
        floor += 1
    elif instruction == ')':
        floor -= 1

    # PART 2
    if not been_to_basement and floor == -1:
        been_to_basement = True
        print(f"First got to basement at position {position}")

    position += 1

# PART 1
print(f'Finishing floor {floor}')

