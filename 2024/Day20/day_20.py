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

For part 2, initially changed Part 1 to do a BFS for all possible points a maximim of 2 steps from current point (repeat for all points on shortest path)
Then, changed 2 to 20 for Part 2 and it worked. A bit slow and could do with some optimisation. Definitelty checking too many points.
               
'''
from Day20 import Day20
from time import time
      
                            
def main():
    start_time = time()
    d = Day20('input.txt')
    p1, p2 = d.solution(100)
    print(f'Part 1: {p1}')
    print(f'Part 2: {p2}') 
    print(f'Excution Time: {(time()-start_time):.3f} s')

if __name__ == '__main__':
    main()
            