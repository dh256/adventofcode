class Packet:
    def __init__(self,version,type_id,lit_val=None,sub_packets=None):
        self._version = version
        self._type_id = type_id
        self._lit_val = lit_val            # only applies to type 4 - int
        self._sub_packets = sub_packets    # only applies to type <> 4 - list of packets

    @property
    def version(self):
        return self._version

    @property
    def type_id(self):
        return self._type_id
    
    @property
    def lit_val(self):
        return self._lit_val

    @property
    def sub_packets(self):
        return self._sub_packets


class Bits:
    
    __decode_table = { 
    "0": "0000",
    "1": "0001",
    "2": "0010",
    "3": "0011",
    "4": "0100",
    "5": "0101",
    "6": "0110",
    "7": "0111",
    "8": "1000",
    "9": "1001",
    "A": "1010",
    "B": "1011",
    "C": "1100",
    "D": "1101",
    "E": "1110",
    "F": "1111"
    }
    
    def __init__(self,filename):
        with open(filename,'r') as input_file:
            self.decoded_message =''.join([Bits.__decode_table[c] for c in input_file.readline().strip('\n')])
            _, self.packets = self.get_packets(0,None,None)

    def get_packets(self,start_pos,seq_len,num_packets):
        curr_pos = start_pos
        packets = []
        keep_going = True
        while keep_going:
            curr_pos, version, type_id = self.get_header(curr_pos)
            if type_id == 4:
                curr_pos, lit_val = self.get_literal_value(curr_pos)
                packets.append(Packet(version,type_id,lit_val))
            else:
                # operator packet
                curr_pos, length_type_id, sub_packet_val = self.get_sub_packet_ind(curr_pos)
                if length_type_id == '0':
                    # need to extract sub_packet_length chars and recurse
                    curr_pos, sub_packets = self.get_packets(curr_pos,seq_len=sub_packet_val,num_packets=None)
                else:
                    # need to recurse until next num_sub_packets are found and add these as subpackets
                    curr_pos, sub_packets = self.get_packets(curr_pos,seq_len=None,num_packets=sub_packet_val)
                packets.append(Packet(version,type_id,lit_val=None,sub_packets=sub_packets))

            # need to decide to keep going or not
            if seq_len is None and num_packets is None:
                keep_going = curr_pos < len(self.decoded_message) and int(self.decoded_message[curr_pos:],2) > 0
            elif not seq_len is None:
                # check whether we have read seq_len bits
                keep_going = curr_pos - start_pos < seq_len
            else:
                # check whether we have extracted num_packets packets
                keep_going = len(packets) < num_packets

        return curr_pos, packets

    def get_sub_packet_ind(self,curr_pos):
        length_type_id = self.decoded_message[curr_pos]
        curr_pos += 1
        inc = 15 if length_type_id == '0' else 11
        sub_packet_ind = int(self.decoded_message[curr_pos:curr_pos+inc],2)
        curr_pos += inc
        return curr_pos, length_type_id, sub_packet_ind

    def get_header(self,curr_pos):
        version = int(self.decoded_message[curr_pos:curr_pos+3],2)
        curr_pos += 3
        type_id = int(self.decoded_message[curr_pos:curr_pos+3],2)
        curr_pos += 3
        return curr_pos, version, type_id

    def get_literal_value(self,curr_pos):
        # process literal value
        # take next 5 bits
        lit_val_bin = ""
        last = False
        while not last:
            chunk = self.decoded_message[curr_pos:curr_pos+5]
            lit_val_bin += chunk[1:5]
            last = chunk[0] == '0'
            curr_pos += 5
        lit_val = int(lit_val_bin, 2)
        return curr_pos, lit_val

    def version_sum(self, packets=None, total=0):
        # iterate over packets return version sum
        if packets == None:
            packets = self.packets
        for p in packets:
            total += p.version
            if not p.sub_packets is None:
                total += self.version_sum(p.sub_packets)
        return total

    def evaluate(self, packets=None, eval_str=''):
        if packets == None:
            packets = self.packets
        for p in packets:
            if p.type_id == 4:
                return p.lit_val
            elif p.type_id == 0:
                sp_sum = 0
                for sp in p.sub_packets:
                    sp_sum += self.evaluate([sp])
                return sp_sum
            elif p.type_id == 1:
                sp_prod = 1
                for sp in p.sub_packets:
                    sp_prod *= self.evaluate([sp])
                return sp_prod
            elif p.type_id == 2:
                vals = []
                for sp in p.sub_packets:
                    vals.append(self.evaluate([sp]))
                return min(vals)
            elif p.type_id == 3:
                vals = []
                for sp in p.sub_packets:
                    vals.append(self.evaluate([sp]))
                return max(vals)
            elif p.type_id == 5:
                sp_1 = self.evaluate([p.sub_packets[0]])
                sp_2 = self.evaluate([p.sub_packets[1]])
                return 1 if sp_1 > sp_2 else 0
            elif p.type_id == 6:
                sp_1 = self.evaluate([p.sub_packets[0]])
                sp_2 = self.evaluate([p.sub_packets[1]])
                return 1 if sp_1 < sp_2 else 0
            elif p.type_id == 7:
                sp_1 = self.evaluate([p.sub_packets[0]])
                sp_2 = self.evaluate([p.sub_packets[1]])
                return 1 if sp_1 == sp_2 else 0