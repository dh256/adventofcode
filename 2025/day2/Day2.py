class Day2:
    def __init__(self,file_name:str) -> None:
        with open(file_name, 'r') as input_file:
            self._product_ranges: list[str] = input_file.readline().strip('\n').split(',')
    
    def _invalid1(self,num: str) -> bool:
        '''
        Invalid if made _only_ of some sequence of digits repeated twice
        '''
        if len(num) % 2 == 1:
            return False
        else:
            divide_at: int = len(num) // 2
            return num[0:divide_at] == num[divide_at:]
    
    def _invalid2(self,num: str) -> bool:
        '''
        Invalid if made _only_ of a sequence of digits repeated at least twice
        '''
        for sequence_length in range (1,(len(num) // 2 + 1)):
            # get next sequence
            sequence: str = num[0:sequence_length]
            
            # if remaining num_str _only_ made up of blocks of "sequence" chars return True
            for block_start in range(sequence_length,len(num),sequence_length):
                if num[block_start:block_start+sequence_length] != sequence:
                    break
            else:
                return True
        
        # not invalid
        return False
     
    def parts1and2(self) -> tuple[int, int]:
        invalid_total_part1: int = 0
        invalid_total_part2: int = 0
        for product_range in self._product_ranges:
            range_start, range_end = map(lambda s: int(s), product_range.split('-'))
            for num in range(range_start,range_end+1):
                if self._invalid1(str(num)):
                    invalid_total_part1 += num
                if self._invalid2(str(num)):
                    invalid_total_part2 += num
        return (invalid_total_part1, invalid_total_part2)
                        
