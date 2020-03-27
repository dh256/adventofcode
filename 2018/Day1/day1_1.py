file = open("day1.txt","r")
start = 0
for line in file: 
    inc = int(line)
    start = start + inc

print(start)
