class Day3:
    def __init__(self,file_name:str) -> None:
        with open(file_name, 'r') as input_file:
            self._banks: list[str] = [line.strip('\n') for line in input_file]

    def next_digit(self,remaining_banks: str, min_length: int) -> str:
        # stop when min_length is 0 
        if min_length == 0:
            return ''
        
        # find largest digit in remaining_banks such that can still make a number of min length
        end_index = len(remaining_banks)-(min_length-1)
        digit: str = max(remaining_banks[0:end_index])
        index: int = remaining_banks[0:end_index].index(digit)
        remaining_banks = remaining_banks[index+1:]

        # recurse
        return digit + self.next_digit(remaining_banks,min_length-1)

    def parts1and2(self) -> tuple[int, int]:
        joltages_part1: int = sum([int(self.next_digit(bank,2)) for bank in self._banks])
        joltages_part2: int = sum([int(self.next_digit(bank,12)) for bank in self._banks])
        return (joltages_part1, joltages_part2)
