
''' 
David Hanley, December 2024
'''
import re

class Day9:
    def __init__(self,file_name:str) -> None:
        with open(file_name, 'r') as input_file:
            disk_map = input_file.read()
        
        self.disk: list[str | int] = list()
        self.file_blocks: dict[int, tuple[int,int]] = dict()  # useful for Part 2, holds start index and length of of each file block
        disk_index: int = 0
        for map_index, c in enumerate(disk_map):
            file_block: bool = map_index % 2 == 0
            if file_block:
                append = map_index // 2
                file_block_start = disk_index
            else:
                append = '.'
    
            # fill disk
            for _ in range(0,int(c)):
                self.disk.append(append)
                disk_index += 1
                    
            if file_block:
                self.file_blocks[append] = (file_block_start,disk_index-file_block_start)
    
    def part1(self) -> int:
        # rearrange disk
        file_block_index: int = len(self.disk)-1
        free_space_index: int = 0
        
        while True: 
            # find next free space block
            while self.disk[free_space_index] != '.':
                free_space_index += 1
            
            # find next file block
            while type(self.disk[file_block_index]) != int:
                file_block_index -= 1
            
            # if haven't overlapped, swap; otherwise done
            if free_space_index < file_block_index:
                # swap
                self.disk[free_space_index] = self.disk[file_block_index]
                self.disk[file_block_index] = '.'
            else: 
                break
        
        # checksum        
        return sum(map(lambda e: e[0] * e[1] if type(e[1]) is int else 0, enumerate(self.disk)))    

    def swap(self,file_block_start: int,file_block_length: int,disk_str: str) -> str:
        '''
        Swaps current file_block if there's a free space large enough for it
        Use string representation of disk to search for blocks of free space large enough
        Return updated string representation of disk
        '''
        # find first block of free space big enough to hold file block
        re_str: str = '\\.{' + f'{file_block_length}' + ',}'
        match = re.search(rf'{re_str}',disk_str[0:file_block_start])
        if match:
            # swap if a match found
            for index in range(0,file_block_length):
                # swap on disk
                self.disk[match.start()+index] = self.disk[file_block_start+index]
                self.disk[file_block_start+index] = '.'
                
            # swap in disk_str
            disk_str = disk_str[0:match.start()] + 'F'*file_block_length + disk_str[match.start() + file_block_length:file_block_start] + '.'*file_block_length + disk_str[file_block_start+file_block_length:] 

        return disk_str

    def part2(self) -> int:
        '''
        Use a string representation of disk to quickly find blocks of free space. A . represents free space and a F represents a file block.
        Use information from file_blocks dict (created in __init__) to get start indexes and lengths of each file block
        Once swaps complete return checksum
        '''
        disk_str: str = ''.join(map(lambda d: 'F' if type(d) is int else d, self.disk)) 
        for file_id in range(max(self.file_blocks.keys()),-1,-1):
            disk_str = self.swap(self.file_blocks[file_id][0],self.file_blocks[file_id][1],disk_str)
            
        # checksum        
        return sum(map(lambda e: e[0] * e[1] if type(e[1]) is int else 0, enumerate(self.disk)))        
