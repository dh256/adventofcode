import re

class Room:

    def __init__(self, room_code):
        first_square_bracket = room_code.find('[')
        last_dash = [x.start() for x in re.finditer(r'\-', room_code)][-1]   
        self.checksum = room_code[first_square_bracket+1:len(room_code)-1] 
        self.encrypted_name = room_code[0:last_dash]
        self._encrypted_name_checksum = self._get_encrypted_name_checksum()
        self.sector_id = int(room_code[last_dash+1:first_square_bracket])
        self.valid = self.checksum == self._encrypted_name_checksum

    def _get_encrypted_name_checksum(self):
        checksum_dic = dict()
        for c in self.encrypted_name:
            if c != '-':
                if c in checksum_dic.keys():
                    checksum_dic[c] += 1
                else:
                    checksum_dic[c] = 1

        # sort dictionary on Value desc, then Key asc and take (up to) first 5
        checksum_keys = [x[0] for x in sorted(checksum_dic.items(),key=lambda i: (-i[1],i[0]))][0:5]

        # return as a string
        checksum = "" 
        for k in checksum_keys: 
            checksum += k 
        return checksum

class Rooms:

    def __init__(self, filename):
        with open(filename, "r") as input:
            self.rooms = [Room(line.strip('\n')) for line in input]

    def sector_id_sum(self):
        return sum([room.sector_id for room in self.rooms if room.valid])

    def decrypt_room_names(self):
        decrypted_rooms = [(self._decrypt(room.encrypted_name,room.sector_id),room.sector_id) for room in self.rooms if room.valid]
        return decrypted_rooms
    
    def _decrypt(self, enc_name, sector_id):
        decrypted = ""
        move_by = sector_id % 26    # Each factor of 26 brings char back to itself
                                    # only interested in mod 26
        for c in enc_name:
            if c == '-':            # dash becomes string
                decrypted += ' '
            else:
                if ord(c) + move_by > ord('z'): # overlap, wrap around
                    decrypted += chr(ord('a') + (move_by - 1 - (ord('z') - ord(c))))
                else:  # no overlap
                    decrypted += chr(ord(c) + move_by)
        return decrypted