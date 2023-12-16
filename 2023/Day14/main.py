'''
Part 1: Complete - but it's going to be too slow - must be another method
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
            