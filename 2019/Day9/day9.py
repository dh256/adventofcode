from Computer import Computer, StopReason

with open("input.txt","r") as program_data:
    program = program_data.readline().strip('\n')
    
    # PART 1
    computer = Computer(program,[1])
    output = computer.run_program()
    print(output[0])
    
    # PART 2
    computer = Computer(program,[2])
    output = computer.run_program()
    print(output[0])
    