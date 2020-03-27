import pytest
from day17 import ClayStrands
from day17 import Grid
from day17 import Point

@pytest.fixture(scope="module")
def grid():
    strands = ClayStrands("day17_test.txt")
    grid = Grid(strands)
    return grid

@pytest.fixture(scope="module")
def grid_water():
    strands = ClayStrands("day17_test.txt")
    grid = Grid(strands)
    for y in range (0,6):
        grid.grid[y][500] = '|'
    for x in range(496,501):
        grid.grid[6][x] = '~'
    return grid
    
def test_fall(grid,grid_water):
    result = grid.can_fall(Point(500,1))
    assert result[0]
    assert result[1] is None

    result = grid.can_fall(Point(500,6))
    assert result[0] == False
    assert result[1] == "CLAY"

    result = grid_water.can_fall(Point(500,5))
    assert result[0] == False
    assert result[1] == "WATER"

    result = grid.can_fall(Point(500,13))
    assert result[0] == False
    assert result[1] == "MAX"
    
def test_constrained(grid,grid_water):
    assert grid.constrained(Point(500,12))[0] == True 
    assert grid.constrained(Point(499,12))[0] == True
    assert grid.constrained(Point(503,12))[0] == True
    assert grid.constrained(Point(500,4))[0] == False
    assert grid.constrained(Point(500,2))[0] == False
    assert grid.constrained(Point(500,9))[0] == False
    assert grid_water.constrained(Point(500,5))[0] == True
    assert grid_water.constrained(Point(500,2))[0] == False

def test_countwater(grid_water):
    assert grid_water.countwater() == 10


def test_fill(grid):
    grid.fill()
    assert grid.countwater() == 57
