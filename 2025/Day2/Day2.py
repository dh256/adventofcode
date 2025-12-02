class Day2:
    def __init__(self,file_name:str) -> None:
        with open(file_name, 'r') as input_file:
            self._product_ranges: list[str] = input_file.readline().strip('\n').split(',')
    
    def invalid1(self,num: int) -> bool:
        '''
        Invalid if made only of some sequence of digits repeated twice
        '''
        num_str = str(num)
        if len(num_str) % 2 == 1:
            return False
        else:
            divide_at = len(num_str) // 2
            if num_str[0:divide_at] == num_str[divide_at:]:
                return True
    
    def invalid2(self,num: int) -> bool:
        '''
        Invalid if made only of a sequence of digits repeated at least twice
        '''
        num_str = str(num)
        for prefix_length in range (1,(len(num_str) // 2 + 1)):
            sequence = num_str[0:prefix_length]
            
            # is remain num_str only made up of "sequence" chars return True
            for i in range(prefix_length,len(num_str),prefix_length):
                if num_str[i:i+prefix_length] != sequence:
                    break
            else:
                return True
        
        # not invalid
        return False
     
    def parts1and2(self) -> tuple[int, int]:
        invalid_total1: int = 0
        invalid_total2: int = 0
        for product_range in self._product_ranges:
            range_start, range_end = map(lambda p: int(p), product_range.split('-'))
            for num in range(range_start,range_end+1):
                if self.invalid1(num):
                    invalid_total1 += num
                if self.invalid2(num):
                    invalid_total2 += num
        return (invalid_total1, invalid_total2)
                        
