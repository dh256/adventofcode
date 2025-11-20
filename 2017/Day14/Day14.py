from Point import Point
from collections import deque
class Day14:

    def __init__(self, key: str) -> None:
        self._key = key
        self._squares: set[Point] = set()
    
    def sparse(self,lengths: list[int]) -> list[int]:
        curr_pos: int = 0
        skip_size: int = 0
        list_size: int = 256
        num_list: list[int] = [x for x in range(0,list_size)]
        
        for _ in range(0,64):
            for len in lengths:
                # get portion of list to reverse
                reverse_nums: list[int] = list()
                for pos in range(0,len):
                    reverse_nums.append(num_list[(curr_pos+pos) % list_size])
                
                # reverse
                reverse_nums.reverse()
                
                # put reversed numbers back into list
                for pos in range(0,len):
                    num_list[(curr_pos+pos) % list_size] = reverse_nums[pos]  
                
                # calculate new curr_pos and skip_size
                curr_pos += len + skip_size
                skip_size += 1
        
        return num_list
    
    def knot_hash(self, hash: str) -> str:
        lengths = [ord(c) for c in hash] + [17,31,73,47,23]
        sparse_hash: list[int] = self.sparse(lengths)
        dense_hash: list[int] = [self.x_or_list(sparse_hash[16*block:16*(block+1)]) for block in range(0,16)]
        knot_hash: str = str()
        for num in dense_hash:
            if num < 16:
                knot_hash += f'0{hex(num)[2:]}'
            else:
                knot_hash += f'{hex(num)[2:]}'
        return knot_hash
    
    def x_or_list(self,num_list: list[int]) -> int:
        x_or: int = num_list[0]
        for i in range(1,len(num_list)):
            x_or ^= num_list[i]
        return x_or
    
    def part1(self) -> int:
        grid: list[str] = [f'{int(self.knot_hash(self._key + '-' + f'{row}'),16):0>128b}' for row in range(128)]
        
        # create a set of all points in grid with a square
        # this will help with Part 2
        for x in range(128):
            for y in range(128):
                if grid[y][x] == '1':
                    self._squares.add(Point(x,y))
        
        return len(self._squares)
        
    def part2(self) -> int:
        regions: int = 0
        
        while len(self._squares) > 0:
            '''
            Take any square from remaining squares
            Do a BFS of all neighbours until no neighbours remain, removing any squares visited from available squares
            When BFS completes region done
            Repeat until no squares remain
            '''
            stack: deque[Point] = deque()
            stack.appendleft(self._squares.pop())
            while len(stack) > 0:
                next_square: Point = stack.popleft()
                for n in next_square.neighbours():
                    if n in self._squares:
                        stack.appendleft(n) 
                        self._squares.discard(n)
            regions += 1
        
        return regions