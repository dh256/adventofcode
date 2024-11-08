'''
First attempt failed. Got stuck with 320 instructions not processed.
Need a different approach:
- Find instruction that sets destination wire 'a' (there is only one)
- If instruction results in an actual value stop and return
- If not, recursively find next instruction that sets the value of inputs for that instruction
- Eventually will get a value  

def find_signal(wire):
    Find instructions that sets signal for wire:
        Can instruction provide a signal i.e. do all its inputs have a value set?
        If yes return value
        If no pass each wire with no signal into find_signal(wire)
    
    To make this work probably need to have a global table of signal values for wires
'''



from Day7 import Day7

def main():
    day7 = Day7('input.txt')
    print(f'Part 1: {day7.part1('a')}')
    print(f'Part 2: {day7.part2('a')}')
    

if __name__ == '__main__':
    main()