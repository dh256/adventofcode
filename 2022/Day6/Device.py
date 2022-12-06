class Device:

    def __init__(self,file_name) -> None:
        with open(file_name,'r') as input_file:
            self.stream = input_file.readline().strip('\n')

    def first_marker(self,chars) -> int:
        '''
        Returns position of first marker
        That is the end position of first string of length chars that contains unique
        characters in the input stream
        '''
        for index in range(0,len(self.stream)-chars-1):
            if len(set(self.stream[index:index+chars])) == chars:
                return index+chars