from Computer import Computer

computer = Computer("input.txt")

# Part 1
reg_a_value = computer.execute()
print(reg_a_value)

# Part 2
computer.reset()
computer.set_register('c',1)
reg_a_value = computer.execute()
print(reg_a_value)