 
''' 
David Hanley, December 2024
            
First approach was to remove walls one at a time and determine impact on shortest path.
This seemed to work for the test data set was way too slow and gave wrong answer

Read problem statement again 
Key point is that after second move, program MUST be back on track again 
This means that removing all walls (one at a time) is not way to do this.
Can "walk through" a wall only if it after walking through wall brings you back to shortest path.

What do we need:
- Points on shortest path
- For each point on shortest path - actual time from start

With this can walk through walls but only if they are adjacent to two points on shortest path
After removal, can work out distance save by subtracting time from point on one side of wall from the other.

This avoids the need to do repeated BFS.
                
'''
from Day20 import Day20
from time import time
      
                            
def main():
    #d = Day20('tests/test1.txt')
    d = Day20('input.txt')
    start_time = time()
    print(f'Part 1: {d.part1()}; Excution Time: {(time()-start_time):.3f} s')
    #start_time = time()
    #print(f'Part 2: {d.part2()}; Excution Time: {(time()-start_time):.3f} s')

if __name__ == '__main__':
    main()
            