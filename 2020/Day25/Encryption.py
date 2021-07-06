class Encryption:

    _divisor = 20201227 
    _subject_number = 7

    @staticmethod
    def calc_loop_size(key):
        curr_val = 1
        loop_size = 0
        while curr_val != key:
            loop_size += 1
            curr_val = (curr_val * Encryption._subject_number) % Encryption._divisor 
        return loop_size

    @staticmethod
    def calc_private_key(subject_number,loop_size):
        private_key = 1
        for _ in range(0,loop_size):
            private_key = (private_key * subject_number) % Encryption._divisor
        return private_key