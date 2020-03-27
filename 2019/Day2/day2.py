from Computer import Computer

filename = "input.txt"
with open(filename,"r") as file_in:
    program = file_in.readline().strip('\n')
    computer = Computer(program)
    computer.initialise_memory((12,2))
    computer.run_program()
    print(f'Answer: {computer.memory[0]}')

    ''' PART 2 '''
    for noun in range(1, 100):
        for verb in range(1, 100):
            # Need to reset computer memory to initial state before each run
            computer = Computer(program)
            computer.initialise_memory((noun,verb))
            computer.run_program()
            if computer.memory[0] == 19690720:
                print(f"Noun = {noun}; Verb = {verb}. Answer = {100 * noun + verb}")
                break
            