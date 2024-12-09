 
''' 
David Hanley, December 2024
'''
from Day8 import Day8
from time import time
                            
def main():
    d = Day8('input.txt')
    start_time = time()
    print(f'Part 1: {d.part1()}')
    print(f'Execution Time: {(time()-start_time):.3f}')

    start_time = time()
    print(f'Part 2: {d.part2()}')
    print(f'Execution Time: {(time()-start_time):.3f}')

if __name__ == '__main__':
    main()
            