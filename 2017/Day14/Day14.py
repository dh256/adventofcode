class Day14:

    def __init__(self, key: str) -> None:
        self._key = key
    
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
        squares: int = 0
        for row in grid:
            for c in row:
                if c == '1':
                    squares += 1
        
        return squares
        
    def part2(self) -> int:
        pass