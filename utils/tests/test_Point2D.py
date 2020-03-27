import pytest
from adventofcode.utils.Point2D import Point2D

eq_data = [
        (Point2D(0,0),Point2D(0,0),True),
        (Point2D(-1,0),Point2D(0,0),False),  
        (Point2D(0,-1),Point2D(0,0),False),  
        (Point2D(0,0),Point2D(-1,0),False),  
        (Point2D(0,0),Point2D(0,-1),False)  
    ]

dist_data = [
    (Point2D(10,10),Point2D(0,0),20),
    (Point2D(-10,-10),Point2D(0,0),20),
    (Point2D(0,0),Point2D(10,10),20),
    (Point2D(0,0),Point2D(-10,-10),20),
    (Point2D(5,5),Point2D(5,5),0)
]

repr_data=[
    (Point2D(0,0), "(0,0)"),
    (Point2D(-5,-3), "(-5,-3)"),
    (Point2D(5,3), "(5,3)")
]

@pytest.mark.parametrize("point1,point2,equals",eq_data)
def test_eq(point1,point2,equals):
    assert((point1 == point2) == equals)

@pytest.mark.parametrize("point1,point2,dist",dist_data)
def test_distance(point1,point2,dist):
    assert(point1.distance(point2) == dist)

@pytest.mark.parametrize("point,repr_str",repr_data)
def test_repr(point,repr_str):
    assert(str(point) == repr_str)
