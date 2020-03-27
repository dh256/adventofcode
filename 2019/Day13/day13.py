# Computer.py is same code from 2019 Day 9
from Computer import Computer, StopReason

with open("input.txt","r") as program_data:
    program = program_data.readline().strip('\n')
    
    '''
    # PART 1
    computer = Computer(program,[1])
    output = computer.run_program()
    print(output[0])

    # look at every 3rd entry in output list and count all those with a value of 2
    i=1
    block_tiles=0
    for n in output[0]:
        if i % 3 == 0 and n == 2:
            block_tiles += 1
        i += 1
    
    print(f'Block Tiles: {block_tiles}')
    '''

    # PART 2
    computer = Computer(program,[0])
    computer.memory_write(0,2)
    output = computer.run_program()
    print(output[0])