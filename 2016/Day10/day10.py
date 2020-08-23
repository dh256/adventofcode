from Factory import Factory

file_name = "input.txt"
compare_chips = (61,17)

factory = Factory(file_name)
output = factory.run(compare_chips)
print(f'Bot Number: {output[0]}')
print(f'Values: {output[1]}')