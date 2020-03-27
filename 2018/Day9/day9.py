from blist import blist   # blist offers enhanced performance for large lists. See https://pypi.org/project/blist/ 

players=424
marbles=71482*100
playerScores = [0] * players
marbleToPlay = 2
currentMarbleIndex = 1    # index of current marble (may also want to record value?)
currentPlayer = 2
circle = blist([0,1]) 

while marbleToPlay <= marbles:
    if marbleToPlay % 23 == 0:
        # find marble seven places to left (counter clockwise of current marble) and remove
        marbleToRemoveIndex = currentMarbleIndex - 7
        if marbleToRemoveIndex < 0:
            marbleToRemoveIndex = len(circle) + marbleToRemoveIndex
        marbleRemoved = circle.pop(marbleToRemoveIndex)
        if marbleToRemoveIndex == len(circle):
            currentMarbleIndex = 0
        else:
            currentMarbleIndex = marbleToRemoveIndex
        
        # increment player score
        playerScores[currentPlayer] += marbleRemoved + marbleToPlay

    else:
        # place next marble into circle at appropriate place and update current marble index
        # next marble should be placed into circle between marble 1 and 2 place clockwise of current marble  
        insertIndex = (currentMarbleIndex + 2) 
        if insertIndex > len(circle):       # wrap around
            insertIndex = insertIndex % len(circle)
        circle.insert(insertIndex,marbleToPlay)
        currentMarbleIndex = insertIndex

    # set next player
    currentPlayer = (currentPlayer + 1) % players   # wrap when get to number of players
    
    # set next marble to play
    marbleToPlay += 1
    if marbleToPlay % 100000 == 0:
        print(marbleToPlay)

# get max score
playerScores.sort(reverse=True)
highScore = playerScores[0]
print(f"High score is: {highScore}")
