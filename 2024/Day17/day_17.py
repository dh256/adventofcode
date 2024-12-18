 
''' 
David Hanley, December 2024
'''
from Day17 import Day17
from time import time
                            
def main():
    #d = Day17('tests/test1.txt')
    d = Day17('input.txt')
    start_time = time()
    print(f'Part 1: {d.part1()}; Excution Time: {(time()-start_time):.3f} s')
    
    #d = Day17('tests/test1.txt')
    #start_time = time()
    #print(f'Part 2: {d.part2()}; Excution Time: {(time()-start_time):.3f} s')

if __name__ == '__main__':
    main()
            