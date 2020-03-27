from functools import reduce
from itertools import islice
import sys

class Tree:
    def __init__(self, data):
        self.data = data

    def build(self):
        # next iter is always number if children
        # next iter is always number of metadataitems
        # if number of children is zero next metadataitems iters are the metadataitems for that child.
        # if number of children is > 0, recursively call build for each child
        # once all children are processed next metadataitems iters are the metadataitems for parent node 
        children = next(self.data)
        metadataItems = next(self.data)
        if children == 0:
            childSum = sum(islice(self.data, metadataItems))
            return childSum
        
        totalSum = 0
        for _ in range(children):
            childMetadataItemsSum = self.build()
            totalSum += childMetadataItemsSum
        totalSum += sum(islice(self.data, metadataItems))
        return totalSum

        
def processInput(filename):
    # file consists of a single line with a large number of numbers
    # read in whole line and split into a list of numbers
    with open(filename, "r") as input:
        data = iter(int(i) for i in input.read().split())
        return data

# increase recusrsion linit - Python limits to 1000 recursions by default
sys.setrecursionlimit(10000)
data = processInput('day8_full.txt')
tree = Tree(data)
totalSum = tree.build()
print(f'{totalSum}')
