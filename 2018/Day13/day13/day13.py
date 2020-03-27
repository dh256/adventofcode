from itertools import cycle

class Track():
    '''
    Manages the track
    Consist of a grid (list of list) of track symbols, a list of carts and a list of where crashes occurred
    
    Operations exist to moveCarts (until only one is remaining); move an individual cart, detect crashes and display results
    '''

    def __init__(self):
        self.track = []
        self.carts = Carts()
        self.crashes = []       

    def moveCart(self, cart):
        '''
        Move a cart and detect any crashes
        Moving a cart involves determing its current position, its direction of travel, whether it will crash into another cart and whether to turn if next position on track is a curve or intersection
        Returns False of more than one cart remains, true otherwise
        '''
        cartPositionX = cart.position.x
        cartPositionY = cart.position.y
        nextSymbol = None
        if cart.direction.direction == Direction.UP:
            nextSymbol = self.track[cartPositionY-1][cartPositionX]
            cart.moveUp()
        elif cart.direction.direction == Direction.DOWN: 
            nextSymbol = self.track[cartPositionY+1][cartPositionX]
            cart.moveDown()
        elif cart.direction.direction == Direction.LEFT:
            nextSymbol = self.track[cartPositionY][cartPositionX-1]
            cart.moveLeft()
        elif cart.direction.direction == Direction.RIGHT:
            nextSymbol = self.track[cartPositionY][cartPositionX+1]
            cart.moveRight()
        
        # detect crash
        crash = self.detectCrash(cart.id)
        if not crash:
            # check whether at curve or intersection and turn accordingly
            if nextSymbol in ["/","\\"]:
                cart.curveTurn(nextSymbol)
            elif nextSymbol == "+":
                cart.intersectionTurn()
        
        # check whether final crash has occurred leaving only 1 cart remaining
        return len(self.carts.notCrashed()) == 1

    def moveCarts(self):
        '''
        move all carts one after anbother until only one remains
        Note: the one remaining must move once before finsihing
        '''
        finished = False
        while not finished:
            # carts are moved in row (y) and column (x)
            self.carts.carts.sort(key=lambda item:(item.position.y, item.position.x))
            for cart in self.carts.carts:
                if not cart.crashed:
                    finished = self.moveCart(cart)

    def results(self):
        # print results
        print(f'{self}')
        print(f'Crashes detected:')
        for index, crash in enumerate(self.crashes):
            print(f'{index}: @ {crash.x},{crash.y}')
        remainingCart = list(filter(lambda cart: not cart.crashed, self.carts.carts))[0]
        print(f"Remaining cart at position: {remainingCart.position.x},{remainingCart.position.y} pointing {remainingCart.direction}")    

    def detectCrash(self,id):
        # crash if given position of matches any other cart
        movingCart = [cart for cart in self.carts.carts if cart.id == id][0]
        stationeryCarts = [cart for cart in self.carts.carts if cart.id != id and not cart.crashed and cart.position == movingCart.position]
        if len(stationeryCarts) == 1:
            # record position of crash and remove crashed carts from list
            # when only one car t left, return 1 
            self.crashes.append(movingCart.position)
            movingCart.crashed = True
            stationeryCarts[0].crashed = True
            return True
        else:
            return False    # no crash

    def __str__(self):
        output=""
        for y, row in enumerate(self.track):
            for x, c in enumerate(row):
                cartFound = [cart for cart in self.carts.carts if cart.position.x == x and cart.position.y == y and not cart.crashed] 
                if len(cartFound) == 0:
                    output += c
                else:
                    output += str(cartFound[0])
            output += '\n'
        return output

class Position():
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __eq__(self,pos):
        return self.x == pos.x and self.y == pos.y 

class NextTurn():
    # Manages direction of cart's next turn
    LEFT=0
    STRAIGHT=1
    RIGHT=2
    def __init__(self):
        # use itertools.cycle to cycle through next turn values LEFT->STRAIGHT->RIGHT->LEFT ...
        self.turns = cycle((self.LEFT,self.STRAIGHT,self.RIGHT))

        # set initial nextTurn to first value in cycle
        self.nextTurn = next(self.turns)

    def turn(self):
        # set to next value in cycle
        self.nextTurn = next(self.turns)

class Direction():
    # Manage direction cart is facing
    # cart can turn either clockwise or anticlockwise
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3

    def __init__(self,direction):
        self.direction = direction
    
    def rotateClockwise(self):
        self.direction = (self.direction + 1) % 4   # use mod to wrap round

    def rotateAntiClockwise(self):
        self.direction = (self.direction - 1) % 4   # use mod to wrap round

    # represent cart direction when displayed 
    def __repr__(self):
        if self.direction == Direction.UP:
            return "^" 
        elif self.direction == Direction.DOWN:
            return "v"
        elif self.direction == Direction.RIGHT:
            return ">"
        elif self.direction == Direction.LEFT:
            return "<"

class Cart():
    '''
    Manage a cart
    A cart has an id, direction of next turn, direction it is pointing, a position and whether it has crashed
    A cart can either move up, down, left or right and can turn at either an intersection (+) or a curve (\\  or /)
    '''
    def __init__(self,id,direction,x,y):
        self.id = id
        self.nextturn=NextTurn()    # inital next turn is LEFT
        self.position=Position(x,y)
        self.crashed = False
        if direction == 'v':
            self.direction = Direction(Direction.DOWN)
        elif direction == '>':
            self.direction = Direction(Direction.RIGHT)
        elif direction == '<':
            self.direction = Direction(Direction.LEFT)
        elif direction == '^':
            self.direction = Direction(Direction.UP)
    
    def moveUp(self):
        self.position.y -= 1

    def moveLeft(self):
        self.position.x -= 1

    def moveRight(self):
        self.position.x += 1

    def moveDown(self):
        self.position.y += 1

    def curveTurn(self, curve):
        '''
        A cart changes direction at a curve depending on which direction it is currently travelling
        and the direction of the curve
        '''
        if curve == '/':
            if self.direction.direction == Direction.RIGHT or self.direction.direction == Direction.LEFT:
                self.direction.rotateAntiClockwise()
            elif self.direction.direction == Direction.UP or self.direction.direction == Direction.DOWN:
                self.direction.rotateClockwise()
            
        elif curve == '\\':
            if self.direction.direction == Direction.RIGHT or self.direction.direction == Direction.LEFT:
                self.direction.rotateClockwise()
            elif self.direction.direction == Direction.UP or self.direction.direction == Direction.DOWN:
                self.direction.rotateAntiClockwise()

    def intersectionTurn(self):
        '''
        At an intersection, cart will change direction depending on its next turn direction
        Calculate which way cart needs to turn and change direction
        Then, set next turn direction
        '''
        if self.direction.direction == Direction.DOWN or self.direction.direction == Direction.LEFT: 
            if self.nextturn.nextTurn == NextTurn.LEFT:
                self.direction.rotateAntiClockwise()
            elif self.nextturn.nextTurn == NextTurn.RIGHT:
                self.direction.rotateClockwise()
        
        elif self.direction.direction == Direction.UP or self.direction.direction == Direction.RIGHT:
            if self.nextturn.nextTurn == NextTurn.RIGHT:
                self.direction.rotateClockwise()
            elif self.nextturn.nextTurn == NextTurn.LEFT:
                self.direction.rotateAntiClockwise()

        # set nextturn
        self.nextturn.turn()

    def __repr__(self):
        ''' Representation of a cart when displayed '''
        if self.crashed:
            return ''
        else:
            return str(self.direction)

class Carts():
    '''
    Manages Carts on the track
    Can add a cart or request how many carts are not mark as crashed
    '''
    def __init__(self):
        self.carts = []

    def add(self, cart):
        self.carts.append(cart)

    def notCrashed(self):
        return [cart for cart in self.carts if not cart.crashed]

def processFile(filename):
    track = Track()
    cartId = 1
    with open(filename,"r") as inputFile:
        for y, line in enumerate(inputFile):
            row = []
            for x, c in enumerate(line.strip('\n')):
                if c in ('v','^'): 
                    row.append('|')
                    track.carts.add(Cart(cartId,c,x,y))
                    cartId += 1
                elif c in ('<','>'):
                    row.append('-')
                    track.carts.add(Cart(cartId,c,x,y))
                    cartId += 1
                else:
                    row.append(c)
            track.track.append(row)
        return track


# solve puzzle
track = processFile("input_files/day13.txt")
track.moveCarts()
track.results()
