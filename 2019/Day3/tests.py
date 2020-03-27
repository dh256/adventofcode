import pytest
from Point2D import Point2D
from Lines import Lines
from Grid import Grid

def test_point2d_distance():
    point1 = Point2D(2,-2)
    point2 = Point2D(2,-2)
    point3 = Point2D(-6,-8)
    point4 = Point2D(6, 10)

    assert point1.distance(point2) == 0
    assert point1.distance(point3) == 14
    assert point1.distance(point4) == 16
    assert point3.distance(point4) == 30

@pytest.mark.parametrize("filename,expected",{('test1.txt',6),("test3.txt",159),('test2.txt',135)})
def test_closest_intersect(filename,expected):
    grid =  Grid(Lines(filename))
    grid.populate()
    assert(grid.closest_intersect() == expected)

@pytest.mark.parametrize("filename,expected",{('test1.txt',30),("test3.txt",610),('test2.txt',410)})
def test_shortest_intersect_path(filename,expected):
    grid =  Grid(Lines(filename))
    grid.populate()
    assert(grid.shortest_intersect_path() == expected)