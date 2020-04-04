'''
This method uses a graph
It works but the Dijkstra algorithm is very inefficient for larger grids
Including as an alernative
'''
from Pluto import Pluto

pluto = Pluto("input.txt")
dist = pluto.shortest_distance()
print(dist)
