class Password:
    def __init__(self,password):
        self.password = str(password)

    def valid(self):
        if len(self.password) != 6:
            return False
        prev_c = None
        two_digits_found = False
        for c in self.password:
            if not prev_c is None:
                if  c < prev_c:
                    return False
                elif prev_c == c:
                    two_digits_found = True
            prev_c = c    
        return two_digits_found

    def valid2(self):
        if len(self.password) != 6:
            return False
        prev_c = None
        two_digits_found = False
        repeating_digits = {}
        for c in self.password:
            if not prev_c is None:
                if  c < prev_c:
                    return False
                elif prev_c == c:
                    if c in repeating_digits:
                        repeating_digits[c] += 1
                    else:
                        repeating_digits[c] = 2
            prev_c = c
                
        for d,count in repeating_digits.items():
            if count == 2:
                return True
        return False