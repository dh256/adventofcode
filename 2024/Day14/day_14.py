 
''' 
David Hanley, December 2024
'''
from Day14 import Day14
from time import time
                            
def main():
    width = 101
    height = 103
    d = Day14('input.txt',width,height)
    start_time = time()
    print(f'Part 1: {d.part1()}; Excution Time: {(time()-start_time):.3f} s')
    
    # reset robots
    d = Day14('input.txt',width,height)
    start_time = time()
    print(f'Part 2: {d.part2()}; Excution Time: {(time()-start_time):.3f} s')

if __name__ == '__main__':
    main()
            