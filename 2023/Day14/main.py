'''
Part 1: Complete - but it's going to be too slow - must be another method

Part 2: Added code to do W, E, S tilts but too slow to run 1000000000 times.
Noticed during testing that after a few runs, a repeating pattern of 7 numbers stars to emerge.
Same thing happenned with real input. Summised it must be one of the repeating 7 numbers.
Not sure why this happens though.
'''

from Rocks import Rocks
import time
    

def main():
    rocks = Rocks('input.txt')
    start_time = time.time()
    print(f'Part 1: {rocks.part1()}')
    print(f'Execution Time: {time.time() - start_time}')

if __name__ == '__main__':
    main()
            