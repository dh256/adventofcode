class MemoryGame():

    def __init__(self,input):
        self._start_numbers = input
        self._spoken_numbers = {}

    def spoken_before(self,num):
        '''
        Return number of times given number has been spoken before
        '''
        try:
            return len(self._spoken_numbers[num])
        except KeyError:
            return 0 

    def update_spoken_numbers(self,num,turn):
        '''
        Updates spoken numbers
        '''
        try:
            self._spoken_numbers[num].append(turn)
        except KeyError:
            self._spoken_numbers[num] = [turn]

    def play(self,turns):
        '''
        Play game
        This method works but is quite slow. Look for a faster algorithm
        '''
        last_number_spoken = None
        for t in range(1,turns+1):  
            if t <= len(self._start_numbers):
                self.update_spoken_numbers(self._start_numbers[t-1],t)
                last_number_spoken = self._start_numbers[t-1]
            else:
                times_spoken_before = self.spoken_before(last_number_spoken)
                if times_spoken_before == 1:
                    # last number spoken was new therefore last_number_spoken becomes 0
                    self.update_spoken_numbers(0,t)
                    last_number_spoken = 0
                else: 
                    # last number spoken was not new
                    last_number_spoken = self._spoken_numbers[last_number_spoken][times_spoken_before-1] - self._spoken_numbers[last_number_spoken][times_spoken_before-2]
                    self.update_spoken_numbers(last_number_spoken,t)
        return last_number_spoken