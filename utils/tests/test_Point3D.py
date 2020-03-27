import pytest
from adventofcode.utils.Point3D import Point3D

eq_data = [
        (Point3D(0,0,0),Point3D(0,0,0),True),
        (Point3D(-1,0,0),Point3D(0,0,0),False),  
        (Point3D(0,-1,0),Point3D(0,0,0),False),  
        (Point3D(0,0,-1),Point3D(0,0,0),False),  
        (Point3D(0,0,0),Point3D(-1,0,0),False),  
        (Point3D(0,0,0),Point3D(0,-1,0),False),  
        (Point3D(0,0,0),Point3D(0,0,-1),False)
    ]

dist_data = [
    (Point3D(10,10,10),Point3D(0,0,0),30),
    (Point3D(-10,-10,-10),Point3D(0,0,0),30),
    (Point3D(0,0,0),Point3D(10,10,10),30),
    (Point3D(0,0,0),Point3D(-10,-10,-10),30),
    (Point3D(5,5,5),Point3D(5,5,5),0)
]

repr_data=[
    (Point3D(0,0,0), "(0,0,0)"),
    (Point3D(-5,-3,-2), "(-5,-3,-2)"),
    (Point3D(5,3,2), "(5,3,2)")
]

add_data=[
    (Point3D(0,0,0),Point3D(10,10,10), Point3D(10,10,10)),
    (Point3D(0,0,0),Point3D(-10,-10,-10), Point3D(-10,-10,-10))
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

@pytest.mark.parametrize("point1,point2,point3",add_data)
def test_add(point1,point2,point3):
    assert(point1 + point2 == point3)