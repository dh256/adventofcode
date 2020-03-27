from Point2D import Point2D
from Line import Line
import math

class LocationInfo():
    def __init__(self,asteroid=True):
        self.asteroid = asteroid
        if asteroid:
            self.can_see = []
            self.cant_see = []
            self.angle = None
        else:
            self.can_see = None
            self.cant_see = None
            self.angle = None

class AsteroidField():    
    def __init__(self,filename):
        '''
        Populate Asteroid Field
        '''
        self.best_asteroid = None
        self.best_asteroid_can_see = None
        self.field = {}
        with open(filename,'r') as asteroid_data:
            y = 0
            rows = [line.strip('\n') for line in asteroid_data]
            for row in rows:
                x = 0
                for col in row:
                    if col == '#':
                        self.field[Point2D(x,y)] = LocationInfo()
                    else: 
                        self.field[Point2D(x,y)] = LocationInfo(False)
                    x += 1
                y+=1
            self.columns = x
            self.rows = y

    def num_asteroids(self):
        return len(list(self._asteroids()))
    
    def _asteroids(self):
        return filter(lambda i : i[1].asteroid == True,self.field.items())

    def _empty(self):
        return filter(lambda i : i[1].asteroid == False,self.field.items())

    def find_best_asteroid(self):
        # for each asteroid:
        #   examine each other asteroid and determine whether any of the other
        #   remaining asteroids sit in line of sight (i.e. sit on line between two asteroids)
        #   if one is found, add other asteroid to can't see collection of asteroid (and vice versa)
        #   if one is not found, add other asteroid to can see collection of asteroid (and vice versa)
        # when complete return asteroid with highest number of can_sees 
        for a1 in self._asteroids():
            for a2 in self._asteroids():
                if a1[0] != a2[0] and not (a2[0] in a1[1].can_see or a2[0] in a1[1].cant_see):
                    line = Line(a1[0],a2[0])
                    blocker_found = False
                    # if line gcd is 1 then no other point can lie between a1 and a2
                    if line.gcd != 1:
                        # otherwise, need to loop through all other points and determine if any 
                        # line on line
                        for a3 in self._asteroids():    
                            if a3[0] != a1[0] and a3[0] != a2[0]:
                                if line.point_on_line(a3[0]):
                                    # blocker found
                                    a1[1].cant_see.append(a2[0])
                                    a2[1].cant_see.append(a1[0])
                                    blocker_found = True
                                    break

                    if not blocker_found:
                        a1[1].can_see.append(a2[0])
                        a2[1].can_see.append(a1[0])
        
        best_asteroid = max(self._asteroids(),key=lambda i:len(i[1].can_see))
        self.best_asteroid = best_asteroid[0]
        self.best_asteroid_can_see = len(best_asteroid[1].can_see)

    def vapourize(self, number):
        '''
        Vapourizes the given number of asteroids
        Returns x cord * 100 + y coord of the last asteroid vapourized 
        '''
    

        # check that have found best_asteroid, if not find it
        if self.best_asteroid == None:
            self.find_best_asteroid()

        # remove best_asteroid, no longer an asteroid 
        self.field[best_asteriod].asteroid = False

        # for each asteroid in field calculate angle to best_asteroid
        for i in self._asteroids():
            self.field[i[0]].angle = math.atan2(self.best_asteroid.y-i[0].y,self.best_asteroid.x-i[0].x)

        # now sort by angle and distance
        sorted(self.field, key=lambda x,y )

        

    def __repr__(self):
        output_str = ""
        for y in range(0,self.rows):
            for x in range(0,self.columns):
                a = self.field[Point2D(x,y)]
                if a.asteroid:
                    output_str += '#' #f'{len(a.can_see)}'
                else:
                    output_str += '.'
            output_str += '\n'
        return output_str