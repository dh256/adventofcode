from CPU import CPU

cpu = CPU('input.txt')
print(f'{cpu.process()}')

# reload machine instructions - they were changed above
cpu = CPU('input.txt')
print(f'{cpu.process2()}')
