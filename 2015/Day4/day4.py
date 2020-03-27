import hashlib

def find_number(key, prefix, start=1):
    i = start
    while True:
        string_to_hash = f"{key}{i}"
        result = hashlib.md5(string_to_hash.encode())
        if result.hexdigest().startswith(prefix):
            return i
        i+=1

key = "yzbqklnj"
part1 = find_number(key, "00000")
print(f"Part 1: {part1}")
part2 = find_number(key, "000000")
print(f"Part 2: {part2}")
