class Day10:
    def __init__(self, file_name):
        with open(file_name, 'r') as input_file:
            line = input_file.readline().strip('\n')
        
        # part 1 lengths
        self._lengths_part1: list[int] = [int(num) for num in line.split(',')]
        
        # part 2 lengths
        self._lengths_part2: list[int] = [ord(c) for c in line]
        self._lengths_part2 += [int(num) for num in '17,31,73,47,23'.split(',')]
        
    def part1(self,list_size=256) -> int:
        sparse = self.sparse(1,self._lengths_part1,list_size)
        return sparse[0] * sparse[1]
    
    def sparse(self,rounds: int, lengths: list[int], list_size:int=256) -> list[int]:
        num_list: list[int] = [x for x in range(0,list_size)]
        curr_pos: int = 0
        skip_size: int = 0
        
        for _ in range(0,rounds):
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
        
    
    def part2(self) -> str:
        sparse_hash: list[int] = self.sparse(64,self._lengths_part2)
        dense_hash: list[int] = [self.x_or_list(sparse_hash[16*block:16*(block+1)]) for block in range(0,16)]
        return self.knot_hash(dense_hash)
    
    def knot_hash(self,dense_hash: list[int]) -> str:
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