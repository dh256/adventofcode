import re

class WeatherMachine:
    _digits = {'one':1, 'two':2, 'three':3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
    def __init__(self, file_name) -> None:
        with open(file_name,'r') as input_file:
            self.lines = [line.strip('\n') for line in input_file]
    
    def sum_calibration_values(self, part: int) -> int:
        if part == 1:
            expr = re.compile(r'\d') 
        elif part == 2:
            expr = re.compile(r'(\d|one|two|three|four|five|six|seven|eight|nine)')
        
        result = 0
        for line in self.lines:
            first_num = None
            last_num = None
            for index in range(1,len(line)+1):
                if first_num is None:
                    prefix = line[0:index]
                    match = re.search(expr,prefix)
                    if match is not None:
                        first_num = self._get_digit(match[0])
                
                if last_num is None:
                    suffix = line[-index:]
                    match = re.search(expr,suffix)
                    if match is not None:
                        last_num = self._get_digit(match[0])

            result += int(f'{first_num}{last_num}') 
        
        return result

    def _get_digit(self, value: str) -> str:
        if value in WeatherMachine._digits.keys():
            return WeatherMachine._digits[value]
        else:
            return value