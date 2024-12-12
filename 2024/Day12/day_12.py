 
''' 
David Hanley, December 2024
'''
from Day12 import Day12
from time import time
                            
def main():
    d = Day12('input.txt')
    start_time = time()
    p,s = d.solution()
    print(f'Part 1: {p}')
    print(f'Part 2: {s}')
    print(f'Excution Time: {(time()-start_time):.3f} s')
    
if __name__ == '__main__':
    main()
            