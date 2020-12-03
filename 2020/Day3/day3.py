from Map import Map,Slope

map = Map("input.txt")

# Part 1
slopes = [Slope(3,1)]
trees = map.traverse(slopes)
print(trees)

# Part 2
slopes = [Slope(3,1),Slope(1,1),Slope(5,1),Slope(7,1),Slope(1,2)]
trees = map.traverse(slopes)
print(trees)