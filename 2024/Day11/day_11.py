 
''' 
David Hanley, December 2024
'''
from Day11 import Day11
from time import time
                            
def main():
    d = Day11('5 89749 6061 43 867 1965860 0 206250')
    start_time = time()
    print(f'Part 1: {d.solution(25)}; Excution Time: {(time()-start_time):.3f} s')
    
    d = Day11('5 89749 6061 43 867 1965860 0 206250')
    start_time = time()
    print(f'Part 2: {d.solution(75)}; Excution Time: {(time()-start_time):.3f} s')

if __name__ == '__main__':
    main()
