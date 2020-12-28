from attr import setters

'''
Class to represent Day 14 binary number
'''
class Binary():

    def __init__(self,num,length):
        # Holds num as a binary in a dictionary, right most is 1, left most is 2 ^ length-1
        self._length = length
        self._bin = {}
        for b in range(length,0,-1):
            if pow(2,length-b) & num:
                self._bin[b] = '1'
            else:
                self._bin[b] = '0'
        
    def __str__(self):
        output = ''
        for i in range(self._length,0,-1):
            output = self._bin[i] + output
        return output

    def update(self,index,value):
        if value in ('0','1','X'):
            self._bin[index] = value 
        else:
            raise ValueError   

    @property
    def bin(self):
        return self._bin

    @property
    def num(self):
        if len(list(filter(lambda v : v == 'X', self._bin))) == 0:
            return int('0b' + self.__str__(),2)
        else:
            raise ValueError
