import re

class File:

    def __init__(self,filename):
        with open(filename,"r") as input_file:
            self.contents = input_file.read().strip('\n')

    def decompress(self):
        decompressed = ""

        '''
        While current position not beyond end of file contents:
            Start at position 0
            Find first (axb) pattern in string and extract and b by splitting on x
                If no match found copy everything from curr_pos to end of contents
            Copy everything from start position to character before first bracket (start of marker)
            Starting at character after ) (end of marker) take next a characters and then copy these b times to output
            Set current position to (end of marker) take next a characters
        '''
        curr_pos = 0
        regex = re.compile(r'\((\d+x\d+)\)')
        while curr_pos < len(self.contents):
            # find occurrences of (axb) in contents starting at curr_pos
            match = regex.search(self.contents,curr_pos)
            if match:
                marker = match.group(0).replace('(','')
                marker = marker.replace(')','')
                marker_components = marker.split('x')
                num_chars_to_copy = int(marker_components[0])
                num_times_to_copy = int(marker_components[1])
                start_of_marker = match.start()
                end_of_marker = match.end()

                # copy characters up to start of marker
                decompressed += self.contents[curr_pos:start_of_marker]

                # copy characters after marker
                chars_to_copy = self.contents[end_of_marker:end_of_marker+num_chars_to_copy]                
                for _ in range(0,num_times_to_copy):
                    decompressed += chars_to_copy

                curr_pos = end_of_marker + num_chars_to_copy
            else:
                decompressed += self.contents[curr_pos:]
                curr_pos = len(self.contents)

        return decompressed

    def decompress2(self):
        # A multiplier is a tuple (m,e) where m is multiplier and e is position it ends at
        self.multipliers = []
        total_length = 0
        curr_pos = 0
        regex = re.compile(r'\((\d+x\d+)\)')
        while curr_pos < len(self.contents):
            match = regex.search(self.contents,curr_pos)
            if match:
                marker_start = match.start()
                marker_end = match.end()
                marker = match.group(0).replace('(','')
                marker = marker.replace(')','')
                marker_components = marker.split('x')
                a = int(marker_components[0])    # number of characters
                b = int(marker_components[1])    # multiplier

                # get any prefix chars
                # for each character multiply by any valid multipliers and add to total length
                prefix_chars = 0
                if marker_start > curr_pos:
                    for j in range(0,marker_start - curr_pos):
                        total_length += self.valid_multipliers(curr_pos+j)

                # add b to list of multipliers
                self.multipliers.append((b,a+marker_end))
                
                # move curr_pos to end of marker
                curr_pos = marker_end
            else:
                # get any remaining chars
                # for each character multiply by any valid multipliers and add to total length
                for i in range(0,len(self.contents) - curr_pos):
                    total_length += self.valid_multipliers(curr_pos+i)
                curr_pos = len(self.contents)

        return total_length

    def valid_multipliers(self, curr_pos):
        # a valid multiplier is any multiplier whose endpoint 
        # is greater than current_position
        multiplier = 1
        for m in [f[0] for f in filter(lambda x : curr_pos < x[1], self.multipliers)]: 
            multiplier *= m
        return multiplier

   