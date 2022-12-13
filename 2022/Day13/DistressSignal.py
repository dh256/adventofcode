class Signal:
    def __init__(self,file_name: str) -> None:
        self.packets = []
        with open(file_name,'r') as input_file:
            for line in input_file:
                line = line.strip('\n')
                if len(line) > 0:
                    self.packets.append(eval(line))        

    def compare(self, left, right) -> bool:
        curr_index = 0
        for curr_index in range(max(len(left), len(right))):
            
            # if left has not more items order is correct
            if curr_index >= len(left):
                return True

            # if right has no more items order is wrong
            if curr_index >= len(right):
                return False
            
            # if both are ints, compare
            if type(left[curr_index]) == int and type(right[curr_index]) == int:
                if left[curr_index] < right[curr_index]:
                    return True
                
                if left[curr_index] > right[curr_index]:
                    return False

                else:
                    continue

            if (type(left[curr_index]) == list and type(right[curr_index]) == list):
                if not left[curr_index] == right[curr_index]:
                    return self.compare(left[curr_index], right[curr_index])

            if type(left[curr_index]) == int and type(right[curr_index]) == list:
                return self.compare([left[curr_index]],right[curr_index])

            if type(left[curr_index]) == list and type(right[curr_index]) == int:
                return self.compare(left[curr_index],[right[curr_index]])
        
        return True

    def right_order_pairs(self) -> int:
        '''
        Returns the sum of the indices of the pairs that are in the right order
        '''
        index_sum = 0
        for index in range(0,len(self.packets),2):
            if self.compare(self.packets[index], self.packets[index+1]):
                index_sum +=  (index // 2) + 1
        return index_sum

    def pairs_in_right_order(self) -> int:
        '''
        Puts packets in the correct order and returns product of the index of the two decoder keys
        '''
        
        # add in the decoder key packets
        self.packets.append(eval('[[2]]'))
        self.packets.append(eval('[[6]]'))
        
        # sort packets into order (insertion sort)
        for curr_index in range(1, len(self.packets)):
            curr_packet = self.packets[curr_index]
            j = curr_index
            while j > 0 and self.compare(curr_packet, self.packets[j-1]):
                # swap if in correct order
                self.packets[j] = self.packets[j-1]
                j -= 1
                self.packets[j] = curr_packet

        # find indexes of key packets in sorted list and return product of these instances
        first_decoder_index = self.packets.index(eval('[[2]]'))+1
        second_decoder_index = self.packets.index(eval('[[6]]'))+1
        return first_decoder_index * second_decoder_index
