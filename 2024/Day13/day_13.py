 
''' 
David Hanley, December 2024
'''
from Day13 import Day13
from time import time
                            
def main():
    d = Day13('input.txt')
    start_time = time()
    print(f'Part 1: {d.solution(1)}; Excution Time: {(time()-start_time):.3f} s')
    start_time = time()
    print(f'Part 1: {d.solution(2)}; Excution Time: {(time()-start_time):.3f} s')
 
if __name__ == '__main__':
    main()
            