import hashlib


class Door:

    def __init__(self,door_id):
        self.door_id = door_id

    def find_password(self):
        password = ""
        num = 0
        while len(password) < 8: 
            hash_str = f'{self.door_id}{num}'
            result = hashlib.md5(hash_str.encode())
            hash_hex = result.hexdigest()
            if hash_hex[0:5] == "00000":
                password += hash_hex[5]    
            num += 1

        return password

    def find_password2(self):
        password_chars = ['-' for x in range(8)]
        valid_positions = [f'{i}' for i in range(8)]
        num = 0
        while '-' in password_chars: 
            hash_str = f'{self.door_id}{num}'
            result = hashlib.md5(hash_str.encode())
            hash_hex = result.hexdigest()
            if hash_hex[0:5] == "00000":
                position = hash_hex[5]
                if position in valid_positions:
                    if password_chars[int(position)] == '-':
                        password_chars[int(position)] = hash_hex[6]  
                        print(f'{self.password_to_string(password_chars)}')
            num += 1
        return self.password_to_string(password_chars)

    def password_to_string(self,password_chars):
        password = ''
        for c in password_chars:
            password += c
        return password
