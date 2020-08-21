from File import File

my_file = File("input.txt")

# Part 1
decom_file = my_file.decompress()
print(decom_file)
print(f'Decompressed Length = {len(decom_file)}')

# Part2 
print(f'Decompressed Length = {my_file.decompress2()}')