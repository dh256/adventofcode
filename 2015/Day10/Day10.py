'''
David Hanley, November 2024
'''

class Day10:
    def __init__(self, digits: str) -> None: 
        self.digits = digits
    
    def part1(self, iterations: int) -> int:
        for _ in range(iterations):
            next_digit: str = self.digits[0]
            index: int = 0
            new_digits: str = ''
            sequence_length = 1
            while index < len(self.digits):
                if index+1 < len(self.digits) and self.digits[index+1] == next_digit:
                    sequence_length += 1
                else:
                    new_digits += f'{sequence_length}{next_digit}'
                    if index + 1 < len(self.digits):
                        sequence_length = 1
                        next_digit = self.digits[index+1]
                index += 1
            self.digits = new_digits
            
        return len(self.digits)
    
    def part2(self,iterations) -> int:
        return self.part1(iterations)