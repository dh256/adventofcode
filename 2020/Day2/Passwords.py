class Password:
    def __init__(self,input_data):
        parts = input_data.split(' ')
        self.password = parts[2] 
        from_to = parts[0].split('-')
        self.min = int(from_to[0])
        self.max = int(from_to[1])
        self.letter = parts[1][0]

    def valid_part1(self):
        num_chars = len([c for c in self.password if c == self.letter])
        return num_chars >= self.min and num_chars <= self.max

    def valid_part2(self):
        a = self.password[self.min-1] == self.letter
        b = self.password[self.max-1] == self.letter

        # XOR
        return (a and not b) or (not a and b)

class Passwords:

    def __init__(self,input_file):
        with open(input_file,'r') as data:
            self.passwords = [Password(line.strip('\n')) for line in data] 

    def num_valid_part1(self):
        return len([p for p in self.passwords if p.valid_part1()])

    def num_valid_part2(self):
        return len([p for p in self.passwords if p.valid_part2()])