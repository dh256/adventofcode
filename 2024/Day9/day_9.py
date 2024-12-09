 
''' 
David Hanley, December 2024
'''
from Day9 import Day9
import time

                            
def main():
    start_time = time.time()
    d = Day9('input.txt')
    print(f'Part 1: {d.part1()}')
    print(f'Execution Time: {(time.time() - start_time):.3f}')
    
    # need to reset disk for Part 2
    start_time = time.time()
    d = Day9('input.txt')
    print(f'Part 2: {d.part2()}')
    print(f'Execution Time: {(time.time() - start_time):.3f}')

if __name__ == '__main__':
    main()
            