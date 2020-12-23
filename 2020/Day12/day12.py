from Ship import Ship,ShipMoveMode

# Part 1
ship = Ship("input.txt")
dist = ship.navigate(mode=ShipMoveMode.SHIP)
print(dist)

# Part 2
ship.reset()
dist = ship.navigate(mode=ShipMoveMode.WAYPOINT)
print(dist)