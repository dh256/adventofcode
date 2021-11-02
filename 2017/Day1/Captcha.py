class Captcha:

    def __init__(self,input_file):
        with open(input_file, 'r') as in_file:
            self.sequence = in_file.readline().strip('\n')

    def sum(self):
        index = 0
        sum = 0
        for index in range(0,len(self.sequence)):
            if self.sequence[index % len(self.sequence)] == self.sequence[(index+1) % len(self.sequence)]:
                sum += int(self.sequence[index % len(self.sequence)])
        return sum

    def sum2(self):
        index = 0
        sum = 0
        seq_len = len(self.sequence)
        half_seq_len = seq_len // 2
        for index in range(0,seq_len):
            if self.sequence[index] == self.sequence[(index+half_seq_len) % seq_len]:
                sum += int(self.sequence[index])
        return sum
        