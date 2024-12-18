 
''' 
David Hanley, December 2024
'''
from Day18 import Day18
from time import time
                            
def main():
    #grid_width, grid_height, num_bytes = 7,7,12
    #d = Day18('tests/test1.txt',grid_width,grid_height,num_bytes)
    grid_width, grid_height, num_bytes = 71,71,1024
    start_time = time()
    d = Day18('input.txt',grid_width, grid_height)
    print(f'Part 1: {d.part1(num_bytes)}; Execution Time: {(time()-start_time):.3f} s')
    
    start_time = time()
    print(f'Part 2: {d.part2()}; Execution Time: {(time()-start_time):.3f} s')

if __name__ == '__main__':
    main()
            