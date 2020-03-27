def processFile(filename):
    with open(filename, "r") as inputfile:
        lines = [line.strip() for line in inputfile]
        initialState = lines[0][15:]
        notes = lines[2:]
        return(initialState, notes)        

def applyNotes(prevGen, generationOffset, notes):
    generation = 
    return generation

# Solve puzzzle
initialState, notes = processFile('day12.txt')
print(initialState)
print(notes)

# generations will hold state of plants after each generation
# prevGen holds previous generation status and is passed to applyNotes 
# If 
generations = list(initialState)
prevGen = initialState
nextGen = applyNotes(prevGen, notes)
