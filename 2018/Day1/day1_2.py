
dupFreqFound = False
freq = 0
freqSet = {0}
while not dupFreqFound:
    file = open("day1.txt","r")
    for line in file: 
        inc = int(line)
        freq = freq + inc
        if freq not in freqSet:
            freqSet.add(freq)
        else:
            print("First repeating frequency: ", freq)
            dupFreqFound = True
            break
