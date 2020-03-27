import pytest
from Asteroid import AsteroidField
from Line import Line
from Point2D import Point2D

testdata_Point2D = [(Point2D(3,4),Point2D(1,0),Point2D(2,2),Point2D(1,1)),
                    (Point2D(0,0),Point2D(4,4),Point2D(2,2),Point2D(-6,-16)),
                    (Point2D(3,1),Point2D(3,5),Point2D(3,2),Point2D(2,9)),
                    (Point2D(1,3),Point2D(5,3),Point2D(2,3),Point2D(2,9))]
testdata=[("test1.txt",10),("test2.txt",40)]
testdata2=[("test1.txt",Point2D(3,4),8),
            ("test2.txt",Point2D(5,8),33),
            ("test3.txt",Point2D(1,2),35),
            ("test4.txt",Point2D(6,3),41),
            ("test5.txt",Point2D(11,13),210)
            ]

@pytest.mark.parametrize("start,end,point_on_line,point_not_on_line", testdata_Point2D)
def test_line(start,end,point_on_line,point_not_on_line):
    line = Line(start,end)
    assert(line.point_on_line(point_on_line))
    assert(line.point_on_line(point_not_on_line) == False)

@pytest.mark.parametrize("filename,asteroids",testdata)
def test_num_asteroids(filename,asteroids):
    field = AsteroidField(filename)
    assert(field.num_asteroids() == asteroids)

@pytest.mark.parametrize("filename,location,asteroids",testdata2)
def test_best_asteroid(filename,location,asteroids):
    field = AsteroidField(filename)
    best_asteroid = field.best_asteroid()
    assert(best_asteroid[0] == location and best_asteroid[1] == asteroids)
