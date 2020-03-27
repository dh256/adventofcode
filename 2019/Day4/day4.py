from Password import Password

start_range = 278384
end_range = 824795
valid_passwords1 = 0
valid_passwords2 = 0
for code in range(278384,824795+1):
    password = Password(code)
    if password.valid():
        valid_passwords1 += 1
    if password.valid2():
        valid_passwords2 += 1

print(f'Part 1: {valid_passwords1}')
print(f'Part 2: {valid_passwords2}')